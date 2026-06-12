---
name: viral-hook-title
description: Write viral titles, opening hooks, scroll-stoppers, curiosity gaps, and A/B hook variants for social and content campaigns. Use when the user asks for viral hook title or content creator workflow support.
---

# viral-hook-title

This is a local Codex wrapper for the content-creator Top 10 skill list. It preserves the exact skill name from the user's list while keeping the upstream source material in `references/upstream/`.

## Source

- Source repository: `EvolutionAPI/evo-nexus`
- Upstream material: `references/upstream/`

## Operating Rules

1. Load `references/upstream/SOURCE_SKILL.md` before doing substantive work when it exists.
2. Follow the upstream workflow unless the user asks for a narrower output.
3. Keep outputs practical and ready to use: tables, checklists, copy blocks, or structured briefs.
4. Ask only for missing inputs that materially affect quality.
5. Include source/citation/compliance notes when the output could be published publicly.

## Local Adaptation

Use upstream hook patterns. Always return multiple variants grouped by pattern and include a short rationale plus A/B test recommendation.

## Standard Output

Return the requested deliverable first, then add a short `Notes` section with assumptions, missing inputs, and recommended next steps.
