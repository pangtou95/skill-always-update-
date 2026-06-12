---
name: script-writer
description: Write short-video scripts, spoken-word scripts, livestream outlines, podcast drafts, and hook-to-CTA narration flows. Use when the user asks for script writer or content creator workflow support.
---

# script-writer

This is a local Codex wrapper for the content-creator Top 10 skill list. It preserves the exact skill name from the user's list while keeping the upstream source material in `references/upstream/`.

## Source

- Source repository: `Affitor/affiliate-skills`
- Upstream material: `references/upstream/`

## Operating Rules

1. Load `references/upstream/SOURCE_SKILL.md` before doing substantive work when it exists.
2. Follow the upstream workflow unless the user asks for a narrower output.
3. Keep outputs practical and ready to use: tables, checklists, copy blocks, or structured briefs.
4. Ask only for missing inputs that materially affect quality.
5. Include source/citation/compliance notes when the output could be published publicly.

## Local Adaptation

Use upstream short-form script workflow as the base. Adapt output to the requested channel: short video, talking-head, livestream outline, podcast draft, or ad read.

## Standard Output

Return the requested deliverable first, then add a short `Notes` section with assumptions, missing inputs, and recommended next steps.
