# Liblib / LibTV Public Skill Synthesis

## Scope

- Source: https://www.liblib.tv/skill
- Inspected: 2026-07-14 (Asia/Tokyo)
- Public catalog count returned by the site: 103
- Public categories: professional film, commercial advertising, animation/games, creator media, short/comic drama, general utilities, and music video
- Material inspected: public catalog metadata such as title, category, description, intended use, expected input/output, publication time, and template identifier
- Material not copied: hidden Skill bodies, creator files, prompts unavailable in the public detail view, example media, credentials, or paid execution data

The catalog used an undocumented public web endpoint at inspection time. `scripts/liblib_catalog.py` can refresh metadata, but the endpoint is not a promised public API and may change.

## Catalog Distribution

| Category | Count |
| --- | ---: |
| Professional film | 29 |
| Commercial advertising | 19 |
| Animation and games | 16 |
| Creator media | 14 |
| Short/comic drama | 12 |
| General utilities | 10 |
| Music video | 3 |
| **Total** | **103** |

Only one item exposed its Markdown body in the unauthenticated catalog response observed during inspection. Therefore this package is a metadata-level synthesis, not a redistribution of the original Skills.

## Main Finding

The 103 entries are not 103 unrelated directing systems. They repeatedly combine a smaller set of reusable dimensions:

1. format and business goal;
2. narrative engine and hook;
3. composition and blocking;
4. lens and camera grammar;
5. performance and motion physics;
6. light, palette, material, and period treatment;
7. edit rhythm and transition logic;
8. sound, voice, music, and silence;
9. asset registration and continuity;
10. deliverables, model compilation, and quality control.

This Skill normalizes those dimensions so a user can combine, for example, a restrained observational grammar with a skincare TVC blueprint and product-lock module, without installing dozens of overlapping prompts.

## Recurrent Production Families

### Narrative aesthetics

The catalog repeatedly uses domestic observation, formal symmetry, fragmented neon romance, youthful backlight, social distance, urban blocking, western standoff tension, absurdist auteur imagery, silent physical comedy, documentary observation, old-city memory, golden-age opulence, monumental brutalism, and cool-blue naturalism.

These were converted into trait-based grammar IDs in `director-grammar-library.md`. Named directors or studios are treated as discovery labels only; final instructions use observable craft traits.

### Commercial systems

Repeated commercial patterns include story-led TVC, luxury restraint, minimal technology, hyperkinetic automotive/product reels, skincare material studies, fashion/accessory performance, culturally rooted premium design, spokesperson campaigns, UGC reviews, try-on videos, and product tutorials.

The reusable value is the pipeline: claim check -> audience tension -> product truth -> visual concept -> asset lock -> storyboard -> shot prompts -> edit/audio -> CTA/QC.

### Series and short drama

The catalog includes romance, revenge/power fantasy, gothic fantasy, supernatural overseas drama, live-action-to-animation conversion, script decomposition, multi-episode writing, and character/world consistency.

These become genre-neutral modules for hook density, episode boundary, payoff, character bible, world bible, continuity state, and next-episode handoff.

### Animation and graphic motion

Repeated craft systems include cel animation, paper cutout, felt miniatures, woodblock-print movement, low-poly retro 3D, retro space illustration, glossy Y2K materials, miniature tilt-shift, toy animation, dark fairy-tale dolls, and translucent glass/crystal studies.

Each grammar defines material rules, motion limits, lighting behavior, transition logic, and failure modes instead of relying on a style name alone.

### Production utilities

The strongest cross-format ideas are casting, role/world locking, script decomposition, shot scheduling, action previs, micro-expression control, B-roll coverage, aspect-ratio reframing, style extraction, multi-panel timing boards, video diagnosis, and finish/QC.

These are implemented as optional modules in `production-modules.md`.

## Safe Reuse Rule

- Use catalog entries as research signals, not as text to reproduce.
- Preserve public source attribution and inspection date.
- Do not claim endorsement by Liblib, LibTV, listed creators, directors, studios, or brands.
- Do not download or redistribute example media without permission.
- Convert named style requests into craft traits and user-owned story choices.
- Refresh counts before making time-sensitive claims.

Generate a current metadata inventory:

```bash
python3 scripts/liblib_catalog.py --format markdown --output /tmp/liblib-skill-catalog.md
```
