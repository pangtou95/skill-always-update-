---
name: taste-skill-frontend-direction
description: Use when applying or curating taste-skill style anti-generic frontend direction, frontend redesign audits, image-to-code workflows, high-end visual design, brand kits, minimalist/brutalist variants, or agent skill packaging based on leonxlnx/taste-skill.
---

# Taste Skill Frontend Direction

Source analyzed: https://github.com/leonxlnx/taste-skill

Use this skill for anti-generic frontend design direction, redesign audits, image-to-code handoff, and packaging design-focused agent skills.

## Repository Shape

- Installable skills live under `skills/`.
- Main default skill: `skills/taste-skill/SKILL.md` with install name `design-taste-frontend`.
- Stricter GPT/Codex variant: `skills/gpt-tasteskill/SKILL.md`.
- Redesign workflow: `skills/redesign-skill/SKILL.md`.
- Image-to-code workflow: `skills/image-to-code-skill/SKILL.md`.
- Visual variants: minimalist, brutalist, soft/high-end, brand kit, frontend image generation, mobile image generation.
- Research notes live under `research/`, especially laziness/remediation material.

## Use The Right Variant

Choose the narrowest skill direction:

- General landing, portfolio, marketing page: use `design-taste-frontend`.
- Existing UI improvement: use `redesign-existing-projects`.
- Strict Codex/GPT frontend work: use `gpt-taste`.
- Screenshot or generated visual to implementation: use `image-to-code`.
- Premium calm visual language: use `high-end-visual-design`.
- Minimal editorial product UI: use `minimalist-ui`.
- Industrial sharp experimental UI: use `industrial-brutalist-ui`.
- Brand boards: use `brandkit`.
- Web or mobile reference image generation: use `imagegen-frontend-web` or `imagegen-frontend-mobile`.

Do not stack every taste skill at once. One design direction should lead.

## Design Read First

Before coding, infer and state a one-line design read:

```text
Reading this as: <page kind> for <audience>, with a <vibe> language, leaning toward <system or aesthetic family>.
```

Then set three dials:

- `DESIGN_VARIANCE`: symmetry vs experimental layout.
- `MOTION_INTENSITY`: static vs cinematic motion.
- `VISUAL_DENSITY`: airy vs dense.

Use the brief, audience, references, and constraints to set these. Public-sector, regulated, and trust-first work should reduce variance and motion.

## Anti-Generic Rules

Avoid common AI defaults unless the brief truly asks for them:

- purple/blue gradient hero;
- centered headline over dark mesh;
- three equal feature cards;
- generic glassmorphism everywhere;
- excessive floating micro-animations;
- default Inter plus slate palette;
- vague product copy that could fit any SaaS.

Instead, anchor decisions in audience, domain, and brand assets.

## Design System Selection

If the brief maps to a real design system, use the official package:

- Microsoft/enterprise: Fluent UI.
- Google/Material: Material Web or Material 3.
- IBM analytics: Carbon.
- Shopify admin: Polaris.
- Atlassian product: Atlaskit.
- GitHub/dev community: Primer.
- UK government: GOV.UK Frontend.
- US government: USWDS.
- Modern owned React components: shadcn/ui or Radix, adjusted beyond defaults.

Do not imitate an official system with ad hoc CSS when an official package is the right foundation.

## Redesign Audit Protocol

For existing projects:

1. Inspect the app before changing styles.
2. Identify hierarchy, spacing, density, typography, color, motion, and responsive issues.
3. Preserve brand assets and product workflows unless the user asked for a full overhaul.
4. Fix the highest-visibility screens first.
5. Verify mobile and desktop screenshots.
6. Remove generic decorative clutter.

## Image-To-Code Protocol

When using images as direction:

1. Generate or inspect reference frames.
2. Extract layout grid, type scale, spacing, colors, surfaces, and motion implications.
3. Implement with real components and responsive constraints.
4. Compare screenshots against reference.
5. Iterate on differences that affect perceived quality.

## Skill Packaging Note

This repository itself is a collection of portable `SKILL.md` files. When creating derivative skills:

- Keep frontmatter `name` and `description` precise.
- Keep `SKILL.md` actionable, not encyclopedic.
- Put large examples or research into references only when needed.
- Avoid extra docs inside a skill folder unless they directly support execution.

