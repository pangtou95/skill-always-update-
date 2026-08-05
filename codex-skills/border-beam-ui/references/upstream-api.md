# Upstream API And Capability Ledger

Sources inspected on 2026-08-05:

- Demo: <https://beam.jakubantalik.com/>
- Repository: <https://github.com/Jakubantalik/border-beam>
- Commit: `647d26e2a27f26587110fea5a8410c80deb5ac5e`
- Repository package manifest version: `1.4.0`
- npm `latest` version: `1.3.0`
- License: MIT

The repository was ahead of the npm `latest` tag at inspection time. Recheck the installed package version before relying on exact defaults or newly documented behavior.

## Public Props

| Prop | Values/default | Purpose |
| --- | --- | --- |
| `size` | `sm`, `md`, `line`, `pulse-outside`, `pulse-inner`; default `md` | effect geometry and motion family |
| `colorVariant` | `colorful`, `mono`, `ocean`, `sunset`; default `colorful` | palette preset |
| `theme` | `dark`, `light`, `auto`; default `dark` | surface adaptation |
| `strength` | `0..1`; default `1` | beam-layer intensity only |
| `duration` | rotate `1.96`, line `3.1`, pulse `2.3` seconds by README | cycle duration |
| `active` | boolean; default `true` | play/fade state |
| `borderRadius` | number or auto-detected | radius alignment |
| `brightness` | preset-dependent | glow brightness |
| `saturation` | default around `1.2` | glow saturation |
| `hueRange` | default `30` degrees | hue-shift range |
| `staticColors` | default `false` | disable hue cycling |
| `onActivate`, `onDeactivate` | callbacks | fade completion |

Standard `HTMLDivElement` attributes are forwarded to the wrapper.

## Rendering Model

- Wrapper `div`: positioning and stacking context.
- `::after`: masked beam stroke/perimeter.
- `::before`: inner glow.
- `[data-beam-bloom]`: outer bloom layer.
- Rotate/line: CSS custom properties and keyframes.
- Pulse: one shared frame-capped requestAnimationFrame driver, approximately 30 fps.
- Pulse instances pause when inactive, offscreen, or reduced motion is requested.
- Decorative layers use `pointer-events: none`.

## Important Limits

- React 18+ is a peer requirement.
- README lists modern `@property` support; unsupported browsers degrade rather than fully fail.
- `pulse-outside` needs an opaque child, visible overflow, and an existing idle hairline.
- Pulse reduced-motion behavior is built in. The upstream README says rotate reduced motion remains the consumer's responsibility.
- Auto radius detection reads the first child. Complex nested shells should pass an explicit radius.
