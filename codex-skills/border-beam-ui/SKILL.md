---
name: border-beam-ui
description: Design, implement, and audit restrained animated border-beam treatments for buttons, icon controls, inputs, search bars, cards, selected states, and status surfaces. Use when a frontend needs traveling border light, bottom-line motion, inner breathing glow, outer bloom, React border-beam integration, or a CSS fallback with accessibility, reduced-motion, overflow, focus, performance, theme, and visual-restraint checks.
license: MIT
---

# Border Beam UI

Use luminous borders as a state or hierarchy signal, not as default decoration. This Skill is based on the MIT-licensed `Jakubantalik/border-beam` package and adds design selection, framework routing, accessibility, restraint, and QA rules.

## Preflight

Inspect the existing framework, React version, package manager, tokens, control states, border radii, motion stance, overflow ancestry, and light/dark themes.

- React 18+: prefer the upstream `border-beam` package.
- Existing component library: wrap its semantic control; do not replace it.
- Vue, Svelte, or vanilla: use the CSS fallback in [references/implementation-recipes.md](references/implementation-recipes.md), adapted to existing tokens.
- No established motion language: default to static hairline or event-triggered `mono`, not a permanent rainbow loop.

Read [references/upstream-api.md](references/upstream-api.md) when using the package. Read [references/design-patterns.md](references/design-patterns.md) before choosing an effect.

## Select One Effect

| Intent | Preset | Typical target |
| --- | --- | --- |
| Compact traveling accent | `sm` | icon button, compact CTA |
| Full traveling perimeter | `md` | one primary card or hero CTA |
| Directional progress/accent | `line` | input, search, command bar |
| Quiet contained status | `pulse-inner` | selected card, working state |
| Celebratory/attention halo | `pulse-outside` | success, activation, rare CTA moment |

Use `mono` for work tools and quiet interfaces, brand-derived colors when available, `ocean` only when blue-violet belongs to the palette, and `sunset` for warm brands or warnings that are not destructive. Do not let the preset choose the product palette.

## Implementation Rules

1. Preserve native semantics. The beam wrapper is decorative and must not own button, link, input, disabled, loading, error, or success behavior.
2. Keep a real idle edge. Use the component's existing border or inset 1px hairline so the control remains legible when animation is off.
3. Match radii exactly. Prefer auto-detection; pass `borderRadius` when nested wrappers or computed styles make it ambiguous.
4. Preserve layout. The upstream wrapper is a `div`; give button/icon wrappers an explicit `inline-flex`, `width: fit-content`, and stable dimensions when block layout would alter sizing or grid/flex behavior.
5. Keep effect layers non-interactive with `pointer-events: none` and out of the accessibility tree.
6. Keep focus visible without animation. A beam may supplement, never replace, a high-contrast `:focus-visible` outline.
7. Gate activity. Prefer hover, focus, selected, loading, newly available, or short success windows. On dense screens, keep no more than one persistent beam in a viewport.
8. Respect reduced motion. Pulse presets handle it upstream; consumers must disable or freeze rotate presets under `prefers-reduced-motion: reduce`.
9. Check clipping. `pulse-outside` requires an opaque child and visible overflow through every ancestor that should show the bloom.
10. Adapt light and dark themes separately. Recheck edge contrast and bloom strength on both surfaces.
11. Do not animate destructive actions, every card, table rows, routine navigation, disabled controls, or long-form reading surfaces.

## React Route

Install and use the official package:

```bash
npm install border-beam
```

```tsx
import { BorderBeam } from 'border-beam';

<BorderBeam className="beamButtonWrap" size="sm" colorVariant="mono" theme="auto" active={isEmphasized} strength={0.72}>
  <button className="primaryAction">Create project</button>
</BorderBeam>
```

Do not add the dependency if the repository already has an equivalent maintained component. Follow its package manager and lockfile conventions.

## State Design

- Default: stable hairline, beam normally off.
- Hover: optional soft activation on precise-pointer devices only.
- Focus-visible: static accessible outline plus optional beam.
- Active/pressed: reduce bloom; preserve tactile press feedback.
- Disabled: no animation and no misleading glow.
- Loading: `line` or `pulse-inner`, with text/progress semantics.
- Error: use established error tokens; avoid celebratory hue cycling.
- Success: short `pulse-outside`, then settle to the normal success state.

For Hallmark component work, include these states in its eight-state preview.

## Verify

Run [scripts/audit_beam_usage.py](scripts/audit_beam_usage.py) against the changed component or project:

```bash
python3 scripts/audit_beam_usage.py PATH
```

Then verify keyboard focus, screen-reader semantics, reduced motion, light/dark themes, 320/375/414/768 widths, hover-capable and touch devices, offscreen pausing, clipping, and stable layout. Use browser screenshots for default, active, focus, reduced-motion, and mobile states.

## Provenance

The upstream source was inspected at commit `647d26e2a27f26587110fea5a8410c80deb5ac5e` on 2026-08-05. See [references/upstream-api.md](references/upstream-api.md) and [LICENSE.upstream](LICENSE.upstream). Do not present local CSS fallbacks as upstream source code.
