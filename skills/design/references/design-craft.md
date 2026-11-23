# Design craft

What separates a good interface from a generic one, drawn from published work by named designers and researchers. Use it to judge a screen before and after you build it.

Every rule below names its source. Rules marked † come from memory of well-known guidance and were not re-checked against the primary page. The code and diagrams are illustrations written for this file, not quotes from the sources. Where a rule has a number, the source gave the number.

## 1. Hierarchy and grouping

**Source:** Adam Wathan and Steve Schoger, *Refactoring UI*. Nielsen Norman Group (NN/g) articles on proximity and common region.

Hierarchy answers "what do I look at first, second, last". Three levers do most of the work: size, weight, and contrast. Color is the weakest lever.

Rules from *Refactoring UI* (the book itself was not fetched; these come from summaries of it):

- Build hierarchy from spacing, weight, and size, not color alone.
- Design in grayscale first. If the hierarchy holds without color, color only reinforces it.
- Mute secondary content instead of boosting primary content.
- Save bold color for the call to action.
- Rank buttons by their role on this screen, not by how important the action sounds.
- Start with too much whitespace, then remove.

Rules from NN/g:

- **Proximity.** Items close together read as one group. Proximity can override similarity in color or shape.
- **Common region.** Items inside a boundary (border, card, fill) read as a group. A boundary overrides proximity and similarity. Overuse creates clutter, so draw boundaries only where grouping is ambiguous.

Before and after. Same content, same font size for everything, so nothing leads:

```
BEFORE                              AFTER
Invoice #4021                       Invoice #4021          (14px, muted)
Acme Corp                           $1,280.00              (32px, 600 weight)
$1,280.00                           Acme Corp · Due Nov 30 (14px, muted)
Due Nov 30                          [ Pay now ]            (only filled button)
Pay now   Download   Share         Download   Share       (text buttons)
```

```css
/* the AFTER, expressed as rules */
.invoice-id, .invoice-meta { font-size: 0.875rem; color: var(--text-muted); }
.invoice-total { font-size: 2rem; font-weight: 600; }
.btn-primary { background: var(--accent); }            /* one per card */
.btn-secondary { background: transparent; color: var(--text-muted); }
```

Test: squint at the screen, or blur it. You should still see the one thing that matters.

## 2. Typography

**Source:** Matthew Butterick, *Practical Typography* (practicaltypography.com, "Summary of key rules").

- Body size on the web: 15 to 25 px.
- Line spacing: 120% to 145% of the font size.
- Line length: 45 to 90 characters, spaces included. Measure in characters, not pixels.
- Smaller type needs wider margins, and the reverse.

```css
.prose {
  font-size: 1.0625rem;   /* 17px */
  line-height: 1.4;       /* 140%, inside 120% to 145% */
  max-width: 65ch;        /* inside 45 to 90 characters */
}
```

Use `ch` for the width. It tracks the font, so the character count survives a font change.

## 3. Usability heuristics

**Source:** Jakob Nielsen (with Rolf Molich), ten usability heuristics, first defined in 1990 and stable since 1994. Official text: nngroup.com, "10 Usability Heuristics for User Interface Design". The search did not return that page, so the names are from memory and the UI examples are mine.

| Heuristic | What a failure looks like | What fixes it |
|---|---|---|
| Visibility of system status | Click "Save", nothing changes | Button shows "Saving...", then "Saved" |
| Match with the real world | Error: `ERR_ENOENT 0x2` | "We couldn't find that file. It may have been moved." |
| User control and freedom | Delete is final, no exit from a wizard | Undo toast, visible Cancel and Back |
| Consistency and standards | A trash icon that archives | Same icon, same word, same result everywhere |
| Error prevention | Free-text date field | Date picker, disabled invalid options, confirm only destructive acts |
| Recognition over recall | User must remember a code from page 1 | Show the value on page 3 |
| Flexibility and efficiency | Mouse-only power-user flows | Shortcuts and defaults that skip steps for repeat users |
| Aesthetic and minimalist design | Ten equal-weight links | Show the few that matter, hide the rest behind one control |
| Recover from errors | "Something went wrong" | Say what broke and what to do next, next to the field |
| Help and documentation | Docs in a separate site nobody finds | Short help at the point of need |

## 4. Laws of UX

**Source:** Jon Yablonski, *Laws of UX* (O'Reilly, 2020; second edition since). Site: lawsofux.com. Figures below came from search summaries of the book.

| Law | Finding | Apply it |
|---|---|---|
| Jakob's Law | People spend most of their time on other sites and expect yours to work the same | Put the logo top-left, search as a field, cart as a cart. Spend novelty on the product, not the controls. |
| Fitts's Law | Large, close targets are faster to reach | Make primary touch targets big. 44 pt (Apple) or 48 dp (Material) is the common floor.† Put the confirm button near the thumb. |
| Hick's Law | Decision time grows with the number of options | Cut options, group them, or reveal in steps. |
| Miller's Law | Working memory holds roughly 7 ± 2 items (1956). Later work suggests nearer 4 ± 1. | Chunk long numbers and lists. Don't design around "7". |
| Doherty Threshold | Productivity rises when the system responds within about 400 ms. Not a magic number. | Show feedback inside 400 ms. Past that, show progress. |
| Aesthetic-Usability Effect | Attractive interfaces are seen as more usable and get forgiven for minor flaws. Not for major ones. | Polish helps, but it doesn't fix a broken flow. |
| Von Restorff Effect | The item that differs from its neighbors is remembered | Make the one thing that matters different. Highlight everything and nothing stands out. |
| Peak-End Rule | People judge an experience by its most intense moment and its ending | Work on the best moment and the last screen. Make the confirmation page good. |

## 5. Emotion

**Sources:** Don Norman, *Emotional Design* (2003/2004). Aarron Walter, *Designing for Emotion* (A Book Apart, 2011). NN/g, "Theory of user delight".

**Norman's three levels.** A design should work on all three.

- **Visceral.** First impression: look and feel before use. Typography, color, spacing, polish.
- **Behavioral.** The pleasure and effectiveness of use. Fast, predictable, in control.
- **Reflective.** Meaning and self-image. Whether using it says something the user is proud of.

**Walter's pyramid.** Adapted from Maslow. Bottom to top: functional, reliable, usable, pleasurable. Each tier needs the one below it. NN/g reads this as: delight sits at the top and only counts once the base works.

What this means in practice:

- A loading animation on a broken form is decoration. Fix the form, then add the animation.
- Delight belongs at low-stress moments: a finished task, an empty state, the last screen. Put it in front of someone mid-error and it reads as mockery.
- Personality comes from copy, spacing, and motion working together. A gradient alone doesn't carry it.

```
Empty state, flat:     "No items."
Empty state, with a job:
  No invoices yet.
  Create one and it will show up here.   [ New invoice ]
```

The second tells the user what happened and what to do. The warmth is in the wording, not in an illustration.

## 6. Motion

**Sources:** Apple Human Interface Guidelines, Motion. Google Material, "Making motion meaningful". Disney's twelve principles, as applied to UI in various articles.

- Apple: add motion purposefully. Don't use it for its own sake. Keep feedback brief and precise. Let people cancel motion instead of waiting. Reduce or remove animation when Reduce Motion is on.
- Material: motion should be responsive, natural, aware, and intentional.
- Disney's principles are contested for UI. Easing is the principle that carries over best. Willenskomer (cited by Adobe) argues interfaces need their own principles because the Disney set was built for drawing physical objects in 2D.

Treat motion as a tool for showing cause and effect, not as decoration. The concrete rules (durations, easing curves, what not to animate) are in `emil-design-eng.md` and the `SKILL.md` rules.

## 7. A taste test

**Source:** Dieter Rams, ten principles of good design, from *Less but Better*. They work as criteria for judging, not as rules. The sources I fetched confirmed five by name; the rest are from memory.

Good design is: innovative, useful, aesthetic, understandable, unobtrusive, honest, long-lasting, thorough down to the last detail, environmentally friendly, and as little design as possible.

Ask three questions of any screen:

1. **Useful and understandable.** Can a first-time user say what it does and what to press?
2. **Unobtrusive and honest.** Does the interface step back from the content? Does it promise only what it delivers?
3. **Thorough to the last detail.** Check the empty state, the error state, the loading state, the 3-character and 300-character name, focus rings, and the 320 px width.

## 8. Telling good from poor

Signs of a poor design:

| Sign | Why it fails | Source principle |
|---|---|---|
| Everything is the same size and weight | No hierarchy, no entry point | Refactoring UI |
| Everything is highlighted | Nothing stands out | Von Restorff |
| Cards inside cards inside cards | Boundaries stop meaning grouping | NN/g, common region |
| Novel controls for standard tasks | Users relearn what they already know | Jakob's Law |
| Looks polished, breaks at 320 px or with long text | Polish masks a broken flow | Aesthetic-Usability |
| "Something went wrong" | Gives no recovery path | Nielsen |
| Animation with no cause | Motion without purpose | Apple HIG |
| Copy written to steer, not inform | Deception | Brignull |

**Deceptive patterns.** Harry Brignull coined "dark patterns" in 2010 and catalogs them at deceptive.design. Do not build these, and flag them in reviews. Names from the original list: roach motel (easy in, hard out), confirmshaming (guilt-trip decline text), hidden costs, bait and switch, forced continuity, misdirection, privacy zuckering, disguised ads, friend spam. The catalog has grown past that original twelve.

```
Confirmshaming:   [ Yes, save me money ]   [ No, I enjoy overpaying ]
Honest version:   [ Subscribe ]            [ Not now ]
```

## 9. Reviewing a screen

1. Squint test: is there one clear first thing?
2. Grayscale test: does the hierarchy survive without color?
3. Run Nielsen's ten against the main flow.
4. Count the choices on the screen (Hick). Cut or group.
5. Check the states: empty, loading, error, long text, 320 px.
6. Check the last screen and the one most intense moment (Peak-End).
7. Check that it matches the product's own conventions (Jakob, Consistency).
8. Search the copy for anything that steers instead of informs.

## Sources

Search results were mostly secondary summaries. Fetch the primary page before quoting a number or a name.

- Adam Wathan and Steve Schoger, *Refactoring UI*: refactoringui.com, and the authors' Medium post "7 Practical Tips for Cheating at Design"
- Jakob Nielsen and Rolf Molich, ten usability heuristics: nngroup.com/articles/ten-usability-heuristics
- Jon Yablonski, *Laws of UX*: lawsofux.com
- Don Norman, *Emotional Design*
- Aarron Walter, *Designing for Emotion*, and nngroup.com/articles/theory-user-delight
- NN/g on [common region](https://www.nngroup.com/articles/common-region/) and [proximity](https://www.nngroup.com/articles/gestalt-proximity/)
- Matthew Butterick, [Practical Typography, summary of key rules](https://practicaltypography.com/summary-of-key-rules.html)
- Dieter Rams, *Less but Better*, and [principles.design](https://principles.design/examples/ten-principles-of-good-design)
- Harry Brignull, [deceptive.design](https://deceptive.design)
- Apple Human Interface Guidelines, [Motion](https://developer.apple.com/design/human-interface-guidelines/motion)
- Google Design, [Making motion meaningful](https://design.google/library/making-motion-meaningful)
