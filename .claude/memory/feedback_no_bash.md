---
name: Avoid bash commands, use file tools
description: User prefers Read/Grep/Glob over bash for file exploration; use MCP servers for framework-specific queries
type: feedback
---

Don't run bash commands to explore files or search code. Use Read, Grep, and Glob tools instead.

**Why:** User explicitly corrected this — bash commands are unnecessary when dedicated file tools exist.

**How to apply:** For file reading/searching, always use Read/Grep/Glob. For Svelte-specific questions (component syntax, docs), use the Svelte MCP server instead of reading node_modules. Only use Bash for things that truly require shell execution (running a build, starting a dev server, etc.).
