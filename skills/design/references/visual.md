# Making it look good

Good-looking UI is mostly not taste. It is clear hierarchy, a small consistent system of sizes and colours, and attention to the details most generated pages skip. Taste decides the remaining part, and that comes from the person you are designing for, not from you. This file covers both.

Contents: [Intent](#intent-first) · [Taste](#taste-comes-from-examples) · [Plan](#plan-the-system-before-the-code) · [Hierarchy](#hierarchy) · [Typography](#typography) · [Space](#space-and-layout) · [Colour](#colour-and-surfaces) · [Copy](#copy) · [Generated defaults](#what-makes-ui-look-generated) · [Craft](#the-craft-floor) · [Critique](#look-at-it-then-cut)

## Intent first

Before anything visual, know what the screen is for. A design can only be intentional once you know what a visitor should understand and do. Read the request closely, then ask only what changes the design: what the page needs a visitor to do, what goes first, and what they should do if they aren't ready. Offer a sensible suggestion with each question, so "you decide" is a real answer.

Then sum up in a few lines what you understood and let the person correct it. Every element on the page must serve that purpose or help people find their way; cut whatever does neither.

Follow the conventions of the category. People spend most of their time on other sites and expect yours to work the same way. A shop has departments across the top; an article starts with the article. Put originality into how it looks and what it chooses to say first, never into where things are.

## Taste comes from examples

You can't infer someone's taste, and describing it in words rarely works. Get it from examples:

- **Ask for two or three sites or screenshots they like** for this kind of page, and what they like about each. Take structure, hierarchy and tone from them; leave brand and content.
- **Or show options.** When they can't name references, build two or three clearly different directions behind a switcher ([prototype.md](prototype.md)) and let them pick. Reacting to something real is much easier than describing a preference.
- **In an existing product,** the product is the reference. Match its components, tokens and spacing before inventing anything; a beautiful screen that doesn't match the rest looks broken.

When you have a direction, commit to it. A page torn between two styles reads as neither.

## Plan the system before the code

Write a short plan first, so every value later comes from a decision instead of being invented on the spot:

- **Colour:** four to six named values: background, surface, text, muted text, one accent, plus a danger colour if needed.
- **Type:** one or two families and their roles, and a type scale.
- **Space:** one spacing scale (for example 4, 8, 12, 16, 24, 32, 48, 64, 96).
- **Radius:** one or two values, used consistently.
- **Layout:** a sentence or a rough ASCII wireframe per section, and where content aligns.

Then check the plan against [the generated defaults](#what-makes-ui-look-generated). If a part of it is what you'd produce for any similar page, change that part and say why. Only then build.

## Hierarchy

Hierarchy answers "what do I look at first, second, last". Size, weight and contrast do most of the work; colour is the weakest lever.

- **One primary action per screen.** It gets the only filled button, the most contrast and the most obvious place. Everything else is visibly secondary. Two filled buttons side by side means the hierarchy failed.
- **Mute secondary content** rather than boosting primary content. Lighter text colour and smaller size push metadata back.
- **Group with space before borders.** Things close together read as one group. Add a border or card only where grouping is still ambiguous; cards inside cards stop meaning anything.
- **Limit choices.** A navigation of four to seven items; one message and one action in a hero. More options go behind one entry point.

Test it: squint at the screenshot, or view it in grayscale. The one thing that matters should still be the first thing you see.

## Typography

Type carries most of a page's personality, and most of its polish.

- **One or two families.** If two, make them clearly different, one for display and one for text. Choose them deliberately for this brief rather than reaching for the default.
- **A real scale.** Every size comes from the scale; no one-off `19px`. Big steps between levels (for example 14, 16, 20, 24, 32, 48) give clearer hierarchy than many small ones.
- **Body text:** 16 to 18 px on the web, line height about 1.4 to 1.6, lines of 45 to 80 characters (`max-width: 65ch`). Long lines are the most common reason text looks amateur.
- **Headings:** tighter line height (1.1 to 1.25) and slightly tighter tracking at large sizes.
- **Wrapping:** `text-wrap: balance` on headings and `text-wrap: pretty` on body text, so no word sits alone on the last line.
- **Numbers that line up:** `font-variant-numeric: tabular-nums` in tables, prices and counters.
- **Weights:** regular for text, medium or semibold for emphasis. Black weights and many weights at once look heavy and unsure.

## Space and layout

- **Start generous, then remove.** Cramped UI looks cheap faster than anything else. Sections need far more space between them than elements inside them.
- **Every gap comes from the spacing scale.** Consistent rhythm is what makes a page look built rather than assembled.
- **Align to one grid.** Shared left edges and consistent column widths read as order even when the reader can't say why.
- **Nested corners:** when a rounded element sits inside another with a small gap, inner radius = outer radius − gap, so the curves stay parallel.
- **Check at 390 px wide.** Same content, same order, nothing overflowing, the primary action visible on the first screen.

## Colour and surfaces

- **Neutrals plus one accent.** The accent marks the primary action, links and active states. Used for decoration, it stops guiding anyone.
- **Contrast:** at least 4.5:1 for body text and 3:1 for large text and control boundaries.
- **Never colour alone** to show state; pair it with text, an icon or a shape.
- **Depth sparingly.** Pick one way to separate surfaces, a subtle background step, a hairline border or a soft shadow, and use it consistently. Mixing all three looks noisy.
- **Dark mode is a second set of token values,** not a second design. Use real near-black surfaces that step up in lightness for raised layers.
- **Let content carry the emotion:** photography, product shots, real data. Decoration supports the message and never competes with the primary action.

## Copy

Words are part of the design. Copy can make a page feel as templated as its layout.

- Write from the user's side, in plain language: a user manages notifications, not webhook config.
- Buttons say what happens: "Save changes", "Start free trial", never "Submit" or "Learn more". The same action keeps its name through the flow: "Publish" produces "Published".
- Use real, specific content, not placeholder text. On a real product, never invent prices, statistics, testimonials or logos; leave a marked placeholder instead.
- Errors say what failed and what to do next, without apologising. An empty state says what will appear and how to make it happen.
- Sentence case for headings and buttons.

## What makes UI look generated

These are the defaults generated pages fall into whatever the subject. Each is legitimate for some brief; the problem is reaching for it by reflex. When the person's brief asks for one of these, follow the brief.

**Layout**

- Content chopped into identical rounded cards with the same soft grey shadow, especially an icon tile above every heading.
- The hero-metric template: a big number, a small label, a gradient accent.
- Numbered markers (01 / 02 / 03) on content that isn't a sequence.
- A fade-and-slide-up entrance on every section and a hover lift on every card.

**Type and labels**

- A tracked-out ALL-CAPS eyebrow label above every heading.
- One word of a headline in a different colour, italic or weight.
- Metadata joined with middle dots (`A · B · C`), labels like "WORD — fragment", a `→` on every link and button.
- A monospace face for small labels with no data reason.

**Colour and texture**

- A warm cream background with a serif display and a terracotta accent; or near-black with one acid-green or vermilion accent.
- Purple-to-blue gradients, gradient text, and gradient washes as decoration.
- Glass and blur, grain, grid or dot backgrounds with nothing to do.
- Emoji or Unicode symbols used as icons.

## The craft floor

The details that separate built from assembled. Check them on every page.

- **Every state is designed:** hover, active (a slight press, such as `scale(0.97)`), visible keyboard focus, loading (skeletons shaped like the content), empty, and error.
- **The browser defaults are themed:** text selection colour, caret, focus ring, scrollbars where visible.
- **Icons come from one set,** at one stroke width, optically aligned with the text beside them.
- **Images have a fixed aspect ratio,** so nothing jumps while loading.
- **Nothing breaks with real data:** long names, missing images, zero items, a thousand items ([break-ui.md](break-ui.md)).
- **Motion answers an action** and respects reduced motion ([animation-rules.md](animation-rules.md)).

## Look at it, then cut

Render the page and look at a screenshot at desktop and phone widths before calling it done. Most design problems are invisible in code.

Then critique it as the person would: does the squint test pass, does anything compete with the primary action, does any part look like the generated defaults above? Finally, remove one thing. A design is usually improved more by the element you take away than the one you add.
