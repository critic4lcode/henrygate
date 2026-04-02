import argparse
import re
import sys
import os


def timestamp_to_seconds(ts):
    """Convert HH:MM:SS or HH:MM:SS,mmm to integer seconds."""
    ts = ts.strip().split(",")[0]  # drop milliseconds if present
    parts = ts.split(":")
    parts = [int(p) for p in parts]
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    elif len(parts) == 2:
        return parts[0] * 60 + parts[1]
    return int(parts[0])


def format_ts(ts):
    """Return HH:MM:SS from a timestamp that may include milliseconds."""
    return ts.strip().split(",")[0]


def strip_font_tags(text):
    text = re.sub(r"<font[^>]*>|</font>", "", text)
    text = re.sub(r"^>>\s*", "", text.strip())
    return text


def convert_srt(content):
    """Convert SRT format to the target format with leading second timestamps."""
    # Split into blocks separated by blank lines
    blocks = re.split(r"\n\s*\n", content.strip())
    output_parts = []

    srt_ts_pattern = re.compile(
        r"(\d{2}:\d{2}:\d{2}[,\.]\d+)\s*-->\s*(\d{2}:\d{2}:\d{2}[,\.]\d+)"
    )

    for block in blocks:
        lines = block.strip().splitlines()
        if not lines:
            continue

        # Find the timestamp line
        ts_line_idx = None
        for i, line in enumerate(lines):
            if srt_ts_pattern.match(line.strip()):
                ts_line_idx = i
                break

        if ts_line_idx is None:
            continue  # skip malformed blocks

        ts_match = srt_ts_pattern.match(lines[ts_line_idx].strip())
        start_ts = ts_match.group(1)
        end_ts = ts_match.group(2)

        seconds = timestamp_to_seconds(start_ts)
        formatted_start = format_ts(start_ts)
        formatted_end = format_ts(end_ts)

        # Text lines follow the timestamp line
        text_lines = lines[ts_line_idx + 1:]
        text = " ".join(strip_font_tags(l).strip() for l in text_lines if l.strip())

        output_parts.append(f"{seconds}\n{formatted_start} - {formatted_end}\n{text}")

    return "\n\n".join(output_parts) + "\n"


def check_ytdlp():
    """Check yt-dlp installation and version. Prompt user to update if outdated."""
    try:
        import yt_dlp
        from yt_dlp.version import __version__ as installed_version
    except ImportError:
        print("yt-dlp is not installed. Please install it with: pip install yt-dlp")
        sys.exit(1)

    print(f"yt-dlp version: {installed_version}")

    try:
        import urllib.request
        import json
        url = "https://pypi.org/pypi/yt-dlp/json"
        with urllib.request.urlopen(url, timeout=5) as resp:
            data = json.loads(resp.read())
        latest_version = data["info"]["version"]
        from packaging.version import Version
        if Version(latest_version) > Version(installed_version):
            print(f"A newer version of yt-dlp is available: {latest_version}")
            answer = input("Would you like to update yt-dlp now? [y/N] ").strip().lower()
            if answer == "y":
                import subprocess
                subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"])
                print("yt-dlp updated. Please re-run the script.")
                sys.exit(0)
    except Exception:
        pass  # Version check is best-effort


def download_srt(youtube_url, output_dir="."):
    """Download Hungarian SRT transcript for a YouTube video using yt-dlp Python API.
    Returns the path to the downloaded .srt file, or None on failure."""
    try:
        import yt_dlp
    except ImportError:
        print("yt-dlp is not installed. Please install it with: pip install yt-dlp")
        return None

    output_template = os.path.join(output_dir, "transcript.%(ext)s")
    ydl_opts = {
        "skip_download": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["hu"],
        "subtitlesformat": "ttml",
        "postprocessors": [{
            "key": "FFmpegSubtitlesConvertor",
            "format": "srt",
            "when": "before_dl",
        }],
        "outtmpl": output_template,
        "quiet": False,
    }

    print(f"Downloading transcript for: {youtube_url}")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
    except Exception as e:
        print(f"yt-dlp failed to download the transcript: {e}")
        return None

    # Find the downloaded .srt file
    for fname in os.listdir(output_dir):
        if fname.startswith("transcript") and fname.endswith(".srt"):
            return os.path.join(output_dir, fname)

    print("No .srt file found after download.")
    return None


def convert_to_text_only(content):
    """Convert SRT to plain concatenated text, stripping timestamps and sequence numbers."""
    blocks = re.split(r"\n\s*\n", content.strip())
    text_parts = []

    srt_ts_pattern = re.compile(
        r"(\d{2}:\d{2}:\d{2}[,\.]\d+)\s*-->\s*(\d{2}:\d{2}:\d{2}[,\.]\d+)"
    )

    for block in blocks:
        lines = block.strip().splitlines()
        if not lines:
            continue

        ts_line_idx = None
        for i, line in enumerate(lines):
            if srt_ts_pattern.match(line.strip()):
                ts_line_idx = i
                break

        if ts_line_idx is None:
            continue

        text_lines = lines[ts_line_idx + 1:]
        text = " ".join(strip_font_tags(l).strip() for l in text_lines if l.strip())
        if text:
            text_parts.append(text)

    return " ".join(text_parts) + "\n"


def convert_processed_to_text_only(content):
    """Convert already-processed transcript (seconds/timerange/text blocks) to plain concatenated text."""
    blocks = re.split(r"\n\s*\n", content.strip())
    text_parts = []

    for block in blocks:
        lines = block.strip().splitlines()
        if len(lines) < 3:
            continue
        # line 0: seconds (integer)
        # line 1: HH:MM:SS - HH:MM:SS
        # line 2+: text
        if not lines[0].strip().isdigit():
            continue
        text = " ".join(lines[2:]).strip()
        if text:
            text_parts.append(text)

    return " ".join(text_parts) + "\n"


def convert_file(path, inplace=False):
    with open(path, encoding="utf-8") as f:
        content = f.read()

    result = convert_srt(content)

    if inplace:
        with open(path, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        print(result, end="")


def interactive_mode():
    """Prompt for a YouTube URL, download and process the transcript."""
    check_ytdlp()
    youtube_url = input("Paste the YouTube URL: ").strip()
    if not youtube_url:
        print("No URL provided. Exiting.")
        sys.exit(1)

    srt_path = download_srt(youtube_url)
    if srt_path is None:
        sys.exit(1)

    print(f"Downloaded SRT: {srt_path}")
    answer = input(f"Output file name (leave empty to overwrite {srt_path}): ").strip()
    if answer == "":
        convert_file(srt_path, inplace=True)
        out_path = srt_path
        print(f"Processed transcript saved to: {srt_path}")
    else:
        with open(srt_path, encoding="utf-8") as f:
            content = f.read()
        result = convert_srt(content)
        with open(answer, "w", encoding="utf-8") as f:
            f.write(result)
        out_path = answer
        print(f"Processed transcript saved to: {answer}")

    text_answer = input("Do you want a concatenated plain text version? [y/N] ").strip().lower()
    if text_answer == "y":
        with open(out_path, encoding="utf-8") as f:
            processed_content = f.read()
        # Re-read original SRT for text extraction
        with open(srt_path, encoding="utf-8") as f:
            original_content = f.read()
        plain_text = convert_to_text_only(original_content)
        txt_path = os.path.splitext(out_path)[0] + "_concat.txt"
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(plain_text)
        print(f"Plain text saved to: {txt_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download and process YouTube transcripts, or process an existing SRT file."
    )
    parser.add_argument(
        "file", nargs="?", help="SRT transcript file to process (omit to enter interactive download mode)"
    )
    parser.add_argument("--inplace", action="store_true", help="Modify the file in place")
    parser.add_argument(
        "--text-only", action="store_true",
        help="Convert an already-processed transcript file to concatenated plain text"
    )
    args = parser.parse_args()

    if args.file:
        if args.text_only:
            with open(args.file, encoding="utf-8") as f:
                content = f.read()
            plain_text = convert_processed_to_text_only(content)
            txt_path = os.path.splitext(args.file)[0] + "_concat.txt"
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(plain_text)
            print(f"Plain text saved to: {txt_path}")
        else:
            convert_file(args.file, inplace=args.inplace)
    else:
        interactive_mode()
