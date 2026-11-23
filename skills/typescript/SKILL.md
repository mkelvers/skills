---
name: typescript
description: Guides the design of TypeScript code; use when writing, reviewing or auditing TypeScript or Node.js, or designing its types, APIs, errors or docs.
---

# TypeScript

Write the smallest design that models the domain, keeps its invariants true, and checks everything that comes from outside. A reader should understand the code from its types, names and module structure, and every abstraction should be there because something would be lost without it.

The project's conventions win: its validator, its error model, its connection handling, its rules on assertions. For layout, naming, helpers and classes versus functions, use the [code-style skill](../code-style/SKILL.md). This skill covers what is particular to TypeScript.

## The rules

**Check data at the boundary, then trust it.** Request bodies, environment variables, JSON, queue messages, webhooks and third-party responses are `unknown` until a schema or a check proves their shape. Parse them once where they enter, with the project's validator, and derive the type from the schema. After that, business logic works with real types and never re-checks. A cast at the boundary proves nothing, because the sender decides what arrives.

**Let the compiler see the evidence.** Prefer inference, narrowing and annotated assignments to assertions. An assertion does no checking at runtime; it only stops the compiler from telling you that you're wrong. Where the project allows one, limit it to an invariant established elsewhere that the compiler can't follow.

**Make invalid states impossible to write.** Model a result as a discriminated union, where each state carries only its own fields, rather than one object with many optional ones. A field that must exist after creation should be required by construction, not nullable "just in case".

**Add a layer only when it does a job.** Before adding an interface, wrapper, factory or generic, name what it owns and who depends on it. One implementation needs no separate interface. A generic needs a real relationship between types. If deleting the layer loses nothing but indirection, don't add it.

**Give owned resources an owner.** Connections, transactions, timers and subscriptions belong to something with a clear lifetime that also releases them. Follow the project's model for this.

**Document what the types can't say.** Assumptions, side effects, failure modes, ownership and lifecycle go in TSDoc on exported code. A doc comment that only repeats the name is noise.

Treat principles like SOLID, DRY and YAGNI as questions that expose trade-offs, not as a score. Citing one doesn't justify a refactor. Remove duplicated *knowledge*, the same rule in two places, not code that merely looks alike.

## References

Read the one that matches the work.

| Working on | Read |
| --- | --- |
| A public API, abstractions, interfaces, constructors, inheritance | [api-design.md](references/api-design.md) |
| Types, unions, schemas, `unknown`, generics, nullability | [types.md](references/types.md) |
| Errors, causes, result types, defaults | [errors.md](references/errors.md) |
| TSDoc and doc comments | [documentation.md](references/documentation.md) |
| Auditing or cleaning up a whole repository | [audit.md](references/audit.md), with [audit-tooling.md](references/audit-tooling.md) for the commands |

## Reviewing a diff

Flag only what you can point at, with `file:line`, the rule it breaks and the fix. Look in particular for:

- layers with no job: forwarding wrappers, `Foo` with a lone `FooImpl`, factories where `new` would do, generics with one use;
- unchecked input: casts from parsed JSON, an interface duplicating a schema, data used before validation;
- hidden invalid state: defaults on required data, swallowed errors, lost `cause`, thrown strings;
- resources with no clear owner or lifetime;
- exported contracts whose obligations aren't documented.

## Before you finish

- Could someone reading only the public types and docs use this correctly?
- Does any part exist only because it looked like good architecture?
- Does every external value pass a check before the code relies on its shape?
