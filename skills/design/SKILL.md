---
name: design
description: Builds, restyles and reviews web UI, landing pages, Figma files and motion; use for any interface, page, animation, mobile-web or accessibility work.
---

# Design

Make interfaces that are clear at a glance and feel considered in every detail, in the project's own visual language. This file routes; the references hold the knowledge. Read each reference you pick in full, because their rules depend on each other and skimming loses the reasons.

The project's stack and design tokens come first. Match its framework, CSS conventions, components and existing easing or spacing tokens before adding new ones, so the result looks like it belongs. Check the result in a browser; most design problems are only visible when rendered.

## Where to start

| The task | Read first |
| --- | --- |
| A new page, a hero or a redesign | [quiet-ui.md](references/quiet-ui.md), then the screenshots indexed in [images/README.md](references/images/README.md) |
| A landing page or marketing site | [landing-page.md](references/landing-page.md), after quiet-ui.md |
| Anything in Figma | [figma.md](references/figma.md) |
| Any animation | [animation-rules.md](references/animation-rules.md), then the matching motion file below |
| Any other UI work | [emil-design-eng.md](references/emil-design-eng.md) |

When two references disagree, [quiet-ui.md](references/quiet-ui.md) wins over [frontend-design.md](references/frontend-design.md): understand what the page is for before giving it a distinctive look.

## All references

**Intent and look**

- [quiet-ui.md](references/quiet-ui.md): understand intent first, one primary action per screen, familiar structure.
- [frontend-design.md](references/frontend-design.md): a distinctive direction in typography, palette and layout.
- [design-principles.md](references/design-principles.md): hierarchy, accessibility, composition and tokens that hold up as a system grows.
- [design-craft.md](references/design-craft.md): telling good design from generic, with a review checklist.

**Pages and tools**

- [landing-page.md](references/landing-page.md): intake, structure, copy, SEO and visual rules for landing pages.
- [figma.md](references/figma.md): variables, text styles, auto layout, components and tokens in Figma.

**Quality and review**

- [web-interface-guidelines.md](references/web-interface-guidelines.md): accessibility, forms, focus and semantics, reported as `file:line`.
- [break-ui.md](references/break-ui.md) with [break-ui-catalog.md](references/break-ui-catalog.md): stress-test UI with worst-case data.
- [mobile-native.md](references/mobile-native.md): make a web app feel native on a phone.
- [prototype.md](references/prototype.md) with [prototype-picker.md](references/prototype-picker.md): build several versions behind a switcher to compare.

**Motion**

- [animation-rules.md](references/animation-rules.md): the short list of rules agents break most. Read for any animation work.
- [emil-design-eng.md](references/emil-design-eng.md): the reasoning behind those rules.
- [animate.md](references/animate.md) with [animate-recipes.md](references/animate-recipes.md): build an animation.
- [review-animations.md](references/review-animations.md) with [review-animations-standards.md](references/review-animations-standards.md): review animation code.
- [improve-animations.md](references/improve-animations.md) with [improve-animations-audit.md](references/improve-animations-audit.md) and [improve-animations-plan-template.md](references/improve-animations-plan-template.md): audit motion and plan fixes.
- [find-animation-opportunities.md](references/find-animation-opportunities.md): where motion helps and where it doesn't.
- [apple-design.md](references/apple-design.md): gestures, springs, drag, sheets and interruptible motion.
- [animation-performance.md](references/animation-performance.md) with [performance-cheatsheet.md](references/performance-cheatsheet.md): dropped frames and `will-change`.
- [animation-vocabulary.md](references/animation-vocabulary.md): the precise names for effects.

## Before you finish

- The result uses the project's components and tokens, not new one-offs.
- You looked at it rendered, at desktop and phone widths.
- Every animation follows animation-rules.md and respects reduced motion.
- Interactive elements work with a keyboard and have accessible names.

## Sources

Merged from Emil Kowalski's skills (MIT, `LICENSE`), `frontend-design` from anthropics/skills (Apache-2.0, `LICENSE-frontend-design.txt`) and Vercel's Web Interface Guidelines (MIT, `LICENSE-vercel.txt`). `design-principles.md` is reworked from the HeroUI v3 design principles page. `landing-page.md` and `figma.md` were separate skills before.
