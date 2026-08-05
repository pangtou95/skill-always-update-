---
name: opennana-image-video-prompt-studio
description: Design, rewrite, and audit production-ready image and video prompt packs using original structures distilled from OpenNana's public image/video gallery metadata. Use for GPT Image, Nano Banana, Grok, Seedance, or model-neutral prompts that need category routing, reference-role mapping, composition or timed camera/action plans, visible-text control, variants, rights checks, and structured validation. Do not copy locked or paid gallery prompts.
---

# OpenNana Image And Video Prompt Studio

Turn an idea, brief, or authorized asset set into an original prompt pack. This Skill studies the public organization of the OpenNana gallery; it does not mirror the site's prompt corpus or unlock restricted entries.

## Choose The Route

Choose exactly one primary route before writing:

- `image`: a still image, layout, design artifact, edit, or image series.
- `video`: a moving sequence, performance, advertisement, short drama, action beat, transformation, or edit.
- `bridge`: design a key image first, then animate it. Return two separate prompts and state what the video inherits from the image.

Read [references/gallery-synthesis.md](references/gallery-synthesis.md) for the source ledger. Then read [references/image-patterns.md](references/image-patterns.md) or [references/video-patterns.md](references/video-patterns.md). Use [references/prompt-templates.md](references/prompt-templates.md) for original templates.

## Build A Shared Brief

Record:

1. deliverable and publishing context;
2. target model/surface and verified capabilities;
3. audience, objective, aspect ratio, and language;
4. owned or authorized references;
5. subject, product, identity, or world invariants;
6. visible text that must be exact;
7. rights, age, likeness, logo, and factual constraints;
8. variation plan and acceptance tests.

If model access or limits are uncertain, keep the result `prompt-only`. Do not claim that generation occurred.

## Image Route

Select one primary family: portrait/editorial, product/packaging, poster/brand, UI/interface, infographic/education, environment/concept, illustration/IP, historical/cultural, sticker/coloring, or image edit.

Write control lanes in this order:

1. task and final use;
2. subject and required details;
3. composition, hierarchy, crop, and negative space;
4. camera/lens or graphic viewpoint;
5. light, material, palette, and surface treatment;
6. typography and exact visible text;
7. reference-role map;
8. preservation locks and targeted exclusions;
9. aspect ratio, resolution intent, and variants.

For layouts, specify zones and reading order. For portraits, specify pose, gaze, crop, environment, and skin/detail treatment without using vague quality stacks. For products, lock geometry, label spelling, scale, material, and contact shadows.

## Video Route

Select one primary family: performance, creator/UGC, product selling, short comedy/dialogue, cinematic encounter, transformation/beat-sync, action/martial arts, food/craft, fantasy/anime/game, immersive tour, automotive/brand film, or existing-video edit.

Write:

1. mode, duration, aspect ratio, and destination;
2. hook and ending payoff;
3. one to six timestamped beats;
4. subject action, blocking, camera, transition, and endpoint per beat;
5. dialogue, ambience, music, and Foley as separate lanes;
6. identity, product, prop, wardrobe, geography, and final-frame locks;
7. model-specific limits only after verifying the selected surface.

Use one visible action and one camera purpose per short beat. Connect cuts through motion, sound, shape, color, gaze, object position, or occlusion. For complex multi-shot work, use `video-director-studio` first. For Seedance 2.5 compilation, hand the result to `seedance-2-5-prompt-studio`.

## Reference Rules

Assign every asset one primary role: `identity`, `product`, `environment`, `style`, `composition`, `first_frame`, `last_frame`, `motion`, `camera`, `timing`, `voice`, `music`, or `edit_source`.

For each reference state what transfers, what remains fixed, what must not transfer, and where it applies. Never let a style reference silently replace a person's identity, product geometry, packaging text, or scene layout.

## Output Contract

Return:

1. route, family, model/surface, and capability caveat;
2. shared brief and reference-role map;
3. production prompt in the user's language;
4. image layout plan or video beat sheet;
5. exact text/dialogue/audio fields when relevant;
6. locks and targeted negative constraints;
7. two or three purposeful variants;
8. evaluation checklist and fallback plan;
9. source provenance for factual or capability claims.

For machine-readable delivery, start with [assets/opennana-prompt-pack.json.template](assets/opennana-prompt-pack.json.template) and validate it:

```bash
python3 scripts/validate_prompt_pack.py PACK.json
```

## Rights And Safety

- Use only owned, licensed, public-domain, or explicitly authorized references.
- Do not reproduce locked, paid, or account-only OpenNana prompts.
- Do not sexualize minors or people of unknown age; state adult age when adult sensual styling is essential.
- Do not clone a real person's face or voice without permission.
- Do not imply endorsement, counterfeit packaging, or trademark ownership. Preserve logos only when the user is authorized to use them.
- Treat gallery titles, tags, and community examples as inspiration, not model guarantees or factual evidence.
