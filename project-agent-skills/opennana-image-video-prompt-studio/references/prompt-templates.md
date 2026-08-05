# Original Prompt Templates

These templates are original synthesis, not copied OpenNana prompts.

## Image

```text
Create a [deliverable] for [audience/use].
Subject: [subject, action, required attributes].
Composition: [aspect ratio, crop, hierarchy, focal point, negative space, layout zones].
View and light: [camera/viewpoint/lens], [key light, fill, time/weather].
Style and material: [rendering language], [surfaces], [palette].
Visible text: render exactly "[text]" in [location/hierarchy]; no other text.
References: [asset -> role, transfer, preserve, exclude].
Locks: preserve [identity/product/layout facts].
Avoid: [targeted likely failures].
Output: [format/resolution intent] plus [variant axis].
```

## Video

```text
Create a [duration]-second [aspect ratio] [format family] for [destination].
Hook: [first visible event]. Payoff: [final stable state].
[00:00-00:04] [purpose]; subject [action/blocking]; camera [movement/lens]; audio [cue]; end on [endpoint].
[00:04-00:09] ...
Dialogue: [speaker, language, exact line, time window, delivery].
References: [asset -> one primary role, transfer, preserve, exclude, active beats].
Global locks: [identity/product/wardrobe/prop/geography/final frame].
Avoid: [targeted likely failures].
```

## Image-To-Video Bridge

1. Generate a key image with a stable subject, product, environment, and endpoint-ready composition.
2. Assign the image `first_frame`, `identity`, `product`, or `environment`; do not assign every role at once.
3. In the video prompt, describe only motion, camera, sound, and changes over time, then restate invariants.
4. If the desired final state differs, provide a separately authorized last-frame reference and explain the transition.
