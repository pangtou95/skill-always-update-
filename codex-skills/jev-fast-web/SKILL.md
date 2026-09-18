---
name: jev-fast-web
description: Use an optional, locally installed Jev Ultrafast browser agent for bounded Chrome web tasks with structured DOM controls. Choose it for simple public web navigation or form research when TypeSafe and text-model keys are available; use existing Computer Use for desktop apps, uploads, canvas, frames, or sensitive account workflows. Includes an offline browser probe and a guarded terminal entrypoint.
---

# Jev Fast Web

This Skill exposes an optional terminal function built around [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast). It does not replace Codex's built-in Computer Use engine. The upstream MIT code is installed separately; this package contains only an adapter and source record.

## Route

- Prefer a direct API, connector, or the existing browser/computer tool when it already serves the task well. Use Jev for ordinary visible HTML controls on a known Chrome page, especially repetitive navigation or selection where lower observation latency matters.
- Do not use this route for native macOS apps, uploads, canvas, iframes, shadow-root controls, pop-up tabs, payment, account changes, private authenticated sessions, or any action needing a human approval checkpoint. The upstream MVP does not fully support several of these browser surfaces.
- Keep the user's browser profile out of untrusted experiments. Use an isolated Chrome profile and local fixture for probes. A live task may use the configured browser only when its scope and data exposure are understood.

## Local Function

The installed runtime is expected in a separate Python 3.12+ environment, not bundled into this Skill. Run the adapter with that environment's Python:

```bash
~/.local/share/codex-jev-ultrafast/.venv/bin/python scripts/jev_fast_web.py check
~/.local/share/codex-jev-ultrafast/.venv/bin/python scripts/jev_fast_web.py probe --iterations 30
```

The relative script path above is inside this Skill folder; use its absolute path from the installed location. `check` prints only readiness booleans, never key values. `probe` measures DOM observation on a generated local fixture without model calls. Its median is not an end-to-end speedup claim.

For a bounded live task, set `TYPESAFE_API_KEY` and `TEXT_MODEL_API_KEY` in the environment, connect Chrome via Browser Harness, then call:

```bash
~/.local/share/codex-jev-ultrafast/.venv/bin/python scripts/jev_fast_web.py run \
  --url https://example.org/ --allow-host example.org \
  --goal 'Open the requested public article' \
  --expect-url-prefix https://example.org/articles/ --max-actions 12 --live
```

The command opens its own tab, limits executed actions, checks the observed host after each step, and prints only summary metadata. It does not log page bodies or generated text. The explicit `--live` flag prevents accidental API spending. A model's `DONE` is never proof of task success: provide a target URL prefix or expected visible text and inspect the final page. Host checking is not a network security boundary or a guarantee against writes. For sensitive workflows, use a different tool with the appropriate approval and verification surface.

If either key, compatible Chrome/CDP connection, or runtime is absent, stop at `check` or `probe` and report the exact gap. Do not solicit or store key values in the skill library, use a paid API without authorization, or claim that installing instructions alone makes the built-in Computer Use faster. See [SOURCE.md](SOURCE.md) for the pinned upstream version and benchmark limitations.
