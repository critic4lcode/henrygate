# Adding Source Links to Quotes

This guide explains how to add source links to quotes in the markdown files.

## ⚠️ IMPORTANT: Use ONLY This Pattern

**You MUST use ONLY this exact pattern for ALL source links:**

```markdown
[*](source_key&t=XX)
```

**DO NOT hardcode YouTube URLs directly.** The script will convert all `[*]` patterns to actual URLs automatically.

## Format

Use this format for quotes that need source attribution:

```markdown
> „Quote text here"[*](source_key&t=XX)
```

Where:
- `source_key` is one of: `direkt36_szabo_bence`, `partizan_laczo_adrienn`, `partizan_szabo_bence`, `magyar_kormany_gundalf`, `gundalf_444`
- `XXs` is the timestamp in seconds (e.g., `419s` for 6:59 in the video)

**Never use:** `[*](https://www.youtube.com/...)`  
**Always use:** `[*](source_key&t=XX)`

## Multiple Sources

If a piece of information (quote, statement, or claim) is corroborated by multiple sources, use numbered format:

```markdown
> „Quote text here"[**](source_key_1&t=XX)[**](source_key_2&t=YY)
```

Or for separate quotes from different sources:

```markdown
> „Quote text here"[*](source_key_1&t=XX)

> „Another quote"[**](source_key_2&t=YY)
```

The script will replace all `[*]` patterns with actual URLs.

## Examples

Single source:
```markdown
> „Úgy döntöttem, hogy én kezembe veszem az irányítást..."[*](gundalf_444&t=419)
```

Same information from multiple sources:
```markdown
Henry valójában Vogel Evelin[*](direkt36_szabo_bence&t=3074)[**](partizan_laczo_adrienn&t=1245).
```

Multiple quotes from different sources:
```markdown
> „Az összes szóhasználat..."[*](direkt36_szabo_bence&t=3817)
> „Hogy ilyen szinten bele tudnak folyni..."[**](direkt36_szabo_bence&t=5291)
```

## Video Sources

- **direkt36_szabo_bence**: https://www.youtube.com/watch?v=IXmuE2TX9yE
- **partizan_laczo_adrienn**: https://www.youtube.com/watch?v=2GLvrjKpKRY
- **partizan_szabo_bence**: https://www.youtube.com/watch?v=roI9C9zraLE
- **magyar_kormany_gundalf**: https://www.youtube.com/watch?v=2tqZZL_Bv1w (AH kihallgatás, 2025. szeptember)
- **gundalf_444**: https://www.youtube.com/watch?v=xdlMnQsK_f0 (444.hu interjú, 2026. március 30.)

## Workflow

1. Find the quote in the transcript file (in `public/static/`)
2. Note the timestamp where it appears (the number above the time range in the transcript)
3. Add the source link to the quote in the markdown file using `[*]` or `[**]` format
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
