---
name: code-style
description: Applies the user's code style when writing, editing, refactoring, or reviewing code in any language and any codebase. Covers formatting, control flow, naming, classes and functions, error discipline, markup, and lint diagnostics, and how to apply them inside a project's existing architecture and tooling.
---

# Code style

This skill is about how code reads. It works in any codebase: the user's own projects, a new one, or a company's codebase with its own architecture and rules.

- **The project decides architecture and tooling:** layering, file layout, how dependencies are passed, classes or functions, its error model, frameworks, linters and their rules, naming conventions and domain words. Follow what is there. Don't add the user's linters or plugins to a project that isn't theirs.
- **These rules decide how the code reads,** in every project: layout, control flow, name quality, helper placement and error discipline. Don't drift toward a looser style because nearby code does.

They give way only where the project has written down something else: its formatter or linter enforces it, or its instructions say so. A habit that only appears in existing code isn't such a rule. Don't reformat code you aren't changing.

## In one screen

- **Objects one property per line,** with trailing commas. Blank lines between declarations, guards, work and result.
- **Guards first, shallow nesting.** `if`/`else` for work; a ternary only picks between two plain values. Name conditions with more than two operands.
- **Short, true names,** clear at the call site. No dropped-letter abbreviations, filler suffixes or type suffixes, and no repeating the folder, file or owner.
- **Classes for concepts, functions for stateless work.** Where the project leaves the choice open, a concept that owns state or a value its operations share is a class. Small stateless work stays a function. Inline single-use helpers.
- **Never swallow an error; never fake missing data.**
- **Fix the code, not the check.** No suppression comments.

## References

| Working on | Read |
| --- | --- |
| Layout, blank lines, branches, ternaries, conditions, intermediate values | [formatting.md](references/formatting.md) |
| Naming or renaming anything | [naming.md](references/naming.md) |
| Classes or functions, helpers, state, constants, wrappers, abstractions | [structure.md](references/structure.md) |
| Catching errors, defaults, missing data | [errors.md](references/errors.md) |
| HTML, JSX, templates, utility classes | [markup.md](references/markup.md) |
| A lint diagnostic, or the project's tooling | [lint.md](references/lint.md) |
| A project the user owns: their toolchain and oxlint plugin | [own-projects.md](references/own-projects.md) |
| Whether a rule is widely shared or a personal preference | [sources.md](references/sources.md) |

For TypeScript types, errors and documentation, use the [TypeScript skill](../typescript/SKILL.md). For visual design, use the design skill.
