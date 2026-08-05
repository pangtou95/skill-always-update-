# Design Patterns

## Use Cases

### Primary Action Button

- Prefer `sm`, `mono` or brand colors, strength `0.55-0.8`.
- Activate on focus/hover or for a short first-visit cue.
- Keep the button fill, label contrast, press state, and focus outline independently complete.

### Icon Button

- Use `sm`; preserve a stable square/circle footprint.
- The beam must not resize the icon or hit target.
- Provide tooltip and accessible name when the symbol is unfamiliar.

### Input Or Search Bar

- Use `line` for active processing or focus progression.
- Keep error/success borders static and semantically colored.
- Do not put continuous movement under long text entry unless it represents work in progress.

### Selected Card

- Prefer `pulse-inner`, low strength, static/brand color.
- Selection must also be visible through fill, checkmark, label, or ARIA state.
- Never animate all cards in a repeated grid.

### Loading Or Agent Working State

- Prefer `line` or `pulse-inner` with status text and `aria-live` where appropriate.
- Stop the animation when work ends, fails, pauses, or moves offscreen.

### Success Moment

- Use `pulse-outside` briefly, then fade to a stable success state.
- Reserve space for bloom and test ancestor clipping.

## Restraint Scale

| Surface | Persistent beams | Recommended behavior |
| --- | --- | --- |
| Dense dashboard/table | 0 | event-triggered only |
| Standard app screen | 0-1 | selected or primary action |
| Focused tool/modal | 1 | active working state |
| Marketing first viewport | 1-2 | one CTA plus one product focal point |
| Component showcase | several | demo-only, pause inactive/offscreen examples |

## Avoid

- Rainbow defaults unrelated to the brand.
- Glow as the only disabled, selected, error, success, or focus signal.
- High bloom behind text or thin icons.
- Multiple animation speeds competing on one screen.
- Beam effects nested inside other beam effects.
- Permanent motion in operational tables, navigation, settings, or destructive controls.
- `pulse-outside` inside clipped cards, carousels, or `overflow: hidden` containers without deliberate accommodation.
