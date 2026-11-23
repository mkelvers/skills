# Reviewing TypeScript

Read the diff against the rules in `SKILL.md`. Flag only what you can point at. Report each finding with `file:line`, the rule it breaks, and the fix.

Look for:

- **Layers with no job.** Wrappers that only forward a call, `Foo` plus `FooImpl` pairs, factories where `new` works, classes that only group functions, generics with one use.
- **Unvalidated input.** Unvalidated values flowing into code that assumes their shape, casts from unvalidated data, an interface duplicating a Zod schema, trivial helpers wrapping `.parse`.
- **Hidden invalid state.** `??` or `||` defaults on required data, swallowed errors, thrown strings, lost `cause`, string-typed errors where a result type fits.
- **Database ownership.** A connection or transaction with an unclear lifetime, or database plumbing that adds no isolation or ownership.
- **Missing contract docs.** An exported contract whose obligations are missing, or TSDoc that only restates the name.
- **Unreadable structure.** Compressed unions and option objects, vague names (`data`, `manager`, `utils`), code in a file it doesn't belong to.

Finish with the two questions in `SKILL.md`: could someone reading only the public types and docs use this, and is any part here only because it looked like good architecture?
