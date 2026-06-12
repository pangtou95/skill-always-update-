---
name: content-research-brief
description: Research topics, collect credible sources, extract data points, and produce a writing-ready content brief. Use when the user asks for content research brief or content creator workflow support.
---

# content-research-brief

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

Use upstream workflow first. Produce a source-backed brief with sources, stats, quotes, risks, and content angles.

## Standard Output

Return the requested deliverable first, then add a short `Notes` section with assumptions, missing inputs, and recommended next steps.
