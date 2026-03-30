# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A modern, clean HTML timeline engine. Events are displayed in a condensed summary view; clicking an event expands it to show full details. Rich content is supported: embedded videos, images, and tables.

## Architecture

**Content authoring** — timeline data is defined in Markdown or JSON files. Markdown files use frontmatter for event metadata (date, title, tags) and the body for rich content. JSON is the alternative for structured/programmatic data.

**Deno server** — reads content files and serves the timeline dynamically during development.

**Static build** — produces a fully self-contained HTML/CSS/JS bundle suitable for deployment to GitHub Pages (no server required at runtime).

## Tech Stack

- **Runtime/build:** Deno
- **Frontend:** Svelte
- **Styling:** Tailwind CSS via [shadcn-svelte](https://www.shadcn-svelte.com/) (component library built on top of Tailwind)

## Transcript Source Files

Transcript files in `public/static/` contain timestamped segments in this format:

```
80
00:01:20 - 00:01:25
én vagyok ez aff.
```

The leading integer on each segment is the **start time in seconds** (pre-computed by `convert_timestamps.py`). When referencing a specific moment from a transcript, always use this seconds value to construct a timestamped YouTube link:

```
https://www.youtube.com/watch?v=VIDEO_ID&t=80
```

- Read the seconds value directly from the source file — do not recompute it from the `HH:MM:SS` timestamp.
- The video ID comes from the event's frontmatter or the filename context.
- Always append `&t=X` (where X is the seconds integer) to deep-link to the exact moment.

## Key Design Decisions

- Content lives in data files (Markdown/JSON), not in code — the engine renders it
- Development mode: Deno dev server with dynamic rendering
- Production mode: static site build output to `dist/` or `docs/` (for GitHub Pages)
- Expand/collapse interaction is handled client-side with no page reload
- All rich media (video, images, tables) must render correctly in both the collapsed summary and expanded detail views
