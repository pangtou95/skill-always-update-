# Original Prompt Templates

Replace every bracketed field. These are structural templates, not copied gallery prompts.

## 30-second narrative

```text
Deliverable: 30 seconds, [ratio], [mode], [language], [audio mode].
Global locks: [identity/product/wardrobe/world rules].
Reference roles: [tag -> one role -> preserve -> exclude -> active beats].

[0-5s] Setup: [subject action]. Camera: [one instruction]. Audio: [cue]. End on [state].
[5-11s] Development: [action and consequence]. Transition carrier: [object/gesture/sound/shape].
[11-18s] Turn: [new pressure or reveal]. Camera: [instruction and endpoint]. Audio: [cue].
[18-25s] Climax: [single main action]. Preserve [fragile locks].
[25-30s] Resolution: [stable final state and final frame].

Visible text: [exact string, timing, placement, verification requirement] or none.
Exclude: [format-specific failures only].
```

## One-take route

```text
One continuous take with no hidden cuts. Start at [location/composition].
Route: [threshold 1] -> [space 2] -> [threshold 2] -> [final reveal].
Camera-to-subject relationship: [distance/side/axis].
Bridges: [foreground occlusion], [doorway/tunnel/reflection], each caused by visible movement.
Speed changes: [timestamps and motivation].
End at [wide/close hero state], camera fully settled.
No teleportation, axis reversal, unmotivated orbit, repeated room, duplicated subject, or morphing architecture.
```

## Reference-heavy R2V

```text
@Image 1: identity only; preserve [features]; do not transfer [background/pose].
@Image 2: wardrobe only; preserve [construction/color]; do not transfer [person].
@Image 3: environment only; preserve [layout/light source]; do not add its people.
@Video 1: camera path and timing only; do not transfer actors, wardrobe, or set.
@Audio 1: music rhythm only; dialogue must not transfer.
@Clay Render 1: blocking, depth, trajectory, and edit points only; do not use gray materials.
[Add one line per reference.]

Timeline: [beats]. Cast isolation: [character -> allowed references -> beats].
Global exclusions: reference mixing, identity swaps, duplicate characters, grid-cell leakage.
```

## Dialogue and native audio

```text
Speaker map: A = [identity/voice/language]; B = [identity/voice/language].
[time] A performs [visible action], then says exactly: "[line]" with [delivery].
[time] B reacts [nonverbal beat], then says exactly: "[line]" with [delivery].
Music: [none/role/tempo/ducking]. Ambience: [continuous bed]. Foley: [timestamped cues].
Keep speaker identity, language, voice, and lip-sync stable. No narrator, voice swap, added line, subtitles, captions, or generic music unless requested.
```

## Timestamp edit

```text
Edit @Video 1.
Invariants for the whole clip: keep [identity, action timing, wardrobe, set, style, audio elements].
Change only [target property] from [start-end].
Before [start]: unchanged. During [interval]: [precise replacement]. After [end]: rejoin the original state continuously.
Do not alter any other character, object, camera beat, dialogue, music phase, duration, or final frame.
```

## Product film

```text
Product anchor: @Image 1 controls silhouette, dimensions, materials, color, logo placement, and moving-part geometry.
Feature proof: [user-visible function] caused by [action] and demonstrated by [result].
Camera: [macro/track/orbit] with [endpoint]. Light: [source] reveals [material property].
Effects may interact with the environment but cannot cover, stretch, duplicate, melt, or redesign the product.
Finish on a clean hero frame with [exact product orientation and negative space].
```
