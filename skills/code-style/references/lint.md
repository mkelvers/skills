# Lint and formatting tools

This file applies in every codebase. For projects the user owns, also read [own-projects.md](own-projects.md), which adds the user's own toolchain and lint rules.

## Use the project's tools

Run the project's formatter, linter and type checker through its own scripts and configuration. Format every file you touch, then lint and typecheck before calling the work done.

Don't add linters, plugins or rules to a project the user doesn't own, and don't change its configuration to match these references. The project's rules are part of its architecture. When this skill and the project's lint rules disagree, the lint rules win; the rest of this skill still applies to everything they leave open.

## Fix the code, not the check

**Always.** Don't add comments that switch a check off: `eslint-disable`, `oxlint-disable`, `@ts-ignore`, `@ts-nocheck`, `prettier-ignore`, `biome-ignore`, `svelte-ignore` and the like. Don't add a comment arguing the rule doesn't apply here either; that is a suppression with extra words.

If a rule is wrong for the code, say so and propose a configuration change as a separate decision. Don't edit the configuration, rename a public API, or export an internal just to get a clean run.

The routine exception: a negative type test may use `@ts-expect-error` with a reason, on the line before a statement that must fail to compile. A project that documents its own exceptions (a reviewed suppression format, for example) follows them.

## Reading a diagnostic

Before changing code for a diagnostic, read what the rule checks. Then make the smallest change that satisfies it without changing behaviour. A clean lint run doesn't prove behaviour survived: moving a value into a function, reordering statements or renaming an error class can all change it.
