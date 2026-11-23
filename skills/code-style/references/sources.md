# How these rules compare

Where each rule stands against published style guides, engineering writing and other agent skills. Use it to tell a widely shared rule from a personal preference: when a project's own conventions conflict with a personal preference, the project wins without discussion. When they conflict with a widely shared rule, it is worth raising.

Sources were read in November 2026. Quotes are short; follow the links for context.

## Formatting

| Rule here | Published guidance | Standing |
| --- | --- | --- |
| Objects one property per line | Prettier keeps an object multi-line once its first key is on a new line, because "sometimes it really helps readability", and never collapses it. Airbnb puts each item of a multi-line array or signature on its own line. Standard only asks for consistent newlines. | Personal preference, compatible with Prettier and oxfmt (`objectWrap: "preserve"`). |
| Trailing commas | Airbnb and Prettier use them; Standard forbids them. | Common, not universal. |
| Blank line between groups | Airbnb: "Leave a blank line after blocks and before the next statement." Prettier preserves single blank lines. | Widely shared. |
| Guards first, shallow nesting | Airbnb: no `else` after a block that always returns. addyosmani's simplification skill flags nesting of 3+ levels. | Widely shared. |
| Ternary only for two plain values | Airbnb: "Ternaries should not be nested and generally be single line expressions"; "Avoid unneeded ternary statements." Standard: no ternaries "when simpler alternatives exist". | Widely shared. A total ban is a stricter personal preference. |
| Name compound conditions | Clean Code JS encapsulates conditionals into named predicates (`shouldShowSpinner`). | Common practice. The three-operand threshold is personal. |

## Naming

| Rule here | Published guidance | Standing |
| --- | --- | --- |
| Clear at the call site | Swift API guidelines: "Clarity at the point of use is your most important goal." Google: names "must be descriptive and clear to a new reader". | Widely shared. |
| No dropped-letter abbreviations | Google: "do not abbreviate by deleting letters within a word." Airbnb: "Avoid single letter names." Google allows short names in scopes of about ten lines. | Widely shared. |
| No type or mechanism suffixes | Swift: "Omit needless words", don't "repeat type information"; name by role, not type. Google: names "should not be decorated with information that is included in the type." | Widely shared. |
| Don't repeat folder, file or owner | Swift: `remove(_:)` over `removeElement(_:)`. | Follows from "omit needless words"; the lint check is personal. |
| One to three words | No guide sets a word limit. | Personal guideline. |
| No `handle…` prefix | Not addressed by the major guides; React code commonly uses `handleX`. | Personal preference. Follow a project that uses `handle`. |
| Verbs for effects, nouns for values, assertions for booleans | Swift: effects as "imperative verb phrases", no effects as "noun phrases", booleans "read as assertions about the receiver". Airbnb: `isVal()`/`hasVal()`. | Widely shared. |

## Functions, classes and structure

| Rule here | Published guidance | Standing |
| --- | --- | --- |
| Inline single-use helpers | Fowler extracts even one-line, single-use functions when the name states intention ("separation between intention and implementation"). Google: "nothing wrong with a private helper method or class that is used only once." Ousterhout: "only decompose if it can be done cleanly"; size "doesn't really matter that much". | Contested. The rule here sides with Ousterhout against Fowler. Naming a step to state intention is still allowed. |
| Classes for concepts that own state or a value | Ousterhout wants "deep" classes: "a simple interface" over "a simple implementation", "200-2000 lines are fine", and warns against "classitis". Maxwell: classes when an object "has internal state its methods update over time". Rust groups a type's operations in one `impl` block "for organization". Angular builds services as classes. | Shared for stateful concepts. Preferring classes beyond that is a personal preference. |
| Functions for stateless work | Google: prefer module functions to private static methods; no container classes. Maxwell: no classes "as a namespace". React moved components from classes to functions, citing `this`, minification and reuse. Functional core, imperative shell keeps logic pure. | Widely shared, especially in front-end code. |
| No static-only classes | Google and Maxwell both reject them. | Widely shared. |
| No mutable module state | Google: `export let` is not allowed; expose state through functions. | Shared for exported state; extending it to private module state is personal. |
| No thin wrappers | Ousterhout calls pass-through methods a red flag. addyosmani's review skill: delete pass-through wrappers. Fowler accepts a one-line method if its name adds meaning. | Mostly shared. |
| Wait for the third use before abstracting | Dodds (AHA): "prefer duplication over the wrong abstraction." Abramov: deduplication "traded the ability to change requirements". addyosmani: "Don't generalize until the third use case." | Widely shared. |
| Small functions | Fowler: more than "half-a-dozen lines" starts to smell. Clean Code: "Functions should do one thing." addyosmani: 50+ lines is a signal. Ousterhout: depth matters more than size. | Contested. This skill sets no length limit; it asks for depth and readable steps. |

## Errors and suppressions

| Rule here | Published guidance | Standing |
| --- | --- | --- |
| Never swallow errors | Clean Code JS: don't ignore caught errors. | Widely shared. |
| No placeholder data | ciembor's Clean Code rules: prefer "typed results over null-like sentinel flow". | Widely shared in spirit. |
| No suppression comments | Prettier recommends `eslint-disable-next-line` when needed. Google allows type assertions with a reason in a comment. | Stricter than mainstream. A personal rule, held because agents use suppressions to get past checks. |

## How other agent skills are built

- **Anthropic's skill authoring guide:** SKILL.md under 500 lines; references one level deep; a table of contents in reference files over 100 lines; "only add context Claude doesn't already have"; a default with an escape hatch instead of many options.
- **addyosmani/agent-skills:** read CLAUDE.md and "match the project's style"; preserve behaviour exactly; scope changes to what changed; review findings labelled `Critical`, `Nit`, `Optional`.
- **vercel-labs/agent-skills:** one file per rule with an impact level and Incorrect/Correct code pairs.
- **ciembor/agent-rules-books:** short imperative rules distilled from books, in nano/mini/full sizes; no examples.

This skill follows the same pattern: a short entry file, one-level references, ❌/✅ examples with reasons, and the project's conventions ahead of the skill's preferences.

## Links

- Google TypeScript style guide: https://ts.dev/style/
- Airbnb JavaScript style guide: https://github.com/airbnb/javascript
- Standard JS rules: https://standardjs.com/rules.html
- Prettier rationale: https://prettier.io/docs/rationale
- Swift API design guidelines: https://www.swift.org/documentation/api-design-guidelines/
- Clean Code JavaScript: https://github.com/ryanmcdermott/clean-code-javascript
- Martin Fowler, Function Length: https://martinfowler.com/bliki/FunctionLength.html
- John Ousterhout, modular design lecture: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign
- Kent C. Dodds, AHA programming: https://kentcdodds.com/blog/aha-programming
- Dan Abramov, Goodbye, Clean Code: https://overreacted.io/goodbye-clean-code/
- Sean Maxwell, TypeScript best practices: https://github.com/seanpmaxwell/Typescript-Best-Practices
- React, hooks motivation: https://legacy.reactjs.org/docs/hooks-intro.html
- Angular style guide: https://angular.dev/style-guide
- Functional core, imperative shell: https://kennethlange.com/functional-core-imperative-shell/
- Rust book, method syntax: https://doc.rust-lang.org/book/ch05-03-method-syntax.html
- Anthropic skill authoring best practices: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- addyosmani/agent-skills: https://github.com/addyosmani/agent-skills
- vercel-labs/agent-skills: https://github.com/vercel-labs/agent-skills
- ciembor/agent-rules-books: https://github.com/ciembor/agent-rules-books
