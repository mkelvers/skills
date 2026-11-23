---
name: design
description: Builds, restyles and reviews web UI, landing pages, Figma files and motion; use for any interface, page, animation, mobile-web or accessibility work.
---

# Design

Make interfaces that are clear at a glance, consistent in every detail, and look like the person asked for them, not like a generated template.

Good-looking UI is mostly learnable: a clear hierarchy, a small system of sizes and colours used consistently, and the details most pages skip. Taste is the rest, and it belongs to the person you're designing for. You get it from them through examples, not by guessing. Guessing intent and filling the gap with decoration is how designs get rejected.

In an existing product, its stack, components and tokens come first. A screen that looks great but doesn't match the rest of the product looks broken.

## How to work

1. **Understand the intent.** What should a visitor understand and do? Ask only what changes the design, offer a suggestion with each question, and confirm your summary before building.
2. **Get the taste from examples.** Ask for two or three sites or screenshots they like. If they have none, build two or three distinct directions behind a switcher ([prototype.md](references/prototype.md)) and let them pick.
3. **Plan the system before code:** colours, type, spacing, radius and layout. Check the plan against the generated defaults in [visual.md](references/visual.md) and change anything that would fit any similar page.
4. **Build section by section** on that system, with real content.
5. **Look at it.** Render it, screenshot it at desktop and phone widths, critique it, and remove one thing. Most design problems are invisible in code.

## References

[visual.md](references/visual.md) holds the core of this skill. Read it in full for any UI work; the others are for specific jobs.

| The task | Read |
| --- | --- |
| Any page, screen or component | [visual.md](references/visual.md) |
| A landing page or marketing site | [landing-page.md](references/landing-page.md), after visual.md |
| A component library or design system | [components.md](references/components.md) |
| Accessibility, forms, focus, or a code review of UI | [web-interface-guidelines.md](references/web-interface-guidelines.md) |
| Stress-testing UI with worst-case data | [break-ui.md](references/break-ui.md), with [break-ui-catalog.md](references/break-ui-catalog.md) |
| Showing several versions to choose from | [prototype.md](references/prototype.md), with [prototype-picker.md](references/prototype-picker.md) |
| A web app that should feel native on a phone | [mobile-native.md](references/mobile-native.md) |
| Anything in Figma | [figma.md](references/figma.md) |
| Any animation | [animation-rules.md](references/animation-rules.md), then [animate-recipes.md](references/animate-recipes.md) for code |
| Animation reasoning, springs, interruptible motion | [emil-design-eng.md](references/emil-design-eng.md) |
| Gestures, drag, sheets and physical motion | [apple-design.md](references/apple-design.md) |

## Before you finish

- The intent is clear in five seconds, with one primary action per screen.
- Every value comes from the planned system or the product's tokens.
- Nothing on the page is one of the generated defaults unless the brief asked for it.
- Hover, focus, loading, empty and error states exist.
- You looked at it rendered, at desktop and phone widths.

## Sources

Built on Emil Kowalski's design-engineering skills (MIT, `LICENSE`), Anthropic's `frontend-design` skill (Apache-2.0, `LICENSE-frontend-design.txt`) and Vercel's Web Interface Guidelines (MIT, `LICENSE-vercel.txt`). `components.md` is reworked from the HeroUI v3 design principles. `visual.md` also draws on *Refactoring UI*, Matthew Butterick's *Practical Typography* and Paul Bakaus's Impeccable.
