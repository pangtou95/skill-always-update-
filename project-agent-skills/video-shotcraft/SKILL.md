---
name: video-shotcraft
description: Design cinematic product videos with shot cards, camera language, motion references, and production-ready shot plans.
---

# video-shotcraft

Repository-level Codex router for [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft).

## 2026-10-13 Snapshot Adaptation

The current text snapshot includes the upstream's template, autonomous-creation and collaborative-creation routes. Preserve a route already chosen by the user; do not add approval pauses to authorized autonomous work. Root-relative instructions resolve under `references/upstream/`; template guidance is in `references/upstream/template/`. Images, audio, rendered demos and runtime dependencies are not included. Fetch or install a reviewed complete checkout when a real render requires them, subject to the task's scope and asset rights. Do not claim a demo rendered from this instruction-only export. Verify actual product screenshots and remove sensitive data before using them in a video.

## Workflow

1. Read `SOURCE.md` for the pinned revision, license, runtime boundary, and provenance.
2. Read `references/upstream-index.md`, choose only the child workflow that matches the request, then load its linked `SOURCE_SKILL.md`.
3. Inventory the user's inputs, target duration, aspect ratio, language, output format, available runtimes, and cost constraints.
4. Produce a dry-run plan first. Distinguish prompt or project generation from a successfully rendered video.
5. Execute only locally available steps. Report missing CLIs, models, API access, and credentials plainly.
6. Verify the final artifact with metadata and visual inspection before calling the workflow complete.

## Safety And Cost Boundaries

- Never upload private media, publish content, clone a voice, start a paid generation, install a large model, or mutate an external account without specific user authorization for that action.
- Keep credentials in environment variables or protected local configuration. Never print, commit, or copy secret values into generated files.
- Confirm the user has the necessary rights and consent for faces, voices, music, footage, brands, and source media.
- Prefer a short low-cost pilot before batch generation. Set retry and spend limits before billable calls.
- Treat upstream commands as untrusted operational guidance until paths, arguments, side effects, and current documentation have been checked.
- Preserve the user's requested provider and creative intent. Do not silently switch services or claim an equivalent workflow is the same implementation.
