# Scenario Physics Matrix

Compile each scene through one dominant physical contract. If several categories appear, choose the category that owns the visible beat and treat the others as low-intensity constraints.

| Scene | Physical contract | Camera priority | Conditional negatives | Audio priority |
| --- | --- | --- | --- | --- |
| Dialogue / lip sync | Small continuous head, breath, eyeline, and mouth motion; mouth moves only during speech. | Locked or subtle push-in. | lip-sync mismatch, wrong speaker, large head turn, gesture competition | dry dialogue, room tone, minimal Foley |
| Subtle performance | Translate emotion into breathing, eyeline, facial muscles, finger pressure, and posture. | Stable close or medium shot. | blank expression, puppet motion, looping gesture | breath, cloth movement, intentional silence |
| Action | Preparation, weight transfer, inertia, contact reaction, and deceleration into a stable finish. | One tracking or stable relative move. | broken trajectory, floating feet, full-frame shake, hidden cut | impact/contact cues, breath, surface response |
| Product / object | Rigid geometry and proportion; force/support, contact, reflections, and shadows remain synchronized. | Locked, slider, or one controlled orbit. | logo/label redraw, geometry warp, floating support, reflection mismatch | mechanism click, surface contact, restrained music |
| VFX / transformation | Visible source, travel path, material behavior, light/object interaction, dissipation, residue, and one continuity carrier. | Locked or one slow move. | noisy overlay, source detachment, carrier loss, unfinished effect | source cue, propagation cue, endpoint decay |
| Environment / weather | One wind direction, gravity, collision, and coherent surface response; world moves while camera stays stable. | Locked or stabilized tracking. | contradictory wind, global jitter, surface mismatch | stable weather bed, local impacts, distance-consistent ambience |
| Multi-character | Independent skeletons, positions, eyelines, screen direction, and limited visible contact points. | Preserve the 180-degree axis. | fused bodies, duplicate people, clothing fusion, identity swap | speaker ownership, separate Foley positions |
| First/last frame | Preserve one carrier and endpoint geometry; generate only the physical path between states. | Locked or one bridge move. | jump cut, premature final pose, endpoint miss, identity drift | transition bridge and final cue |
| General narrative | One motivated action with cause, continuous motion, visible consequence, and stable endpoint. | One motivated move. | stacked events, action loop, future-beat leakage | ambience, action evidence, endpoint cue |

## Bilingual rule

Create `script_zh` and `script_en` from this same contract. Then compile the four prompt classes in both languages:

- video positive;
- video negative;
- audio positive;
- audio negative.

English must be production English without Chinese characters except linked safety placeholders that must retain their exact IDs. When a deterministic local translation cannot preserve a story-specific detail, mark the result `lexical-baseline` or `local-template`; request a Qwen bilingual rewrite rather than labeling it complete.
