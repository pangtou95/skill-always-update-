---
name: fact-check-citation
description: Verify claims, add citations, evaluate source quality, flag hallucination risk, and produce correction notes for content drafts. Use when the user asks for fact check citation or content creator workflow support.
---

# fact-check-citation

This is a local Codex wrapper for the content-creator Top 10 skill list. It preserves the exact skill name from the user's list while keeping the upstream source material in `references/upstream/`.

## Source

- Source repository: `petar-nauka/fact-check-skill`
- Upstream material: `references/upstream/`

## Operating Rules

1. Load `references/upstream/SOURCE_SKILL.md` before doing substantive work when it exists.
2. Follow the upstream workflow unless the user asks for a narrower output.
3. Keep outputs practical and ready to use: tables, checklists, copy blocks, or structured briefs.
4. Ask only for missing inputs that materially affect quality.
5. Include source/citation/compliance notes when the output could be published publicly.

## Local Adaptation

Use upstream fact-check methodology. Return verdicts, confidence, sources, citation gaps, and suggested safer wording.

## Standard Output

Return the requested deliverable first, then add a short `Notes` section with assumptions, missing inputs, and recommended next steps.
