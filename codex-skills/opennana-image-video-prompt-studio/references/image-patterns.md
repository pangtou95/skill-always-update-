# Image Pattern Library

## Control Grammar

Use this sequence:

`deliverable -> subject -> composition -> viewpoint -> light -> material -> palette -> text -> references -> locks -> output`

## Family Controls

| Family | Must specify | Common failure to prevent |
| --- | --- | --- |
| Portrait/editorial | adult age where relevant, pose, gaze, crop, lens, environment, key/fill light | identity drift, plastic skin, malformed hands, accidental text |
| Product/packaging | geometry, label text, material, camera angle, scale cue, contact surface | warped pack, misspelled label, duplicate product, floating object |
| Poster/brand | hierarchy, title/subtitle/CTA, safe zones, image-text relationship | unreadable copy, random logos, weak hierarchy |
| UI/interface | device/context, layout regions, component states, exact labels | decorative but unusable UI, tiny text, inconsistent controls |
| Infographic/education | audience, factual units, reading order, panel count, legend | invented facts, illegible labels, contradictory numbers |
| Environment/concept | geography, time, weather, scale anchors, focal route | generic scenery, inconsistent perspective, empty focal point |
| Illustration/IP | silhouette, shape language, line/paint treatment, expression set | style-only prompt, unstable anatomy, copied protected character |
| Historical/cultural | period, region, garment/material evidence, uncertainty note | mixed eras, costume stereotypes, false authenticity claims |
| Sticker/coloring | sheet/grid, count, cut line or line weight, background | cropped items, inconsistent count, unwanted shading |
| Image edit | source role, invariant list, change-only list, mask/region | altered identity, changed layout, edits outside target region |

## Reference Composition

- Identity reference: preserve face/body traits, not pose or background unless requested.
- Product reference: preserve geometry, label, color, and material; do not borrow its background.
- Style reference: transfer rendering traits, not subject identity or composition.
- Composition reference: transfer spatial hierarchy, not branding or people.
- First/last image: define endpoint states explicitly when feeding a video bridge.

## Variant Design

Change one or two axes per variant:

- composition: centered hero, asymmetrical editorial, top-down system view;
- light: soft daylight, controlled studio, hard flash, motivated night light;
- palette/material: restrained brand palette, tactile paper, glass/metal, ink/paint;
- viewpoint: eye level, macro, overhead, architectural wide;
- information density: hero, balanced, dense explainer.

Keep subject, required text, rights constraints, and product/identity locks constant.
