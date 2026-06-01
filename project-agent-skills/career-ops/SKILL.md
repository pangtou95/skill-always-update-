---
name: career-ops
description: AI job search command center -- evaluate offers, generate CVs, scan portals, track applications
license: MIT
metadata:
  source: "https://github.com/santifer/career-ops"
  converted-from: "Claude Code skill"
  argument-hint: "[scan | deep | pdf | oferta | ofertas | apply | batch | tracker | pipeline | contacto | training | project | interview-prep | update]"
---

# career-ops -- Router

## Codex Conversion Notes

This Codex skill wraps the upstream `career-ops` project. The original Claude Code skill is a router; its working instructions live in project files such as `modes/`, `templates/`, `batch/`, `config/`, and Node scripts.

The converted skill bundles those files at:

```text
assets/career-ops-template/
```

When invoked:

1. Use the user's current workspace as the active career-ops workspace.
2. If required career-ops files are missing, bootstrap them from `assets/career-ops-template/` into the workspace before running a mode.
3. Preserve existing user files. Do not overwrite `cv.md`, `article-digest.md`, `config/profile.yml`, `modes/_profile.md`, `portals.yml`, `data/*`, `reports/*`, or `output/*` unless the user explicitly asks.
4. For shared system files (`modes/*`, scripts, templates), copy or update from the bundled template only when needed for the requested mode.
5. Codex does not use Claude slash-command arguments; infer the mode from the user's natural-language request or an explicit `$career-ops <mode>` / `career-ops <mode>` phrase.
6. If a mode mentions Claude-specific commands, adapt them to available Codex tools. Use local shell commands for Node scripts. Use browser/tooling available in the current session for scanning or live application tasks.

## Mode Routing

Determine the mode from the user's request:

| Input | Mode |
|-------|------|
| (empty / no args) | `discovery` -- Show command menu |
| JD text or URL (no sub-command) | **`auto-pipeline`** |
| `oferta` | `oferta` |
| `ofertas` | `ofertas` |
| `contacto` | `contacto` |
| `deep` | `deep` |
| `interview-prep` | `interview-prep` |
| `pdf` | `pdf` |
| `training` | `training` |
| `project` | `project` |
| `tracker` | `tracker` |
| `pipeline` | `pipeline` |
| `apply` | `apply` |
| `scan` | `scan` |
| `batch` | `batch` |
| `patterns` | `patterns` |
| `followup` | `followup` |
| `update` | `update` |

**Auto-pipeline detection:** If `$mode` is not a known sub-command AND contains JD text (keywords: "responsibilities", "requirements", "qualifications", "about the role", "we're looking for", company name + role) or a URL to a JD, execute `auto-pipeline`.

If `$mode` is not a sub-command AND doesn't look like a JD, show discovery.

---

## Discovery Mode (no arguments)

Show this menu:

```
career-ops -- Command Center

Available commands:
  /career-ops {JD}      → AUTO-PIPELINE: evaluate + report + PDF + tracker (paste text or URL)
  /career-ops pipeline  → Process pending URLs from inbox (data/pipeline.md)
  /career-ops oferta    → Evaluation only A-F (no auto PDF)
  /career-ops ofertas   → Compare and rank multiple offers
  /career-ops contacto  → LinkedIn power move: find contacts + draft message
  /career-ops deep      → Deep research prompt about company
  /career-ops interview-prep → Generate company-specific interview prep doc
  /career-ops pdf       → PDF only, ATS-optimized CV
  /career-ops training  → Evaluate course/cert against North Star
  /career-ops project   → Evaluate portfolio project idea
  /career-ops tracker   → Application status overview
  /career-ops apply     → Live application assistant (reads form + generates answers)
  /career-ops scan      → Scan portals and discover new offers
  /career-ops batch     → Batch processing with parallel workers
  /career-ops patterns  → Analyze rejection patterns and improve targeting
  /career-ops followup  → Follow-up cadence tracker: flag overdue, generate drafts
  /career-ops update    → Update career-ops system files with diff preview + compat check

Inbox: add URLs to data/pipeline.md → /career-ops pipeline
Or paste a JD directly to run the full pipeline.
```

---

## Context Loading by Mode

After determining the mode, load the necessary files before executing:

### Modes that require `_shared.md` + their mode file:
Read `modes/_shared.md` + `modes/{mode}.md` from the active workspace. If missing, copy them from `assets/career-ops-template/` first.

Applies to: `auto-pipeline`, `oferta`, `ofertas`, `pdf`, `contacto`, `apply`, `pipeline`, `scan`, `batch`

### Standalone modes (only their mode file):
Read `modes/{mode}.md` from the active workspace. If missing, copy it from `assets/career-ops-template/` first.

Applies to: `tracker`, `deep`, `interview-prep`, `training`, `project`, `patterns`, `followup`

### Modes delegated to subagent:
For `scan`, `apply` (with browser automation), and `pipeline` (3+ URLs): use an available subagent tool if present. If no subagent tool is available, execute the mode directly in the current thread with the content of `_shared.md` + `modes/{mode}.md` loaded.

```
Agent(
  subagent_type="general-purpose",
  prompt="[content of modes/_shared.md]\n\n[content of modes/{mode}.md]\n\n[invocation-specific data]",
  description="career-ops {mode}"
)
```

Execute the instructions from the loaded mode file.
