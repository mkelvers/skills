---
name: typescript
description: Guides writing, refactoring, reviewing, and auditing TypeScript code. Use when working on TypeScript or Node.js code, or when cleaning up or auditing a TypeScript repository.
---

# TypeScript

Write the smallest clear design that models the domain, enforces its invariants, and validates its boundaries. Types, names, and module structure should explain the code. Every abstraction earns its place.

## Rules

- Name each new layer's responsibility and consumer. If deleting it loses nothing but indirection, don't add it.
- Validate at trust boundaries (HTTP bodies, env vars, JSON, queues, webhooks, third-party APIs, CLI input). Accept `unknown` where the contract genuinely allows it. Narrow or validate before relying on its shape. Prefer the project's existing validator, including Zod where adopted, and derive runtime-data types from schemas. Avoid `any` for unchecked data.
- Use a concrete function or class when callers need only one implementation. Introduce a separate contract when callers depend on it independently or real implementations share it.
- Start generics concrete. Add one only to preserve a real relationship between types.
- Use classes for state, lifecycle, or invariants. Otherwise write functions. Constructors do no async work. Inherit only for a true is-a.
- Give database connections and transactions an explicit owner. Follow the project's existing connection model. A shared connection, a transaction-scoped client, or an injected pool can each serve a real lifetime or isolation requirement.
- Don't hide missing data with a fallback. `anime.title ?? "Unknown"` on a required field is a bug. Throw, or set defaults once in the schema or config parsing.
- Use TSDoc where exported APIs have assumptions, errors, side effects, or lifecycle requirements that their types do not express. Follow stricter local documentation rules.
- Style (control flow, naming, formatting, grouping) follows the `code-style` skill.

Treat SOLID, DRY, YAGNI, KISS, and separation of concerns as questions that expose trade-offs, not as a score. Citing a principle doesn't justify a refactor. Remove duplicated knowledge (the same rule in two places), not code that merely looks similar. Delete speculative options and abstractions for hypothetical consumers. Fewer lines is not simpler, and indirection is not architecture.

Prefer checked assignments, inference, and narrowing. Where project policy allows, a localized assertion may express an independently established invariant the compiler cannot see. An assertion does no runtime validation. Follow stricter local rules, including Sora's assertion ban.

## References

Read the file that matches the work, in `references/`.

- `api-design.md`: public API shape, abstractions, functions vs classes, constructors, inheritance.
- `types-and-interfaces.md`: interfaces, type aliases, schemas, `unknown`, generics, nullability.
- `documentation.md`: TSDoc.
- `errors-and-results.md`: throwing, causes, result types, defaults.
- `review.md`: reviewing a diff.
- `audit.md`, then `audit-tooling.md` as needed: auditing or cleaning up an existing repo.

Before finishing, ask whether someone reading only the public types and docs would know how to use this, and whether any part exists only because it looked like good architecture.
