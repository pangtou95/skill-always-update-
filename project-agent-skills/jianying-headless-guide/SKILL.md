---
name: jianying-headless-guide
description: Plan and assess local Jianying (CapCut China) headless draft editing on a compatible Apple Silicon Mac, then route an authorized installation of mcncarl/jianying-headless for isolated drafts or explicitly requested exports. Use for 剪映无头剪辑, editable Jianying drafts, existing-draft copies, and native export readiness; this source-linked guide does not bundle the upstream engine.
---

# Jianying Headless Guide

This is an original, source-linked compatibility guide for [mcncarl/jianying-headless](https://github.com/mcncarl/jianying-headless), not its `yichen-jianying-edit` Skill, CLI, codec, or editing engine. Read [SOURCE.md](SOURCE.md) for the pinned source and license boundary. Do not present this guide as a working editor on its own.

## Choose The Right Workflow

- For an editable **local Jianying** draft, consider this route. For a ChatCut cloud project, use the existing `chatcut-*` Skills instead. Do not silently move private footage between products.
- Draft planning needs no Jianying installation. Actual draft creation or export requires authorized access to the upstream core, a compatible local Jianying app, and a passing upstream environment check.
- The user may ask for a new draft, an isolated copy of an existing draft, or an MP4. Default to the reversible draft workflow when the deliverable is unspecified; exporting video is a separate step.

## Before Any Native Operation

1. Confirm Apple Silicon, macOS and Jianying versions against the current [upstream README](https://github.com/mcncarl/jianying-headless#%E7%8E%AF%E5%A2%83). The pinned source described macOS 26+, Jianying 11.4.0/11.4.2 for drafts and 11.4.2 for native export; these are version-specific, not universal compatibility claims.
2. Locate an authorized checkout of the core. A copied Skill or this guide does not grant access to it. If the checkout is separate, `JIANYING_HEADLESS_ROOT` may identify its local path. Never search for credentials, account data, official libraries, or hidden caches to manufacture access.
3. Follow the upstream [standalone Skill instructions](https://github.com/mcncarl/jianying-headless/blob/main/skills/yichen-jianying-edit/SKILL.md) and run its `doctor` before writing drafts. If version, signature, bridge hash, or permissions fail, stop native operations. Do not patch constants, remove verification, acquire paid effects, or pretend a generic FFmpeg render is a native Jianying export.
4. Record the requested source media, rights, target aspect ratio, timeline edits, subtitles, audio, output directory, and whether native export was explicitly requested. For uncertain content cuts, preserve source material and request a decision before destructive interpretation.

## Draft, Publish, Export

- Build only in a new isolated working directory; keep source media and existing Jianying projects unchanged. For modifying an existing draft, use the upstream isolated-copy workflow, not in-place edits.
- Consult the current [plan format](https://github.com/mcncarl/jianying-headless/tree/main/docs) and commands in the upstream README at execution time. Check source paths and media metadata before building; run upstream build verification after building.
- Upstream `publish` means registering a draft on the **local Jianying home screen**, not posting online. Only do that after the user has saved work and quit Jianying, as required by the upstream workflow. Do not force-quit the app.
- Export only when the user asks for a finished video and the pinned profile supports it. Verify the resulting file's duration, streams, representative frames, subtitles and audible sections; a file existing is not proof of correct content.
- If prerequisites are unavailable, deliver a reviewable edit plan and an exact dependency gap report. Do not claim that the plan is an editable native draft or rendered MP4.

## Rights And Distribution

The upstream license allows personal non-commercial study/use but forbids public redistribution of the repository or a derivative packaged skill collection without written permission. This library therefore links to the source and copies none of its Skill text, scripts, engine, bridge, codec, or official assets. Check the [upstream license](https://github.com/mcncarl/jianying-headless/blob/main/LICENSE) and third-party notices before use; commercial/business use requires the right holder's written authorization. This guide grants no Jianying software, effects, footage, music, or account rights.
