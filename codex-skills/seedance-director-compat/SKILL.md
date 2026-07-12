---
name: seedance-director-compat
description: Create, normalize, or review bilingual Chinese-English director-led video prompt packs using Seedance 2.0-compatible principles even when Seedance is unavailable. Use for first-frame I2V, first/last-frame transitions, multimodal reference roles, physically stable dialogue/action/product/VFX/environment/multi-character scenes, connected clips, separate video/audio positive and negative prompts, or WAN/LTX fallback compilation without claiming that a Seedance model or API is connected.
---

# Seedance Director Compatibility

Turn a scene into a compact production object and model-ready prompt while keeping the workflow useful without Seedance access. Treat Seedance as an optional target profile, never as an assumed runtime.

## Workflow

1. Resolve availability.
   - If an active Seedance surface is verified, label the exact surface and date-sensitive assumptions.
   - Otherwise set `model_profile` to `Seedance 2.0 Compatibility`, `availability` to `prompt-only`, and `model_connected` to `false`.
   - Never invent endpoint names, model IDs, prices, limits, regions, or audio capabilities.
2. Classify scope.
   - Use `standalone_clip` for one reliable visible beat.
   - Use `sequence_project` for connected clips, long stories, continuations, dense dialogue, or several narrative turns. Plan the whole arc but compile only the next unresolved clip.
3. Choose the input mode before writing prose: `t2v`, `i2v`, `v2v`, `r2v`, or `flf2v`.
4. Assign every reference one primary role: identity, first frame, last frame, environment, motion, camera, timing, audio, or style. State what must not transfer.
5. Classify the scene and load its physical contract from [references/scenario-physics.md](references/scenario-physics.md): dialogue, subtle performance, action, product, VFX/transformation, environment/weather, multi-character interaction, transition, or general narrative.
6. Name one internal directorial intention. Translate it into visible blocking, one camera choice, motivated light, performance, and sound; do not ship an abstract emotion label as the final prompt.
7. Build one clip contract:
   - actual opening state;
   - one visible action and physical consequence;
   - one primary camera move with endpoint;
   - one stable end state;
   - continuity locks and reserved future beats;
   - audio layers and negative constraints.
8. Compile the current clip only. For I2V, let the source carry static state and let text carry only motion, camera, timing, light change, sound, endpoint, and preservation constraints.
9. Compile Chinese and English independently from the same contract. Do not merely place untranslated Chinese variables inside an English wrapper. Emit separate bilingual visual positive, visual negative, audio positive, and audio negative prompts. Preserve numbered adult placeholders exactly in both languages and never fill them.
10. If Seedance is unavailable, compile the same clip contract for WAN or LTX using the fallback table in [references/compatibility.md](references/compatibility.md). Default LTX to English and WAN/Seedance compatibility to Chinese while always returning both languages.
11. Validate structured output with `python3 scripts/validate_prompt_pack.py PACK.json`.

## Prompt Discipline

- Prefer one visible beat over several events.
- Prefer one motivated camera move over a stack of moves.
- Write physical causes and visible consequences instead of generic mood words.
- Give VFX a source, material behavior, light interaction, object interaction, dissipation, and endpoint.
- Keep fragile faces, hands, logos, text, and product geometry stable by simplifying nearby motion.
- Treat accepted footage or its observed final frame as canonical for continuation; planned state never overrides observed state.
- Keep reference tags literal and role-bound when a target surface uses them.
- Remove generic quality boosters, repeated static description, secondary actions, and future story summary before removing continuity locks or endpoints.

## Safety and Rights

- Use only owned, licensed, public-domain, stock, mocap, rehearsal, or clearly authorized references.
- Transfer general motion, tempo, framing, or camera behavior from real-person references; do not transfer likeness or voice without authorization.
- Generate mature non-explicit material normally.
- Replace clearly adult, consensual but overly explicit details with linked visual/audio placeholders and leave them blank.
- Block sexualized minors or unknown-age characters, non-consensual sexual content, incest, and bestiality instead of using placeholders to bypass the block.

## Output

Return the production object before the final prompt:

1. availability and model profile;
2. mode and reference-role map;
3. clip contract and continuity anchors;
4. Chinese and English shot scripts;
5. Chinese and English visual positive/negative prompts;
6. Chinese and English audio positive/negative prompts;
7. scene type, physical contracts, translation status, and model-preferred language;
8. WAN/LTX fallback when requested or when Seedance is unavailable;
9. source references and compatibility caveats.

Use the stable JSON contract and templates in [references/prompt-contracts.md](references/prompt-contracts.md). Read [references/upstream-attribution.md](references/upstream-attribution.md) when redistributing or extending this skill.
