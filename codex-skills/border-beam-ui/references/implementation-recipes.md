# Implementation Recipes

## React Button With Reduced Motion

```tsx
import { useEffect, useState } from 'react';
import { BorderBeam } from 'border-beam';

function useReducedMotion() {
  const [reduced, setReduced] = useState(false);
  useEffect(() => {
    const query = matchMedia('(prefers-reduced-motion: reduce)');
    const update = () => setReduced(query.matches);
    update();
    query.addEventListener('change', update);
    return () => query.removeEventListener('change', update);
  }, []);
  return reduced;
}

export function BeamButton() {
  const reduced = useReducedMotion();
  const [focused, setFocused] = useState(false);
  return (
    <BorderBeam className="beamButtonWrap" size="sm" colorVariant="mono" theme="auto" active={!reduced && focused} strength={0.68}>
      <button onFocus={() => setFocused(true)} onBlur={() => setFocused(false)}>
        Create project
      </button>
    </BorderBeam>
  );
}
```

The production button still needs its own `:focus-visible` outline, hover, pressed, disabled, loading, error, and success styles.

```css
.beamButtonWrap { display: inline-flex; width: fit-content; }
```

The upstream wrapper is a `div`, so explicitly preserve inline sizing for buttons and icon controls. In grids or full-width forms, use the layout behavior the parent contract expects.

## Vanilla CSS Fallback

This is a local fallback pattern, not copied upstream code. It uses a pseudo-element, conic gradient, and mask to reveal only the edge.

```css
.beam-shell {
  --beam-radius: 8px;
  --beam-width: 1px;
  --beam-duration: 3s;
  position: relative;
  border-radius: var(--beam-radius);
  isolation: isolate;
}

.beam-shell::before {
  content: "";
  position: absolute;
  inset: 0;
  padding: var(--beam-width);
  border-radius: inherit;
  pointer-events: none;
  background: conic-gradient(from var(--beam-angle), transparent 0 72%, var(--color-accent) 82%, transparent 92%);
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  mask-composite: exclude;
  animation: beam-rotate var(--beam-duration) linear infinite;
}

@property --beam-angle {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: false;
}

@keyframes beam-rotate { to { --beam-angle: 360deg; } }

@media (prefers-reduced-motion: reduce) {
  .beam-shell::before { animation: none; --beam-angle: 30deg; }
}
```

Use a stable base border on the child. Add `opacity: 0` by default and activate the pseudo-element through a deliberate state class when permanent motion is unnecessary.

## Overflow Check For Outer Bloom

Inspect every ancestor between the target and intended bloom boundary. `overflow: hidden`, `clip`, transforms, filters, and new stacking contexts can crop or reorder the halo. Prefer `pulse-inner` when layout ownership makes safe overflow uncertain.
