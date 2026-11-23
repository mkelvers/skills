# Tooling playbook

Use project-installed tools and repository scripts first. Do not change dependency manifests merely to run an audit. If a useful tool is absent, either use an ephemeral package-runner command when network use is in scope or ask before installing it permanently.

## Repository discovery

```sh
git status --short
git log --oneline -30
git log --format= --name-only --since='6 months ago' | sed '/^$/d' | sort | uniq -c | sort -nr | head -40
rg --files -g 'package.json' -g 'tsconfig*.json' -g '*lock*' -g 'AGENTS.md' -g 'CLAUDE.md' -g 'CONTRIBUTING.md'
```

Interpret churn as a prioritization signal, not proof of poor design. Exclude generated files and vendored code.

## Existing quality gates

Inspect scripts before running them:

```sh
node -e 'console.log(require("./package.json").scripts ?? {})'
```

Run the repository's focused typecheck, lint, tests, and build. In a monorepo, begin with the affected workspace. Avoid silently substituting `npm` for the lockfile-selected package manager.

For compiler-performance investigations, use the existing TypeScript executable:

```sh
tsc --noEmit --extendedDiagnostics
```

## Dead code and dependency hygiene with Knip

Start with its normal project-aware analysis, then narrow or strengthen it:

```sh
knip
knip --include files,exports,types,dependencies,devDependencies,unlisted
knip --production --strict
knip --include cycles
```

Use the package-manager equivalent (`npm exec -- knip`, `pnpm exec knip`, `yarn knip`, or `bunx knip`) when Knip is installed locally. For an ephemeral run, use the package manager's one-shot runner only when downloads are allowed.

Before deleting anything, verify framework plugins, workspace entry points, dynamic imports, code generation, CLI binaries, package exports, reflection, test-only consumers, and downstream public consumers. Use Knip debug or trace facilities to investigate surprising reachability. Never start with `--fix`.

## Duplication with jscpd

Keep the first pass non-failing and write reports outside the repository or to an ignored temp directory:

```sh
jscpd src --min-tokens 50 --min-lines 5 --reporters console,json --output "${TMPDIR:-/tmp}/jscpd-report"
```

The current defaults are 50 tokens and 5 lines. Omit a nonzero `--exitCode` during exploration; introduce a CI threshold only after baselining and explicit agreement. Respect `.gitignore`; additionally exclude generated output, snapshots, fixtures, migrations, and intentional protocol/schema repetition as appropriate.

Treat clones as review leads. Abstract only when they represent the same knowledge and should change together.

## Dependencies and cycles

Use Knip's cycle report for a quick pass. If dependency-cruiser is already configured, run the repository's rule set and preserve its TypeScript resolution:

```sh
depcruise --validate .dependency-cruiser.cjs --ts-config tsconfig.json src
```

Adapt the config filename and source roots to the repository. Use `--ts-pre-compilation-deps` when type-only or pre-emit dependencies matter. Do not generate or overwrite dependency-cruiser configuration during an audit.

## Complexity

Prefer existing ESLint complexity or cognitive-complexity rules because they understand the repository's parser and ignores. If ESLint is configured but no threshold exists, a temporary CLI rule can identify review candidates:

```sh
eslint src --rule 'complexity: [warn, 12]'
```

Treat `12` as a triage starting point, not a universal quality bar. Also inspect deeply nested control flow, large unions and conditional types, typecheck diagnostics, error-path branching, and high-churn functions. Complexity is acceptable when it is cohesive and well-tested; splitting it into many shallow functions can make locality worse.

## Search probes

Adapt these to repository conventions:

```sh
rg -n '\bany\b|@ts-ignore|@ts-expect-error|eslint-disable' --glob '*.{ts,tsx,mts,cts}'
rg -n 'TODO|FIXME|HACK|XXX' --glob '*.{ts,tsx,js,jsx,mjs,cjs}'
rg -n 'throw new Error|console\.(log|warn|error)' --glob '*.{ts,tsx,js,jsx,mjs,cjs}'
```

Every match needs context. Suppressions can be justified, and logs or generic errors can be correct at infrastructure boundaries.

## Primary documentation

- Knip: <https://knip.dev/>
- dependency-cruiser: <https://github.com/sverweij/dependency-cruiser>
- jscpd: <https://github.com/kucherenko/jscpd>
