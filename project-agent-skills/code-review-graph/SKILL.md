---
name: code-review-graph
description: Install and operate tirth8205/code-review-graph from Codex to build a local Tree-sitter code knowledge graph, inspect architecture, review diffs and pull requests, trace impact, debug issues, plan refactors, and generate repository maps through its CLI or MCP tools. Use when the user names code-review-graph or needs graph-assisted code analysis.
---

# Code Review Graph

This Skill operates the external `code-review-graph` package. It does not bundle the application or assume its MCP server is configured.

## Setup

1. Check `python3 --version`; upstream requires Python 3.10 or newer.
2. Prefer `uv tool install code-review-graph` or `pipx install code-review-graph`.
3. Configure Codex with `code-review-graph install --platform codex`.
4. Restart Codex when MCP configuration changed.
5. In the target Git repository, run `code-review-graph build`, then `code-review-graph status`.

## Workflow

Start graph-assisted tasks with the smallest useful context. When MCP tools are available, call `get_minimal_context(task=...)` first and request minimal detail before escalating.

| Intent | Preferred route |
| --- | --- |
| Initialize or refresh | `build` or `update`, then `status` |
| Understand architecture | architecture overview, communities, flows |
| Review a diff or PR | review context, affected flows, impact radius, tests |
| Debug | semantic search, callers/callees, flows, recent changes |
| Refactor | preview impact, inspect affected flows, apply only after review |
| Export | `visualize`, `wiki`, or GraphML/SVG/Obsidian/Cypher output |

Use graph output to choose files, then read the actual source and run the repository's tests. A graph is an index, not proof of runtime behavior. Never commit `.code-review-graph/` data unless the project explicitly wants it tracked.

Read `references/source.md` for the inspected release surface and license.
