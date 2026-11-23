# Quiet, intentional UI

The goal is a page where a first-time visitor understands, within a few seconds, what the site is, what it wants them to do, and how to do it. Quiet means no competing asks. It doesn't mean less content or a minimal look. An e-commerce site still looks like e-commerce, with a full header, departments and products. It just never puts ten equal things in front of the user at once.

Read this before `frontend-design.md` for any new page, landing page, screen or redesign. Where the two disagree, this file wins.

## 1. Ask for the intent first

Don't guess the purpose from the codebase or the brief. Guessing produced four rejected designs in the session this file comes from.

A design can only be intentional once you know what it's for, so the first job is to understand what the person is building and what success looks like to them. Read the request closely, notice what it already tells you, and ask about what's still missing. Questions should come out of this particular request, the way a good designer would ask them in a first meeting, not from a checklist. Someone building a portfolio and someone building a shop care about different things, and the questions should show you noticed.

What you're trying to learn is what the page needs a visitor to do, what they should do if they're not ready for that, and what the first screen has to say for that to happen. Often it also helps to know what's happening right now that's worth putting first, and what the person already likes the look of. Ask only what changes the design. Offer a sensible suggestion with each question, so answering is easy and "you decide" is a real option. If there's nothing in `images/` that fits, asking for a couple of sites they admire is often the fastest way to learn their taste.

Before building, sum up what you understood in a few lines (what the page is for, what the visitor should do, and what goes first) and let the person correct it. Every element on the page then has to serve that purpose or help people find their way. If it does neither, cut it.

## 2. Look at the reference images

`images/README.md` lists the screenshots the user likes and the lesson each one teaches. Open every image that matches the task with the Read tool before designing. If there is no reference for this kind of site, ask the user for some instead of inventing a style.

## 3. Principles

**Follow the conventions of the category.** People spend most of their time on other sites and expect yours to work the same way (Jakob's Law). The layout comes from the category, and any novelty goes into the visuals, never into where things are or how they work. Section 4 says more.

**One primary action per screen.** It gets the one filled button, the most contrast and the most obvious position. Everything else is visibly secondary: text links, outline buttons, smaller type. Two filled buttons next to each other means the hierarchy failed.

**Every screen answers three questions.** Where am I? What can I do here? What should I do next? If a first-time visitor can't answer all three in five seconds, fix the hierarchy before adding anything.

**Limit choices at each level (Hick's Law).** Top navigation: 4 to 7 items. Hero: one message and one action, plus at most one text link. Each product row has one theme. If there are more options, group them behind one entry point (a "Shop all" link or a menu), not side by side.

**Hierarchy follows the intent.** The thing that serves the primary action is the largest and highest-contrast element on the screen. Squint at the screenshot: the primary action should still be the first thing you see.

**Use the user's words and mental model.** Group by how shoppers think (Women, Men, Kids, Beauty, Home), not by how the company is organised. Name actions by their result ("Shop the gift guide", "Start free trial"), never "Learn more" or "Click here".

**Remove competing asks, not content.** The things that make a site confusing are interruptions: a newsletter popup on arrival, a cookie banner plus a promo bar plus a chat bubble, an auto-rotating carousel, three calls to action in the hero. Keep the content, and drop or delay the interruptions.

**A calm surface.** Use one spacing scale, a restrained palette (neutrals plus one accent used for the primary action), one or two type families, and consistent radius. Let photography or the product carry the emotion. Decoration supports the message and never competes with the primary action.

**Be predictable.** The same thing looks the same and sits in the same place on every page. Links say where they go. Hover, focus, loading, empty and error states are all designed, and every one of them shows the next step.

**The next step is always visible.** After the hero, after a product, at the end of a list and in an empty state, there is an obvious thing to do next. Dead ends lose users.

## 4. Familiar structure

Every kind of site has a shape people already know. A clothing shop has departments across the top and one seasonal story under them. A product page says what the thing is before listing what it does. An article starts with the article. Before laying out a page, think about the best sites of the same kind and what they all share, and keep that skeleton. People shouldn't have to learn where things are. Put the originality into how it looks and feels, and into what the page chooses to say first.

The mistakes repeat too, whatever the site. They're usually interruptions or a lack of focus: a carousel instead of a decision about what matters, a popup before the visitor has seen anything, several promos shouting at the same volume, navigation hidden when there's room to show it.

## 5. What went wrong in the session this file comes from

On 2026-11-08 the brief was "a landing page with felt textures, about anything". Four designs were rejected before the fifth was accepted (`images/felt-homepage-desktop.png`).

The first put a felt collage in a framed box beside a hero headline, which read as a template and had no clear job. The second made the whole page heavy felt and textured the buttons too, so the text became hard to read. The third was a tidy bento grid of product tiles, clean but made of many equal boxes with nothing to focus on. The fourth paired a big headline with a large felt bird, and the illustration fought the message. The accepted one was a blue felt homepage with a short bio and a row of felt flowers along the bottom edge. It had one clear job, one surface, and decoration that stayed out of the way.

The lesson isn't "always make it minimal". The first four failed because the intent was guessed and decoration filled the gap. The fifth worked because it copied a reference the user chose and had one obvious job. Ask for the intent and a reference first.

## 6. Review checklist

- Can a first-time visitor say in five seconds what the site is and what to do?
- Is there exactly one primary action per screen, and is it the most prominent element?
- Would someone who knows similar sites find their way without thinking?
- Does the hero have one message and at most two actions? Does the nav have 7 items or fewer?
- Is anything competing with the primary action (popups, carousels, equal-weight promos)? Remove or demote it.
- Is the next step visible at the end of every section, and in every empty and error state?
- Squint or grayscale test: does the primary action still stand out?
- Does it read the same on a 390px phone, in the same order?
