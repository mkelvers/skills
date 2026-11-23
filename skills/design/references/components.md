# Design principles

Principles for building UI that holds up as it grows. They apply to a component library, a design system, or a single screen. Check new work against them before you add a variant, prop, or color.

## 1. Name intent, not appearance

Name variants by what they do, not how they look. `primary`, `secondary`, `tertiary` survive a restyle. `solid`, `flat`, `bordered` don't, because the rename touches every call site.

Emphasis creates visual hierarchy. The reader should find the main action without reading.

| Level | Purpose | Limit |
|---|---|---|
| Primary | The action that moves the user forward | One per view or context |
| Secondary | Alternative actions | Several allowed |
| Tertiary | Dismissive actions such as cancel or skip | Use sparingly |
| Danger | Destructive actions | Only where something is destroyed |

```tsx
<Button variant="primary">Save</Button>
<Button variant="secondary">Edit</Button>
<Button variant="tertiary">Cancel</Button>
```

Two primary buttons on one screen means the hierarchy failed. Demote one.

Hierarchy also comes from size, weight, contrast, and spacing. Use them to rank content. Don't give everything the same weight and hope grouping does the work.

## 2. Accessibility is the base layer

Build it in at the start. Retrofitting costs more than the original work and usually misses cases.

- Target WCAG 2.1 AA at minimum: 4.5:1 text contrast, 3:1 for large text and UI boundaries.
- Use native elements first (`button`, `a`, `input`, `dialog`). Reach for ARIA only when no native element fits.
- Every interactive element works by keyboard, with a visible focus ring and a logical tab order.
- Give every control an accessible name. Icon-only buttons need `aria-label`.
- Never convey state by color alone. Pair it with text, an icon, or a shape.
- Prefer a tested headless primitive library (React Aria, Radix, Base UI) over hand-rolled tabs, menus, comboboxes, and dialogs. Their keyboard and screen reader behavior took years to get right.

`web-interface-guidelines.md` has the full review checklist.

## 3. Compose, don't configure

A component with twenty props is a component that can't do the twenty-first thing. Split it into parts the caller can arrange, swap, or leave out.

```tsx
<Accordion>
  <Accordion.Item id="1">
    <Accordion.Trigger>Question</Accordion.Trigger>
    <Accordion.Panel>Answer</Accordion.Panel>
  </Accordion.Item>
</Accordion>
```

Cost in a year: composed APIs take more lines per use but rarely need a breaking change. Prop-heavy APIs need a new prop, or a fork, for every new layout.

## 4. Disclose complexity progressively

The default case takes the fewest props. Each extra requirement adds one more.

```tsx
<Button>Click me</Button>
<Button variant="primary" size="lg">Submit</Button>
<Button variant="primary" isDisabled={isLoading}>
  {isLoading ? <><Spinner size="sm" /> Loading</> : "Submit"}
</Button>
```

Apply the same rule to screens. Show the common path first and put advanced options behind a disclosure, a secondary panel, or a settings page. Don't show every control at once.

## 5. Be predictable

The same concept uses the same name and behaves the same way everywhere.

- Sizes are `sm`, `md`, `lg` on every component, not `small` on one and `compact` on another.
- Every component accepts `className` and forwards `ref`.
- State is exposed the same way, for example `data-pressed`, `data-disabled`, `data-focus-visible`.
- Spacing, radius, and type come from a scale. A value outside the scale needs a reason.

If a user has to relearn the pattern on the next component, the system has a bug.

## 6. Keep tokens separate from components

Colors, radius, spacing, type, and motion live in tokens (CSS variables). Components read tokens and hold no raw values.

```css
:root {
  --accent: oklch(0.7 0.25 260);
  --radius: 0.375rem;
  --space: 0.5rem;
}
```

One token change then re-themes the whole product, and dark mode is a second set of token values, not a second set of components. Keep styling reachable without the framework too, through plain classes or a variants function, so a router link or a native element can look like a button.

## 7. Make types do the checking

Typed props catch invalid variants, sizes, and event shapes at build time instead of in review.

```tsx
import type { ButtonProps } from "./button";

interface SaveButtonProps extends Omit<ButtonProps, "variant"> {
  intent: "save" | "cancel" | "delete";
}
```

Use string-literal unions for variants. Extend or `Omit` the base props in wrappers so the wrapper can't drift from the component it wraps.

## 8. Allow extension without forking

Good defaults should look finished. Callers still need three ways to change them, from least to most invasive:

1. Override tokens.
2. Pass `className` or use the variants function.
3. Wrap the component in a thin component that maps your domain words to its variants.

```tsx
const variantMap = { "primary-cta": "primary", minimal: "ghost" } as const;

function CTAButton({ intent = "primary-cta", ...props }: CTAButtonProps) {
  return <Button variant={variantMap[intent]} {...props} />;
}
```

If callers copy the component source to change it, the extension points are missing. Add one, don't tolerate the copies.

## Review checklist

- One primary action per view, and the hierarchy reads at a glance.
- Variants are named by intent.
- Keyboard, focus, contrast, and accessible names pass.
- Composed parts, not a growing prop list.
- Defaults need few props. Advanced options stay out of the way.
- Sizes, states, and naming match the rest of the system.
- No raw color, spacing, or radius values outside tokens.
- Variants and props are typed.
- Wrapping or overriding works without copying source.
