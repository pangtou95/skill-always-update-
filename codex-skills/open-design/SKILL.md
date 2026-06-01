---
name: open-design
description: Use the nexu-io/open-design repository as a design-generation reference pack for high-quality UI prototypes, landing pages, dashboards, mobile screens, decks, design systems, visual directions, and anti-AI-slop craft rules. Trigger when the user mentions open-design, Claude Design alternatives, design systems, polished frontend prototypes, artifact-first design, or asks for a stronger visual/design workflow.
---

# Open Design

This skill wraps the `nexu-io/open-design` repository for Codex. The repository is not a native Codex `SKILL.md` package, so this file is the Codex entrypoint and the rest of the repository is installed here as reference material.

## What To Use

- Read `README.md` first for the project overview and catalog.
- Read `CONTEXT.md` and `AGENTS.md` when working inside or adapting Open Design itself.
- Use `skills/` for surface-specific design patterns such as landing pages, dashboards, mobile apps, decks, social carousels, motion frames, and docs pages.
- Use `design-systems/` for brand/product design system references.
- Use `design-templates/` for concrete templates and reusable artifact structures.
- Use `craft/` for quality rules: typography, color, hierarchy, accessibility, animation discipline, state coverage, and anti-AI-slop checks.
- Use `prompt-templates/` when the task needs image/video/audio prompt examples.

## Working Style

When applying Open Design to a user request:

1. Identify the requested surface: prototype, landing page, dashboard, mobile screen, deck, poster, email, social carousel, or motion frame.
2. Pick the closest folder under `skills/` and read its README or example files.
3. Pick a design system from `design-systems/` if the user named a brand/style; otherwise choose a coherent visual direction from the Open Design defaults.
4. Apply craft checks from `craft/anti-ai-slop.md`, `craft/typography.md`, `craft/color.md`, `craft/state-coverage.md`, and `craft/accessibility-baseline.md`.
5. Build an actual artifact, not just advice, when the user asks to create or improve a design.

## Important

- Prefer existing Open Design templates and rules over inventing an unrelated visual language.
- Do not bulk-read the whole repository. Open only the specific skill/template/design-system/craft files needed for the task.
- If a local project already has a design system, adapt Open Design patterns to the project instead of replacing the project’s conventions.
