# Production Modules

Attach modules by format and risk. Each module must create a concrete artifact; do not add a ceremonial checklist.

| ID | Module | Required artifact |
| --- | --- | --- |
| `M-BRIEF` | Brief resolution | objective, audience, platform, duration, aspect, language, facts, unknowns, approval owner |
| `M-RIGHTS` | Rights and consent | source, owner/license, permitted use, likeness/voice/music/brand status, unresolved restrictions |
| `M-SCRIPT` | Script and beat design | logline, audience promise, beat sheet, dialogue/VO, payoff, duration estimate |
| `M-CAST` | Casting | role need, age band, performance traits, visual contrast, consent, selected asset ID |
| `M-CHARACTER` | Character bible | identity anchors, wardrobe, silhouette, voice, behavior, relationships, prohibited drift |
| `M-WORLD` | World bible | locations, period, rules, geography, props, recurring motifs, continuity state |
| `M-LOOK` | Look bible | grammar IDs, palette, contrast, source lights, lens policy, texture/material rules, typography |
| `M-PRODUCT` | Product/claim lock | geometry, logo/label, colors/materials, scale, required views, approved claims, forbidden claims |
| `M-STORYBOARD` | Storyboard | frame purpose, composition, blocking, camera, action, endpoint, continuity handoff |
| `M-PREVIS` | Action/VFX previs | preparation, trajectory, weight/contact, effect source, interaction, decay, safety, end pose |
| `M-PERFORMANCE` | Performance calibration | objective, eyeline, breath, posture, gesture, micro-expression timeline, dialogue ownership |
| `M-SCHEDULER` | Shot scheduler | shot IDs, duration, dependencies, generation order, expected cost tier, retry priority |
| `M-COVERAGE` | Edit coverage | establish/action/reaction/detail/transition/safety function and editorial dependency |
| `M-AUDIO` | Sound plan | ambience, Foley, dialogue/voice, music role, silence, transitions, mix priority, rights |
| `M-CONTINUITY` | Continuity state | accepted frame/clip, identity, positions, eyelines, screen direction, props, light/audio phase, open motion |
| `M-EDIT` | Edit plan | timeline order, cut motivation, rhythm, transitions, captions, CTA, finishing, deliverables |
| `M-LOCALIZE` | Platform/language localization | copy, VO, captions, cultural checks, disclosure, aspect-safe layout, alternate CTA |
| `M-QC` | Generation and finish QC | factual, visual, temporal, audio, continuity, rights, platform, and delivery verdicts |

## Module Presets

### Lean single shot

`M-BRIEF`, `M-RIGHTS`, `M-LOOK`, `M-STORYBOARD`, `M-AUDIO`, `M-QC`.

### Product or brand video

Add `M-PRODUCT`, `M-SCHEDULER`, `M-COVERAGE`, `M-EDIT`, and `M-LOCALIZE`. Use `M-CAST`/`M-PERFORMANCE` when a person appears.

### Narrative or short drama

Add `M-SCRIPT`, `M-CAST`, `M-CHARACTER`, `M-WORLD`, `M-CONTINUITY`, and `M-EDIT`. For a series, persist state after every accepted clip.

### Action, game, or VFX

Add `M-PREVIS`, `M-SCHEDULER`, `M-CONTINUITY`, and effect-specific QC. Generate a low-cost motion proof before the hero render.

### Documentary or real-person content

Require `M-RIGHTS`; add evidence/source notes, interview consent, disclosure, and an explicit boundary between observed and reconstructed material.

## Shot Contract

Every generated shot should contain:

```text
shot_id
editorial_function
duration_sec
opening_state
visible_beat
physical_consequence
camera: framing + lens intent + one primary move + endpoint
performance
motivated_light
sound
end_state
continuity_in / continuity_out
positive_prompt
negative_constraints
fallback_or_repair
```

## Generation Order

1. Lock the highest-risk static asset: face/character, product, key environment, or style frame.
2. Test the most fragile motion: hands/product contact, dialogue, transformation, action, or camera transition.
3. Generate continuity bridge shots before decorative coverage.
4. Accept or reject clips and update observed continuity.
5. Generate coverage against real edit gaps.
6. Add captions, exact text, logos, and many UI elements in editing unless the selected model is verified to render them reliably.

## QC Severity

- `critical`: rights problem, false claim, identity/product failure, missing story payoff, unusable audio, or broken delivery.
- `major`: continuity break, wrong action, bad lip ownership, camera conflict, unreadable demonstration, or missing edit coverage.
- `minor`: small background drift, nonessential texture issue, optional sound/detail refinement.

Do not hide a critical issue behind an overall aesthetic score.
