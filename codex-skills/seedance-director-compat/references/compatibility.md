# Compatibility and Fallback

## Availability rule

`Seedance 2.0 Compatibility` is a prompt-writing profile, not evidence that a model, account, provider, API, or workflow is available. Keep operational claims source-dated and provider-specific. If availability is unknown, produce prompts and export packets only.

## Source carries state

When an image or accepted clip is attached, do not repeat everything already visible. The source carries identity, wardrobe, product geometry, palette, composition, scene layout, and current state. Text carries the delta:

- motion and timing;
- camera behavior;
- light or environmental change;
- sound intent;
- preservation constraints;
- completed endpoint;
- exclusions for completed and future beats.

## Mode mapping

| Contract | Seedance-compatible wording | WAN fallback | LTX fallback |
| --- | --- | --- | --- |
| I2V | Reference is the first-frame hard anchor; describe only the delta. | Repeat essential identity anchors and one continuous action; explicitly preserve input composition. | Use a flowing present-tense paragraph with opening frame, action progression, relative camera, end state, and audio sidecar. |
| FLF2V | Bind first and last images as endpoints; generate only the continuous transition. | Use the installed first/last-frame workflow profile when available; otherwise split into two I2V clips around a stable midpoint. | State the opening and target frames, temporal progression, physical carrier, and ending composition. |
| T2V | Build subject, scene, action, camera, motivated light, sound, and endpoint compactly. | Use style → subject → space → action → camera → end state. | Use one coherent paragraph and avoid keyword piles. |
| Continuation | Compile from accepted footage or observed final frame only. | Start from the extracted final frame and carry open motion/camera state in text. | Use accepted source state and explicitly exclude replayed actions. |

## Sequence invariants

- Plan globally, compile locally.
- Accepted observed state overrides planned state.
- Rejected footage is never canonical.
- Completed beats do not replay.
- Reserved future beats do not leak into the current clip.
- Use one stable endpoint that can seed the next clip.
- Keep the directorial voice, screen direction, eyeline, lighting state, wardrobe, props, and audio phase continuous unless the story deliberately changes them.

## Model-family differences

Do not pretend the same sentence is optimal for every model. Keep one internal clip contract, then compile separately:

- Seedance compatibility: compact natural-language shooting brief; source-role and delta first.
- WAN: explicit subject, space, continuous action, camera, and stable end state.
- LTX: temporal prose with relative camera and an independent audio sidecar.
