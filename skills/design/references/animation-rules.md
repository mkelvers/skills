# Animation rules

The rules agents break most often. [emil-design-eng.md](emil-design-eng.md) explains the reasoning behind them, and [animate-recipes.md](animate-recipes.md) has working code for common components.

## Whether to animate

- Motion must answer something: a person's action, a change of state, or where something came from. Decoration that moves is still decoration.
- Anything used a hundred times a day, and anything triggered from the keyboard, gets no animation. Repetition turns delight into delay.
- One orchestrated moment beats scattered effects. A reveal on every section reads as generated.

## Timing and easing

- Entering and exiting elements ease out, never in. Use custom curves rather than CSS keywords: `cubic-bezier(0.23, 1, 0.32, 1)` for interactions, `cubic-bezier(0.77, 0, 0.175, 1)` for movement across the screen, `cubic-bezier(0.32, 0.72, 0, 1)` for drawers and sheets.
- Keep UI motion under 300 ms, press feedback at 100 to 160 ms, and exits faster than entrances.
- Stagger a group entrance by 30 to 80 ms per item, and cap the total.

## How it moves

- Pressable elements get `scale(0.97)` on `:active`.
- Nothing starts from `scale(0)`; start at 0.9 to 0.95 with opacity 0.
- Popovers and menus scale from their trigger. Modals stay centred.
- Use CSS transitions, not keyframes, for anything that can be retriggered quickly; keyframes restart from zero and jump.
- Gate hover effects behind `@media (hover: hover) and (pointer: fine)`, so taps on phones don't leave hover stuck.
- Honour `prefers-reduced-motion`: remove movement, keep opacity and colour changes.

## Performance

| Problem | Fix |
| --- | --- |
| Animation stutters | Animate `transform` and `opacity` only, never `width`, `height`, `top` or `left`. |
| Random properties animate | Never `transition: all`; list the exact properties. |
| Blur is slow | Keep an animated `blur()` under 20 px. |
| React re-renders every frame | Write to `ref.current.style`, not to state. |
| A library's `x`/`y` drops frames | Animate the full `transform` string instead. |
| Element shifts 1 px as motion starts | Add `will-change: transform`, only once you see the shift. |
| A long list scrolls slowly | Virtualise it, rendering only what's visible. |

## Reviewing motion

Report findings as one table with Before, After and Why columns, so each change is concrete and justified.
