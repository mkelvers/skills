# The user's own projects

Everything else in this skill applies in any codebase. This file adds what only belongs in projects the user owns: their toolchain and their lint rules. A company or third-party codebase has its own tools and rules; don't bring these in.

## Is this the user's project?

Treat a project as the user's own when any of these is true:

- the user is starting it with you;
- it already vendors the code-style oxlint plugin;
- its repository lives under the user's own account, not an organisation's;
- the user says so.

If none is true, it isn't. When unsure, ask once before adding tooling.

## Toolchain

For JavaScript and TypeScript, the user uses oxfmt and oxlint, with the Ultracite preset and the `correctness` category as errors, instead of Prettier, ESLint or Biome.

Configure oxfmt with tabs, double quotes, semicolons, trailing commas, a print width of 100, sorted imports and `objectWrap: "preserve"`, so expanded objects stay expanded.

## The bundled plugin

The skill's [oxlint plugin](../oxlint/code-style/) enforces the parts of this style a linter can see. In the user's projects it is on, with every rule as an error.

To add it:

1. Copy the folder into the repository, for example `vendor/oxlint/code-style/`.
2. Pin `@oxlint/plugins` to the installed oxlint version.
3. Add the folder to `jsPlugins` in the oxlint config and list the rules in the top-level `rules` (not in an override, which would scope them to one folder).
4. Make the lint script run a first pass with every rule off and `reportUnusedDisableDirectives: "error"`, so any disable comment fails.

Change rules in the skill first, then copy the folder into each project.

| Rule | Catches | Reference |
| --- | --- | --- |
| `expand-objects` | Two members of an object or type on one line. Has an autofix. | [formatting](formatting.md) |
| `named-conditions` | An `if`/`while` condition with more than two `&&`/`\|\|` operands. | [formatting](formatting.md) |
| `name-words` | Abbreviations, filler last words, `handle…` names. | [naming](naming.md) |
| `name-context` | A value or function repeating its folder or file name. | [naming](naming.md) |
| `name-length` | Names over three words. | [naming](naming.md) |
| `no-wrappers` | Functions that only forward their arguments to another call. | [structure](structure.md) |
| `no-module-let` | Module-level `let`/`var`. | [structure](structure.md) |
| `no-loose-functions` | Non-exported top-level functions; pushes helpers into the class that owns them, or inline. | [structure](structure.md) |
| `no-single-use-constants` | Module-level constants read once. | [structure](structure.md) |
| `no-swallowed-errors` | `catch` blocks and `.catch()` callbacks that drop the error. | [errors](errors.md) |
| `no-literal-fallback` | `?? "Unknown"` and similar placeholder text. | [errors](errors.md) |
| `no-suppressions` | Lint, format and type-check suppression comments. | [lint](lint.md) |

Some projects also enable oxlint's `no-ternary` and `typescript/consistent-type-assertions` (`assertionStyle: "never"`). When a project does, there are no ternaries and no `as` casts other than `as const`.
