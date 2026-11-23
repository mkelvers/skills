# Auditing a TypeScript codebase

Read this for a repository-wide audit or cleanup, not for an ordinary change.

Improve the system, not its cosmetic score. Establish trustworthy baselines, gather evidence with several independent signals, prioritize change hotspots, and refactor in small verified slices. Treat tool output as leads to investigate, never as permission to delete or abstract code.

When an audit turns up a real bug or a performance regression, switch to the diagnosing-bugs skill for that issue before continuing.

## 1. Establish the contract

1. Read `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `CONTEXT.md`, relevant ADRs, and package-level instructions.
2. Inspect `git status` and preserve unrelated work. Never normalize or rewrite unrelated files.
3. Identify the package manager, workspaces, runtime and TypeScript versions, framework conventions, entry points, generated files, and public package surfaces.
4. Read `package.json` scripts and CI configuration. Use the repository's own commands before inventing substitutes.
5. Define the requested scope. If broad, weight recently changed and frequently co-changing paths before untouched stable code.

Record the baseline commands and results. A refactor is not proven safe without a before-and-after comparison.

## 2. Build an evidence map

Run the cheapest signals first, using only what the repository and machine already have: the project's scripts, git, `rg` and the TypeScript compiler. Don't add audit tools or change the dependency manifest for an audit. `tsc --noEmit --noUnusedLocals --noUnusedParameters` lists unused code without touching the config, and an export whose name `rg -w` finds only in its own file is a candidate for removal once framework conventions and public consumers are ruled out. Files that change often (from `git log`) are where cleanup pays off.

Collect evidence for:

- existing typecheck, lint, test, build, and formatting gates;
- unused files, exports, types, dependencies, and unresolved imports;
- dependency cycles and imports that bypass intended package entry points;
- exact and structural duplication;
- cyclomatic or cognitive complexity, nesting, oversized functions, and high-churn files;
- unsafe TypeScript escape hatches such as unjustified `any`, assertions, ignored errors, or ambiguous unions;
- flaky, slow, weak, or missing tests at important seams;
- repeated business rules, scattered invariants, pass-through modules, and change coupling.

Separate findings into:

- **Confirmed defect**: demonstrated incorrect behavior or violated repository rule.
- **Measured risk**: a maintainability or architecture problem shown by a command, with concrete impact.
- **Suspected smell**: a review lead requiring semantic inspection.
- **False positive / intentional**: dynamic entry point, public export, generated code, framework convention, or accepted trade-off.

Never present raw command output as a final diagnosis.

## 3. Inspect semantics and architecture

Treat SOLID, DRY, YAGNI and KISS as questions, not rules.

For every serious candidate:

1. Trace callers, data flow, side effects, error modes, and tests.
2. State the maintenance problem in concrete terms: what change is hard, what knowledge is duplicated, or what bug class escapes.
3. Apply the deletion test to wrappers and abstractions. If deletion only moves complexity to callers, the module may be earning its keep.
4. Distinguish textual duplication from duplicated knowledge. Similar-looking code can encode different reasons to change.
5. Prefer cohesion and locality over arbitrary file-size or function-length thresholds.
6. Check whether the proposed seam has real variation. Do not add an interface for a single hypothetical implementation.
7. Check public compatibility, runtime behavior, performance characteristics, and framework discovery before recommending deletion or movement.

## 4. Prioritize a bounded portfolio

Rank candidates by evidence, user impact, change frequency, blast radius, expected leverage, and verification quality. Present a short list with:

- evidence and exact locations;
- why it matters;
- proposed change and explicit non-goals;
- confidence, risk, and estimated effort;
- the command or test that proves success.

Prefer removing dead or redundant structure before introducing abstractions. Prefer one high-confidence slice over a repository-wide cleanup campaign.

## 5. Refactor safely

For each accepted slice:

1. Establish a focused behavioral test or other red-capable feedback loop.
2. Make one coherent structural change.
3. Run the narrowest relevant checks immediately.
4. Inspect the diff for accidental churn and scope expansion.
5. Re-run the broader repository gates proportional to risk.
6. Re-run the check that motivated the change and confirm the targeted signal improved without new failures.

Do not auto-fix or bulk-delete findings. Do not add packages, permanent configuration, CI gates, or new architectural policy unless the user requested that change. Do not commit unless the user requested a commit.

## 6. Finish with evidence

Report:

- what changed and why;
- which smells were confirmed, rejected, or deferred;
- before-and-after measurements where meaningful;
- exact validation commands and outcomes;
- remaining risks and the next highest-leverage candidate.

A cleaner diff is not success if behavior, public compatibility, or developer workflow regressed.
