---
name: chatgpt-video-editing
description: Prepare and execute the repository's consent-aware eight-step short-video editing workflow.
---

# chatgpt-video-editing

Repository-level Codex router for [Jaycheng1103/chatgpt-video-editing-skills](https://github.com/Jaycheng1103/chatgpt-video-editing-skills).

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
