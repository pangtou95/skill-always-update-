---
name: video-director-studio
description: Direct, plan, and compile AI-generated videos across Seedance, Runway, WAN, LTX, Pixelle-Video, LibTV, and editing workflows. Use when the user wants a director treatment, cinematic style, TVC, short drama, animation, MV, documentary, travel film, UGC, storyboard, shot list, continuity plan, per-shot prompts, sound design, or a complete video-generation production pack. Distills recurring production patterns from Liblib/LibTV's public 2026 Skill catalog without copying private or hidden creator instructions.
---

# Video Director Studio

Turn a rough idea, script, product, reference image, or existing clip into a model-agnostic director pack, then compile it for the generator that is actually available.

This skill synthesizes public metadata patterns from [Liblib/LibTV's Skill catalog](https://www.liblib.tv/skill). It does not contain the creators' hidden Skill bodies, assets, credentials, model access, or paid generations. Read [references/liblib-synthesis.md](references/liblib-synthesis.md) for scope and provenance.

## Core Workflow

1. Resolve the brief.
   - Capture objective, audience, platform, aspect ratio, duration, language, required product/story facts, supplied assets, rights status, and delivery target.
   - Separate facts from creative choices. Do not invent product claims, endorsements, locations, likeness rights, or model availability.
2. Choose one format blueprint from [references/format-blueprints.md](references/format-blueprints.md).
3. Choose one primary director grammar and at most one accent grammar from [references/director-grammar-library.md](references/director-grammar-library.md).
   - Translate named influences into observable traits: composition, blocking, lens, camera, light, palette, performance, edit rhythm, material behavior, and sound.
   - Never promise an exact replica of a creator, film, brand campaign, or proprietary look.
4. Attach only the production modules needed for the risk and format. Use [references/production-modules.md](references/production-modules.md).
5. Build the internal director pack before writing model prompts:
   - brief and constraints;
   - format and director profile;
   - creative premise and audience hook;
   - asset, character, world, product, and continuity registers;
   - beat sheet and shot list;
   - camera, performance, light, edit, and sound plans;
   - per-shot prompt contracts and negative constraints;
   - model adapter and quality-control report.
6. Compile only after the pack is coherent. Read [references/model-adapters.md](references/model-adapters.md) and use the matching installed Skill for current provider details.
7. Validate structured packs with:

```bash
python3 scripts/director_pack_audit.py path/to/director-pack.json
```

8. Generate or edit only when a real tool/provider is available and authorized. Otherwise return a prompt-ready production pack and mark execution as `prompt-only`.

## Directing Rules

- Use one visible dramatic beat per generated clip.
- Use one primary camera move per shot; secondary motion may refine, not compete.
- Give every shot an actual opening state, motivated action, visible consequence, and stable end state.
- Let accepted source media carry identity, wardrobe, product geometry, composition, and current state. Text should carry the intended change.
- Preserve screen direction, eyelines, geography, wardrobe, props, lighting phase, product labels, and audio phase across connected clips.
- Build expensive or long pieces through a cheap proof sequence first: look frame, five-second motion test, one continuity transition, then full shot generation.
- Treat audio as a separate plan: ambience, Foley, dialogue/voice, music function, silence, and transition cues.
- Design coverage for editing. Include establishing, action, reaction, detail/product, transition, and safety shots only when they have a clear edit function.
- For UGC, tutorials, and product reviews, prioritize believable behavior, legible demonstration, claim accuracy, and natural pauses over cinematic decoration.
- For products, lock geometry, logo, label, color, material, scale, contact, reflections, and support surfaces.
- For action and VFX, specify preparation, weight, trajectory, contact, reaction, decay, residue, and endpoint.

## Progressive Output

Match depth to the request:

- `concept`: premise, format, grammar, and three creative directions.
- `treatment`: selected direction, visual language, beat sheet, sound, and asset plan.
- `shot-pack`: complete shot list, continuity, prompts, negatives, and edit plan.
- `generation-pack`: shot-pack plus provider-specific compilation and execution manifest.
- `diagnostic`: analyze an existing video for hook, rhythm, coverage, continuity, model failures, and repair prompts.

Do not force a full production package when the user only needs one shot. For connected stories, plan globally and compile the next unresolved clip locally.

## Generator Routing

| Need | Route |
| --- | --- |
| Manga / short-drama specialist direction | Load sibling `../short-drama-director/SKILL.md` for dialogue diagnosis, asset/spatial locks, dialogue/action storyboards and QC; keep the existing director pack or `drama-skills` / `shuohao-video-drama` project as owner |
| Seedance 2.5 prompt pack | `seedance-2-5-prompt-studio`, plus `seedance-director-compat` for bilingual physics/fallback contracts |
| Seedance 2.0 multimodal prompt | `seedance-director-compat`, `seedance-prompt-zh`, or `seedance-prompt-en` |
| Runway generation/API | `rw-check-compatibility`, then `rw-generate-video` or `use-runway-api` |
| WAN or LTX local fallback | `seedance-director-compat` compatibility compiler |
| Automated multi-scene short video | `pixelle-video-workflows` |
| LibTV platform execution | Use LibTV's own Skill/CLI after account, cost, and model availability are confirmed |
| Editable assembly/captions/export | `chatcut-plugin-basics`, relevant `chatcut-*` Skills, then verification |
| Local editable Jianying draft / native export readiness | `jianying-headless-guide` for a source-linked dependency check and isolated-draft handoff; the upstream core and matching Jianying installation are separate requirements |
| Narration-led movie recap | `narrator-ai-cli-skill` |

The director pack is the source of truth. Provider prompts are disposable compilations from that pack.

For manga integration, reuse approved beats, exact dialogue, asset/scene/shot IDs,
and continuity states. Load only the relevant specialist modules and merge their
results into the existing pack. Commercial action presets do not override
intentional 2D side views, quiet scenes, long takes, or the verified model limits.
If the optional sibling Skill is absent, continue with this director workflow
and report that the specialist module was not used.

## Required Final Checks

- The first three seconds have a specific narrative, visual, or informational function.
- Every shot earns its duration and has an edit purpose.
- The primary subject remains identifiable and spatially coherent.
- Dialogue ownership and lip movement are unambiguous.
- Claims, names, captions, logos, and required text are verified or deferred to editing.
- The final shot resolves the beat and provides a usable transition or CTA.
- The selected model can accept the referenced media and requested mode; unknown limits stay labeled unknown.
- Rights and consent are recorded for supplied likeness, voice, music, brand, and reference footage.

Start structured work from [assets/director-pack.json.template](assets/director-pack.json.template).
