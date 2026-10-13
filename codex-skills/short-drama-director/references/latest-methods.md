# V6.9.9 Selective Integration

Reviewed 2026-10-13 at `6da07df971c85e730975785e7301cc1de9a7d3e7` in [manju-laoli-skill](https://github.com/lixiaoxiao9888-create/manju-laoli-skill). Original adaptation of selected new methods; the packaged V6.0 base and local safeguards remain in place. This is not a full upstream runtime upgrade.

## Segment Continuity

For independently generated segments, save the exact visible end state: named subject, pose, screen position, gaze, prop ownership, costume and lighting. The next segment's opening must account for that state or explicitly show an intentional transition. A supported reference image can reinforce continuity; do not assume every model accepts the same reference/frame mode. Do not fabricate a previous rendered end frame from a merely planned storyboard.

Track transition type, overlap and audio bridges separately from shot durations. Environment cutaways can communicate time/location or carry a sound bridge, but should not conceal a continuity error. Avoid padding or slowing all footage solely to fill a target duration.

## Concrete Opening Frames

Name who owns each face, hand and prop. Replace dangling pronouns and unfilmable intensity adjectives with visible action. In a troublesome close-up, reduce the opening sentence to the primary subject and its physical relations, then add secondary details. This is a debugging technique, not a universal ban on two-character compositions. Recheck the actual image for duplicate faces and missing limbs.

## Dialogue, Voiceover And Internal Monologue

Keep exact locked text and separate speaker, audible source and visible lip action. On-screen dialogue, off-screen voiceover and internal monologue are distinct. Establish silence/closed mouth when the visible actor is not speaking, and verify lip sync in the render. Voiceover should add context or perspective rather than repeatedly narrating an already obvious action. Do not impose a fixed narration percentage on a user's chosen style.

## Expressions And Production Ledger

Use FACS-inspired facial action descriptions as optional directing aids: gaze, brow, eyelid, mouth tension and timing. They describe visible behavior, not a diagnosis of real mental state. Keep combinations simple and test whether the selected model understands them. Stable character/shot IDs, parent-child visual anchors and production statuses belong in the existing project ledger rather than a parallel incompatible notebook.

## H3 Format Branch

Before converting a director pack to MiniMax H3, check the actual checkpoint, supported input mode, rewrite format and current official examples. Upstream's October revision describes English rewrite sections while retaining original-language dialogue, plus explicit off-screen/cut phrases. Verify these against the installed checkpoint before applying them. Community reports about speaker mixing are risk observations, not proof that every same-gender scene fails. Use short controlled samples and inspect audio; if uncertain, deliver a model-neutral draft or an explicitly separate post-production voice plan.

Upstream references reviewed: segment-splicing.md, vo-os-weaving.md, model-adapters.md, h3-adapter.md and the V6.9.9 entrypoint. Community capability tables and fixed creative rules are not substituted for current official documentation. No new upstream checker or HTML-board compiler is installed by this integration.
