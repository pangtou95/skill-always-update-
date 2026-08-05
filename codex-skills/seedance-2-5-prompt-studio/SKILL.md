---
name: seedance-2-5-prompt-studio
description: Design, audit, and compile Seedance 2.5 video prompts for up-to-30-second storytelling, multimodal reference-to-video, one-take sequences, native audio and dialogue, timestamp editing, product films, VFX, animation, tutorials, multilingual scenes, and controlled video edits. Use when the user names Seedance 2.5 or needs a production-ready prompt with a timed beat sheet, reference-role map, continuity locks, audio lanes, and failure constraints. Verify the selected provider before claiming generation is available.
---

# Seedance 2.5 Prompt Studio

Convert a video idea or asset set into a production-ready Seedance 2.5 prompt pack. This Skill synthesizes reusable structures from ByteDance's official launch material and an audit of EvoLink's public 122-card prompt gallery; it does not reproduce the gallery's full prompts.

## Verify Availability First

Treat model release, consumer access, first-party API access, and third-party routes as separate facts.

1. Record the date, region, product/provider, account state, visible model name, and intended mode.
2. Verify current limits, accepted assets, duration, resolution, audio, pricing, and request schema on the selected surface.
3. If the route cannot be called, set `availability.status` to `prompt-only` or `docs-only`. Do not claim that a video was generated.
4. As inspected on 2026-08-05: Seedance 2.5 had launched and was rolling out in Jimeng/Doubao; ByteDance announced up to 30 seconds, 30 images, 10 videos, 10 audio clips, extension, and timestamp editing. EvoLink's generation route was still pending and its page said first-party API access would open on 2026-08-07. Recheck after that date.

Read [references/capability-ledger.md](references/capability-ledger.md) before making operational claims.

## Route The Creative Task

Choose one primary format family. Combine families only when the timeline can still be read clearly.

| Intent | Format family | Core control |
| --- | --- | --- |
| Abstract transformations or graphic worlds | motion graphics | material carrier, transition physics, loop endpoint |
| Brand concept or fashion film | brand film | brand carrier, visual thesis, reveal frame |
| Transformation, compositing, impossible physics | VFX | source, material behavior, interaction, dissipation |
| Narrative or atmospheric sequence | cinematic film | setup, development, turn, resolution |
| Product demonstration | product ad | geometry lock, feature proof, clean hero ending |
| Stylized or cel animation | animation | line/color lock, pose keys, controlled in-betweens |
| Continuous spatial journey | 30-second one-take | route map, occlusion bridges, camera axis |
| Instructional procedure | tutorial | ordered steps, hands/tools, verification state |
| Dialogue, vlog, ASMR, performance | native audio/dialogue | speaker map, audio lanes, lip-sync windows |
| Localized spoken or visible language | multilingual | language-by-speaker/beat map, text verification |
| Existing video modification | video editing | invariant list, change list, timestamp scope |
| Sci-fi or fantasy continuity | worldbuilding | world rules, faction/character locks, spatial logic |

For full TVCs, stories, MVs, or multi-platform packages, first use `video-director-studio`. Use this Skill to compile its director pack for Seedance 2.5.

For OpenNana gallery requests, broad image/video format exploration, or a generated-key-image-to-video workflow, first use `opennana-image-video-prompt-studio`. Then compile its video route or bridge pack here with current Seedance 2.5 capability checks.

## Build The Prompt Pack

### 1. Declare The Mode And Deliverable

Specify `t2v`, `i2v`, `r2v`, `edit`, or `extend`; duration; aspect ratio; destination; language; and whether audio is native, supplied, or post-produced.

### 2. Assign Every Reference One Primary Role

Give each asset exactly one primary role: `identity`, `product`, `environment`, `style`, `motion`, `camera`, `timing`, `voice`, `music`, `first_frame`, `last_frame`, `clay_layout`, or `edit_source`.

For each reference state:

- what to transfer;
- what to preserve;
- what must not transfer;
- the beats where it is active.

When many references are used, add a cast/asset isolation matrix. Numbered grids must state which cells belong to which person, prop, costume, or shot. Never let a style reference silently replace identity or geometry.

### 3. Write A Timed Beat Sheet

- For 4-15 seconds, use one to three visible beats.
- For 20-30 seconds, prefer four to six timestamped beats.
- Give each beat one narrative purpose, one main subject action, one camera instruction, one audio cue, and one transition or stable endpoint.
- Make adjacent beats causally connect. A prop, gesture, camera occlusion, sound accent, shape, color, or motion vector can carry continuity across the cut.
- For a one-take, replace cuts with a physical route and motivated bridges such as foreground occlusion, doorway passage, whip-pan, reflection, tunnel, or object match.

### 4. Separate Control Lanes

Keep these instructions distinct even when the final surface receives one text prompt:

1. subject and performance;
2. environment and blocking;
3. camera and lens;
4. edit/transition;
5. light, material, and color;
6. dialogue and voice;
7. music, ambience, and Foley;
8. visible text and typography;
9. preservation and negative constraints.

### 5. Add Locks And Exclusions

Lock only what matters: identity, age, wardrobe, product geometry, prop count, camera axis, scene geography, language/speaker assignment, music phase, and final frame.

Use targeted exclusions tied to likely failures: extra people, face swaps, role leakage, duplicate limbs, prop mutation, reference-grid mixing, text corruption, subtitle generation, camera drift, unwanted cuts, audio-role swaps, repeated actions, or a changed ending. Do not append a generic wall of unrelated negatives.

### 6. Compile And Validate

Return:

1. availability record and provider caveat;
2. format family, mode, duration, and aspect ratio;
3. reference-role and cast-isolation maps;
4. timed beat sheet;
5. compact final prompt in the surface's preferred language;
6. dialogue/audio cue sheet;
7. invariants, change-only instructions, and negative constraints;
8. evaluation checklist and fallback plan.

Start from [assets/seedance25-pack.json.template](assets/seedance25-pack.json.template) and validate it:

```bash
python3 scripts/validate_seedance25_pack.py PACK.json
```

Read [references/pattern-library.md](references/pattern-library.md) for the gallery-derived pattern system and [references/prompt-templates.md](references/prompt-templates.md) for original reusable templates.

## Evaluation

Review the full output, not only the first frame. Score:

- beat order and duration adherence;
- identity, product, wardrobe, and prop stability;
- camera path, axis, and endpoint;
- transition causality and one-take continuity;
- action physics and object contact;
- dialogue speaker, language, lip-sync, and voice stability;
- music/ambience/Foley synchronization;
- text correctness and absence of unwanted subtitles/logos;
- exact compliance with edit invariants and final state.

Change one control lane per iteration when diagnosing failures. Preserve the accepted seed, assets, and prompt version for A/B comparison.

## Rights And Safety

- Use only owned, licensed, public-domain, or authorized reference media.
- Do not clone a real person's face or voice without authorization.
- Treat community examples as inspiration and unverified reports, not product guarantees.
- Do not copy entire gallery prompts into deliverables. Rebuild the user's prompt from the structural patterns and their own assets.
