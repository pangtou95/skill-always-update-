# Prompt Contracts

## Stable JSON object

```json
{
  "availability": "prompt-only",
  "model_connected": false,
  "model_profile": "Seedance 2.0 Compatibility",
  "mode": "i2v",
  "reference_roles": [
    {"tag": "@Image1", "role": "first_frame", "preserve": ["identity", "wardrobe", "composition"], "exclude": ["unseen motion"]}
  ],
  "clip_contract": {
    "opening_state": "",
    "visible_beat": "",
    "camera": "",
    "motivated_light": "",
    "end_state": "",
    "completed_beats": [],
    "reserved_beats": []
  },
  "continuity_anchors": [],
  "positive_prompt": "",
  "negative_prompt": "",
  "audio_prompt": "",
  "audio_negative": "",
  "fallbacks": {
    "wan": "",
    "ltx": ""
  },
  "source_refs": [
    {"url": "https://github.com/Emily2040/seedance-2.0", "license": "MIT", "role": "method reference"}
  ]
}
```

## I2V template

```text
@Image1 is the first-frame hard anchor for identity, wardrobe, props, composition, scene layout, and key-light direction. Add only [one action] from the visible starting pose, with [physical consequence]. Camera: [one move, speed, subject relationship, endpoint]. Light: [motivated change only]. Stop when [stable end state]. Sound: [ambience, synced Foley, dialogue or silence, music cue]. Preserve [fragile anchors]; no hidden cut, redesign, new subject, replayed beat, or future action.
```

## FLF2V template

```text
@Image1 is the first frame. @Image2 is the final visual target. Preserve [identity/carrier/layout]. Generate only the continuous transition from [state A] to [state B]. Motion: [one physical path]. Camera: [locked or one controlled move]. Light: [source and continuity]. Sound: [layers]. End exactly at [state B]; no jump cut, identity change, object redesign, or extra event.
```

## Audio sidecar

```text
[duration] seconds. Ambience: [stable bed]. Foley: [cue synchronized to the visible beat]. Dialogue/voice: [short line or none]. Music: [low-intensity role and endpoint]. Adult audio placeholder when present: 【成人声音细节_A01｜内容：____｜音量/节奏：____】.
```

## Negative prompt priorities

1. identity, wardrobe, product, prop, and scene drift;
2. hidden cuts, action loops, conflicting camera moves, and future-beat leakage;
3. hands, faces, text, logos, and geometry failures relevant to the shot;
4. flicker, jitter, unreadable text, watermark, clipping, desync, and abrupt ambience changes.
