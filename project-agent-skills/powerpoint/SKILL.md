---
name: powerpoint
description: Create PowerPoint (.pptx) presentations from papers, outlines, briefs, or structured text, and verify the generated deck. Use when the user asks for PPT, slides, a presentation, or a deck that should be produced as an editable .pptx file.
---

# PowerPoint

Create an editable `.pptx`, not merely an outline. This Skill is adapted from the Apache-2.0 `pptx` example in `bojieli/ai-agent-book`; it does not copy the restricted Anthropic PowerPoint Skill shown by some third-party collections.

## Workflow

1. Inspect the source material, audience, language, duration, slide count, and output path.
2. Build a narrative with one purpose per slide. Use concise text and preserve citations for factual claims.
3. Prepare an outline JSON matching `reference.md`.
4. Install the isolated dependency only when needed: `python3 -m pip install python-pptx` inside a project virtual environment.
5. Generate the file:

```bash
python3 scripts/generate_pptx.py outline.json output/deck.pptx
```

6. Reopen the deck with `python-pptx` to verify slide count and text. If rendering tools are available, render every slide and inspect for clipping, overlap, unreadable contrast, and broken media.

## Quality Rules

- Adapt structure to the task; do not force every deck into a paper template.
- Prefer 16:9 for modern presentations unless the user or template requires another ratio. The bundled starter script currently uses 4:3, so disclose that or update it before generation.
- Keep headings compact and body text scannable. Split overloaded slides.
- Never invent data, citations, brand assets, or speaker claims.
- Treat the bundled script as a starter generator. For sophisticated visual decks, use the workspace slide runtime or extend the script, then perform visual verification.

Read `reference.md` for the payload schema and starter styling. The source license is in `references/APACHE-2.0.txt`.
