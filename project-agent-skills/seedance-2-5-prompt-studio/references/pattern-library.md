# Seedance 2.5 Pattern Library

## Audit scope

The public EvoLink gallery was inspected on 2026-08-05. The Japanese page exposed 122 cards: 24 labeled as official showcases and 98 linked to community posts on X. The community cards are workflow examples, not verified Seedance 2.5 API outputs.

### Category distribution

| Category | Cards |
| --- | ---: |
| Cinematic film | 29 |
| Native audio and dialogue | 21 |
| 30-second one-take | 17 |
| Animation | 11 |
| VFX | 10 |
| Video editing | 9 |
| Sci-fi and worldbuilding | 7 |
| Brand film | 5 |
| Multilingual | 5 |
| Product ad | 4 |
| Motion graphics | 3 |
| Tutorial | 1 |

Sixty-two cards used a 30-second label. The collection contained 38 expert, 43 advanced, 26 intermediate, and 15 beginner cards. These labels describe the gallery, not a formal model benchmark.

## Reusable structural patterns

### 1. Timestamped acts

Long prompts work as a beat sheet: setup, development, turn, resolution. Each interval receives a visible action, camera relationship, sound cue, and endpoint. Use four to six beats for most 30-second pieces.

### 2. A persistent visual carrier

A stable object, character, gesture, shape, or motion vector links changing worlds. Lock its position, scale, orientation, focus, or material rules while the environment changes. This is useful for brand films, historical explainers, and match-cut montages.

### 3. Transition causality

Do not request a vague seamless transition. State the carrier and physical change: fabric fills frame and becomes cloud; a circular window becomes an eye; reflected light becomes a new location; particles inherit the outgoing text's motion.

### 4. One-take route maps

A one-take needs spatial geography. Define start, route, thresholds, occlusions, camera-to-subject distance, axis, speed changes, and final reveal. Every bridge must be motivated by something visible in the scene.

### 5. Fixed-anchor match cuts

Keep one anchor fixed while the background, era, material, or supporting action switches on music accents. Specify what remains sharp and what carries motion blur. End with a distinct release or hero frame.

### 6. Reference-role isolation

Assign one primary role per asset. Identity references should not dictate camera; camera references should not replace wardrobe; style references should not alter product geometry. State active beats and non-transfer rules.

### 7. Cast and grid isolation

For many characters or numbered grids, map every cell to one character, costume, prop, or beat. State that supporting characters remain distinct and visually subordinate when appropriate. Explicitly exclude duplicates, face mixing, and role swaps.

### 8. Clay/previsualization contracts

Use a clay render or previs for camera, blocking, pose, depth, trajectory, and edit points. Use separate images for identity, materials, light, and style. Never take the clay render's gray material as the final color.

### 9. Material and physics verbs

Name material behavior, not only appearance: refracts, beads, stretches, flakes, scatters, condenses, folds, ripples, drags, collides, settles. Add light interaction, object contact, inertia, and the stable end state.

### 10. Audio as a cue sheet

Split dialogue, voice identity, music, ambience, and Foley. Bind every line to a speaker and language. State whether music is absent, continuous, ducked, or hit-synced. Name unwanted subtitles, voice swaps, and generic background music as exclusions when relevant.

### 11. Surgical edits

For edits, begin with an invariant list and then a small change list scoped to timestamps. Example structure: preserve character/action/style; change only camera from 4-7 seconds; keep preceding and following continuity unchanged.

### 12. Performance realism

Replace “natural acting” with observable micro-actions: breath, blink, weight shift, gaze target, hand-object contact, pauses, interrupted movement, fabric lag, and reaction timing. Choose either polished cinema or imperfect vlog grammar and exclude the opposite.

### 13. Typography as verified production

Specify exact text, script direction, entry/exit motion, font class, material, duration, and background contrast. For multilingual work, isolate each language by beat and require human review of every rendered string.

### 14. Product proof before spectacle

Lock silhouette, logo placement, material, dimensions, and moving parts. Show one feature through a visible cause and result. Use spectacle around the product without allowing particles, hands, or camera effects to deform it.

### 15. Controlled exclusions

Derive negatives from the format's actual failure risks. A one-person scene excludes extra people and reflections; a product shot excludes geometry drift; an edit excludes changes outside the target interval; a dialogue scene excludes speaker/language swaps and unwanted subtitles.

## Anti-patterns

- copying a long example without replacing its structural assumptions;
- assigning several primary roles to one reference;
- describing 30 seconds as one static mood;
- stacking incompatible camera moves;
- requesting “cinematic” without blocking, light, lens, or sound evidence;
- mixing official showcase claims with unverified community workflows;
- treating a provider's published schema as proof that its route is live;
- overloading the negative prompt with unrelated quality words.
