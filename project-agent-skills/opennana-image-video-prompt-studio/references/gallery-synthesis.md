# Gallery Synthesis And Source Ledger

## Scope

Sources inspected on 2026-08-05:

- Image gallery: <https://opennana.com/awesome-prompt-gallery?media_type=image>
- Video gallery: <https://opennana.com/awesome-prompt-gallery?media_type=video>
- Public list API used by the page: `https://api.opennana.com/api/prompts`

The server-rendered image page displayed 14,110 entries, while the public list API returned 15,962 at inspection time. The video page and API both returned 613. Counts are dynamic and may differ because of review state, caching, visibility, or filter behavior. Never present them as permanent inventory totals.

## Public Structure

The gallery exposes these reusable metadata concepts:

- title and slug;
- `image` or `video` media type;
- free or paid access state;
- model filter;
- tags and search terms;
- source attribution;
- one or more language-specific prompt blocks;
- images or video previews;
- notes/description and related recommendations.

Visible image filters named Nano Banana Pro, Nano Banana 2, ChatGPT, and Grok. The visible video filter named Seedance 2.0. These labels describe the gallery, not guaranteed capabilities on every provider surface.

## Observed Families

Public image titles and tags support these broad families: portrait/editorial, fashion/street photography, product and packaging, posters and branding, UI/interface, infographic/education, environment/concept, illustration and character/IP, historical/cultural visuals, stickers, coloring pages, food, architecture, interiors, and image edits.

Public video titles support: dance/performance, livestream and product selling, action/bullet-time/martial arts, comedy dialogue and reversal, romantic/cinematic encounters, beat-synced transformations, cooking and food demonstration, anime/game action, fantasy immersion, automotive advertising, creator/UGC, and local-shop promotion.

These are editorial inferences from public metadata, not an official OpenNana taxonomy.

## Extraction Boundary

- Keep only structural observations, short titles/tags needed for classification, and aggregate metadata.
- Do not bulk-store public prompt text, previews, or creator assets.
- Do not automate login, points spending, copying, or paid-prompt unlocking.
- Cite the original gallery when a user asks where an observed pattern came from.
- Rebuild every output from the user's brief and authorized assets.
