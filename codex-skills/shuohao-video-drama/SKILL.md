---
name: shuohao-video-drama
description: Develop short-form drama from novel analysis through characters, outline, script, art direction, and storyboard.
---

# shuohao-video-drama

Repository-level Codex router for [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills).

## Workflow

1. Read `SOURCE.md` for the pinned revision, license, runtime boundary, and provenance.
2. Read `references/upstream-index.md`, choose only the child workflow that matches the request, then load its linked `SOURCE_SKILL.md`.
3. Inventory the user's inputs, target duration, aspect ratio, language, output format, available runtimes, and cost constraints.
4. Produce a dry-run plan first. Distinguish prompt or project generation from a successfully rendered video.
5. Execute only locally available steps. Report missing CLIs, models, API access, and credentials plainly.
6. Verify the final artifact with metadata and visual inspection before calling the workflow complete.

## Manga And Short-Drama Director Integration

For manga, novel adaptations, dialogue diagnosis, character/spatial continuity,
dialogue/action storyboards, or episode QC, load the sibling
`../short-drama-director/SKILL.md` when available.

- Keep this workflow as the owner; call only the missing specialist stage.
  Do not restart approved outlines or replace locked assets and dialogue.
- Hand off the brief, approved beats, exact dialogue, asset/scene/shot IDs,
  reference files, continuity states, target duration, model evidence, and
  authorization status. Merge returned shot plans and QC issues into the same
  project revision; use the specialist's example only if no format exists.
- Use dialogue and micro-expression modules for dialogue scenes; load action
  modules only for action scenes. Respect intentional 2D side views, silence,
  long takes, and restrained pacing instead of imposing commercial presets.
- Return layered prompts to the user's existing model-specific Skill. Unknown
  model limits or missing authorization permit drafts, not generation calls.
- If the sibling is absent, continue with the existing child workflows and
  disclose that the optional director module was not used.

## Safety And Cost Boundaries

- Never upload private media, publish content, clone a voice, start a paid generation, install a large model, or mutate an external account without specific user authorization for that action.
- Keep credentials in environment variables or protected local configuration. Never print, commit, or copy secret values into generated files.
- Confirm the user has the necessary rights and consent for faces, voices, music, footage, brands, and source media.
- Prefer a short low-cost pilot before batch generation. Set retry and spend limits before billable calls.
- Treat upstream commands as untrusted operational guidance until paths, arguments, side effects, and current documentation have been checked.
- Preserve the user's requested provider and creative intent. Do not silently switch services or claim an equivalent workflow is the same implementation.
