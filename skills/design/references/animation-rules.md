# Animation rules

The short list agents break most often. `emil-design-eng.md` has the reasoning.

- Decide first whether it should animate. Anything used 100+ times a day, and anything triggered by keyboard, gets no animation.
- Enter and exit use ease-out, never ease-in. Use custom curves, not CSS keywords: `cubic-bezier(0.23, 1, 0.32, 1)` for interactions, `cubic-bezier(0.77, 0, 0.175, 1)` for on-screen movement, `cubic-bezier(0.32, 0.72, 0, 1)` for drawers.
- Keep UI motion under 300ms, press feedback at 100 to 160ms, and exits faster than entrances.
- Animate `transform` and `opacity` only. Never `transition: all`.
- Pressable elements get `scale(0.97)` on `:active`. Nothing starts from `scale(0)`; start at 0.9 to 0.95 with opacity 0.
- Popovers scale from their trigger. Modals stay centered.
- Use CSS transitions, not keyframes, for anything that can retrigger quickly. Keyframes restart from zero.
- Gate hover effects behind `@media (hover: hover) and (pointer: fine)`.
- Honor `prefers-reduced-motion`: drop movement, keep opacity and color changes.
- Stagger entrances by 30 to 80ms per item.
- Report UI code review findings as one table with Before, After, and Why columns.
