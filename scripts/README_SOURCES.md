# Adding Source Links to Quotes

This guide explains how to add source links to quotes in the markdown files.

## Format

Use this format for quotes that need source attribution:

```markdown
> „Quote text here"[forrás](source_key&t=XXs)
```

Where:
- `source_key` is one of: `direkt36_szabo_bence`, `partizan_laczo_adrienn`, `partizan_szabo_bence`, `magyar_kormany_gundalf`, `gundalf_444`
- `XXs` is the timestamp in seconds (e.g., `419s` for 6:59 in the video)

## Example

```markdown
> „Úgy döntöttem, hogy én kezembe veszem az irányítást..."[forrás](gundalf_444&t=419s)
```

## Video Sources

- **direkt36_szabo_bence**: https://www.youtube.com/watch?v=IXmuE2TX9yE
- **partizan_laczo_adrienn**: https://www.youtube.com/watch?v=2GLvrjKpKRY
- **partizan_szabo_bence**: https://www.youtube.com/watch?v=roI9C9zraLE
- **magyar_kormany_gundalf**: https://www.youtube.com/watch?v=2tqZZL_Bv1w
- **gundalf_444**: https://www.youtube.com/watch?v=xdlMnQsK_f0

## Workflow

1. Find the quote in the transcript file (in `public/static/`)
2. Note the timestamp where it appears
3. Add the source link to the quote in the markdown file
4. Run `python3 scripts/add_source_links.py` to replace all patterns with actual URLs

## Finding Timestamps

To find the timestamp of a quote:
1. Open the transcript file
2. Search for the quote text
3. Count the line number or use the timestamp information in the transcript
4. Convert to seconds (if needed)

The transcript files use this format:
```
XXX
HH:MM:SS - HH:MM:SS
Quote text
```

Where the first number is the line number and the second is the time range.
