# code-style oxlint plugin

Lint rules for the parts of the code-style skill a linter can check. This is for the user's own JavaScript and TypeScript projects. Don't add it to a codebase they don't own.

## Setup

1. Copy this folder into the project, for example to `vendor/oxlint/code-style/`.
2. Install `@oxlint/plugins` at the same version as `oxlint`.
3. In the oxlint config, add the folder's `index.ts` to `jsPlugins`, and list the rules in the top-level `rules` at `"error"`. Rules inside an `overrides` entry only apply to the files that entry matches.
4. Optionally, make the lint script run a first pass with every rule off and `reportUnusedDisableDirectives: "error"`. Every disable comment then fails, for projects that allow no suppressions at all.

The skill holds the original. Change a rule there, then copy the folder into each project.

## Rules

| Rule | Reports | Skill reference |
| --- | --- | --- |
| `expand-objects` | Two members of an object or type on one line. Autofixes; run the formatter after. | formatting |
| `named-conditions` | An `if`/`while` condition with more than two `&&`/`\|\|` operands. | formatting |
| `name-words` | Abbreviations, filler last words, `handle…` names. | naming |
| `name-context` | A value or function that repeats its folder or file name. | naming |
| `name-length` | Names of more than three words. | naming |
| `no-wrappers` | Functions that only forward their arguments to another call. | structure |
| `no-module-let` | Module-level `let` or `var`. | structure |
| `no-loose-functions` | Non-exported top-level functions. Strict: pushes every helper inline or into a class. | structure |
| `no-single-use-constants` | Module-level constants read once. Strict. | structure |
| `no-swallowed-errors` | `catch` blocks and `.catch()` callbacks that drop the error. | errors |
| `no-literal-fallback` | `?? "Unknown"` and similar placeholder text. | errors |
| `no-suppressions` | Every lint, format and type-check suppression comment. Strict: for projects that allow none. | SKILL.md |

Svelte component scripts are exempt from the rules that would misread per-instance state.
