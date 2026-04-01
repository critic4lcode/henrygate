import argparse
import re


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
    return re.sub(r"<font[^>]*>|</font>", "", text)


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


def convert_file(path, inplace=False):
    with open(path, encoding="utf-8") as f:
        content = f.read()

    result = convert_srt(content)

    if inplace:
        with open(path, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        print(result, end="")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="SRT transcript file to process")
    parser.add_argument("--inplace", action="store_true", help="Modify the file in place")
    args = parser.parse_args()
    convert_file(args.file, inplace=args.inplace)
