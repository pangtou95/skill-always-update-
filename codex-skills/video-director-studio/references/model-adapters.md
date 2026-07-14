# Model And Workflow Adapters

Keep one model-agnostic director pack. Compile separate provider prompts from it; never rewrite the source pack to match one provider's quirks.

## Routing Checklist

1. Confirm the provider/tool is actually installed or connected.
2. Read the installed provider Skill or current official documentation for model names, input limits, regions, pricing, duration, aspect ratios, and audio behavior.
3. Choose `t2v`, `i2v`, `flf2v`, `v2v`, reference-to-video, extension, or editing based on the shot contract and available assets.
4. Map every asset to one primary role and state what must not transfer.
5. Compile one shot per task unless the provider explicitly and reliably supports multi-shot generation.
6. Preserve the director pack and log provider task IDs/results separately.

## Seedance-Compatible

- Prefer Chinese prompt compilation when the installed surface recommends it; still retain bilingual production fields when needed.
- Bind `@` references to explicit roles: first frame, last frame, identity, environment, action, camera, rhythm, audio, product, or wardrobe.
- Source media carries static state; text describes motion, camera, timing, light change, sound, endpoint, and preservation constraints.
- Use timed segments only when the duration and event count support them.
- Route advanced continuity/physics work through `seedance-director-compat` when installed.

## WAN

- Restate essential subject and spatial anchors more explicitly.
- Use one continuous action, clear relative camera, and stable end state.
- For first/last-frame workflows, verify the installed workflow before promising endpoint control.
- Keep negative constraints focused on identity, anatomy, geometry, loops, flicker, camera conflict, and endpoint failure.

## LTX

- Prefer coherent present-tense production English.
- Describe temporal progression and camera relationship in prose rather than keyword piles.
- Keep the audio prompt as a separate sidecar unless the installed workflow defines a native audio field.

## Runway

- Run `rw-check-compatibility` against the intended capability before generation.
- Use `rw-generate-video` or `use-runway-api` for current request fields and task polling.
- Convert each shot contract into a concise action/camera prompt; attach source media through the integration Skill rather than inventing URLs.
- Treat character references, first/last frames, extension, and audio as capability-specific features that require verification.

## Pixelle-Video

- Use `fixed` mode when the director pack already contains approved narration/script.
- Map format beats to `n_scenes`; do not make every sentence a scene.
- Map the look grammar to `prompt_prefix`, shot-specific action to scene prompts, and sound plan to TTS/BGM configuration.
- Choose the media workflow/provider only after checking local ComfyUI, RunningHub, or direct API configuration.
- Exact narrative continuity may require external keyframes or per-shot generation rather than one automatic run.

## LibTV / Liblib

- This Skill can select a compatible LibTV catalog entry or prepare a LibTV-ready brief, but it does not install the creators' hidden Skill packages.
- Actual execution may require a LibTV account, available model, credits, and acceptance of current platform terms.
- Use only public catalog metadata for discovery. Do not replay private API tokens, copy hidden prompts, or scrape authenticated creator content.
- Record the selected template UUID and publication/version metadata because catalog entries can change.

## ChatCut And Postproduction

- Use ChatCut for assembly, trims, captions, exact typography, logos, audio leveling, music, motion graphics, and export when its MCP is connected.
- Verify the visible timeline and export rather than assuming an edit succeeded.
- Keep generated assets local until the user explicitly authorizes upload to an external service.

## Failure Downgrade

If a provider is missing, blocked, paid, region-limited, or incompatible:

1. keep the director pack complete;
2. mark execution `prompt-only`;
3. compile a WAN/LTX/Seedance-compatible fallback only when its assumptions are known;
4. list the exact unresolved capability instead of claiming generation completed.
