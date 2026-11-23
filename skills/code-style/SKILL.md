---
name: code-style
description: Applies the user's code style and TypeScript practices; use whenever writing, editing, reviewing or testing code, or writing code documentation, in any codebase.
---

# Code style

Write code that a reader understands on the first pass, in the shape the project already has.

That sentence holds two jobs, and they come from different places. The project owns its **architecture**: how it is layered, where files live, how dependencies are passed, whether it is built from classes or functions, its error model, its frameworks, its linters and their rules, its naming conventions. The user owns **how code reads**: layout, control flow, naming quality, where helpers go, and how errors are handled. You follow the first and bring the second, in every codebase.

The user's rules give way only to something the project has written down: its formatter or linter enforces a different layout, or its instructions say otherwise. A habit you notice in nearby code is not a rule. Write new code the user's way, and leave code you aren't changing alone.

The question to ask of every change: *would someone new to this codebase understand this faster than the alternative?*

## The rules

**Layout.** Put each property of an object on its own line with a trailing comma, and separate declarations, guards, work and result with blank lines. Readers scan down a column and pause at blank lines; packed lines and unbroken blocks make them parse everything to find anything. Details in [formatting.md](references/formatting.md).

**Control flow.** Return early on the exceptional case so the main path stays at the left margin, and keep nesting shallow. Use `if`/`else` for anything that does work; a ternary only picks between two plain values. Give a condition with more than two parts a name. Each of these keeps one idea per line. Details in [formatting.md](references/formatting.md).

**Names.** A name should be clear at the call site, as short as that allows, and true. Leave out what the folder, file or owner already says, and don't abbreviate by dropping letters. Details in [naming.md](references/naming.md).

**Structure.** Where the project leaves the choice open, a concept that owns state, or a value its operations share, is a class. Small stateless work is a function. Inline a helper that is used once. Avoid both piles of loose little functions and swarms of tiny classes. Details in [structure.md](references/structure.md).

**Errors.** Never drop an error and never invent data to cover a gap. Both let the program carry on in a wrong state and hide the cause. Details in [errors.md](references/errors.md).

**Comments.** Document what a caller can't see from the signature: assumptions, side effects, failure modes, units, lifecycle. A comment inside code explains *why* a non-obvious decision exists. Don't narrate what the code already says, and don't leave comments explaining a lint fix; both go stale and teach the reader to skip comments.

**Markup.** Use the element that means the thing, and keep styling on the element or in the component's variants. Details in [markup.md](references/markup.md).

**TypeScript.** Check data from outside at the boundary and derive its type from the schema; let the compiler see evidence instead of asserting; model states as discriminated unions. Details in [typescript.md](references/typescript.md). For a repository-wide audit or cleanup, read [typescript-audit.md](references/typescript-audit.md).

## Lint and type errors

Run the project's formatter, linter and type checker through its own scripts, and fix what they report in the code. A diagnostic is usually right, and the fix usually improves the code.

A suppression comment (`eslint-disable-next-line`, `@ts-expect-error`, `// biome-ignore`) is a last resort. It is legitimate when the rule genuinely misfires on correct code, for example a framework that requires a name the rule bans. When you use one, disable only the one rule on the one line, give the reason in the comment, and mention it to the user when you report the work, so it is a visible decision rather than a quiet one. Never use one to make a type error or a real bug go away, and never where the project forbids them.

Agents reach for suppressions to finish faster. These are the excuses to catch yourself on:

| Excuse | What is true |
| --- | --- |
| "The rule is too strict here." | Then the fix is usually a small restructure. If the rule really is wrong for this code, say so to the user; don't silence it quietly. |
| "The type is right, TypeScript just can't see it." | Then show it: narrow, parse, or annotate. An assertion or a suppression hides the place where the assumption breaks. |
| "It's only one line." | Each one-line exception teaches the next change that exceptions are fine. |
| "I'll fix it properly later." | Later doesn't come. Fix it now or tell the user it is left. |

Don't change the lint configuration, rename a public API, or export an internal just to get a clean run. A clean run doesn't prove behaviour survived, so check that too.

## The user's own projects

In projects the user owns (one you start together, one under their own account, or one that already vendors this skill's plugin), use their toolchain: oxfmt and oxlint with the Ultracite preset for JavaScript and TypeScript, and the [code-style oxlint plugin](oxlint/code-style/README.md), which enforces much of this skill. Never add these to a project the user doesn't own; a company's codebase has its own tools.

## Before you finish

- The formatter, linter and type checker pass through the project's scripts.
- New code follows the layout, control-flow and naming rules, including where nearby code doesn't.
- No helper exists only to be called once; no class exists only to hold static functions.
- Every error is handled or propagated; no placeholder data.
- Any suppression is one rule, one line, with a reason the user would accept.
- In TypeScript, every external value passes a check before the code relies on its shape.

For visual design, use the design skill. For a bug whose cause isn't obvious, use the diagnosing-bugs skill.
