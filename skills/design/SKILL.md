---
name: design
description: Builds, restyles, and reviews web UI, landing pages, Figma designs, and motion. Use when creating or polishing an interface or page, designing in Figma, adding or reviewing animation, making a web app feel native on a phone, or reviewing accessibility.
---

# Design

The references hold the knowledge. This file only routes. Read each reference you pick in full.

The project's stack and tokens win. Match its framework, CSS conventions, and existing easing tokens before adding new ones. Check the result in a browser.

## Start here

- New page, hero, or redesign: `references/quiet-ui.md`, then open the matching screenshots in `references/images/`.
- Landing page or marketing site: `references/landing-page.md` as well.
- Anything in Figma: `references/figma.md`.
- Any other UI task: `references/emil-design-eng.md`.

## References

All files are in `references/`.

**Intent and look**
- `quiet-ui.md`: understand intent first, one primary action per screen, familiar structure. Wins over `frontend-design.md`.
- `images/`: liked screenshots, indexed in `images/README.md`.
- `frontend-design.md`: distinctive direction, typography, palette, layout.
- `design-principles.md`: hierarchy, accessibility, composition, tokens.
- `design-craft.md`: judging good against poor design, with a review checklist.

**Pages and tools**
- `landing-page.md`: intake, structure, copy, SEO, visual rules for landing pages.
- `figma.md`: variables, text styles, auto layout, components, and tokens in Figma.

**Quality and review**
- `web-interface-guidelines.md`: accessibility, forms, focus, semantics, reported as `file:line`.
- `break-ui.md`, then `break-ui-catalog.md`: stress-test with worst-case data.
- `mobile-native.md`: make a web app feel native on a phone.
- `prototype.md`, then `prototype-picker.md`: several versions behind a switcher.

**Motion**
- `animation-rules.md`: the short list of rules. Read for any animation work.
- `emil-design-eng.md`: the reasoning behind them.
- `animate.md`, then `animate-recipes.md`: build an animation.
- `review-animations.md`, then `review-animations-standards.md`: review animation code.
- `improve-animations.md`, `improve-animations-audit.md`, `improve-animations-plan-template.md`: audit and plan fixes.
- `find-animation-opportunities.md`: where to animate and where not to.
- `apple-design.md`: gestures, springs, drag, sheets, interruptible motion.
- `animation-performance.md`, `performance-cheatsheet.md`: dropped frames, `will-change`.
- `animation-vocabulary.md`: names for effects.

## Sources

Merged from Emil Kowalski's skills (MIT, `LICENSE`), `frontend-design` from anthropics/skills (Apache-2.0, `LICENSE-frontend-design.txt`), and Vercel's Web Interface Guidelines (MIT, `LICENSE-vercel.txt`). `design-principles.md` is reworked from the HeroUI v3 design principles page. `landing-page.md` and `figma.md` are the former `landing-page-design` and `figma-designer` skills. Some references still name each other by old skill names such as `animate` or `review-animations`. Each matches the file of the same name above.
