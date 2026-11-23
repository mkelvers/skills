---
name: code-style
description: Apply the user's code style when writing, editing, refactoring, or reviewing code in any language. Covers readable formatting, explicit control flow, naming, ownership, errors, and verification.
---

# Code style

Find the nearest comparable code and check the project's instructions, formatter, and lint rules. Follow them in an existing project. Use the formatting below as the house style where the project leaves room, including new projects. Keep any stricter project profile in force.

- Expand multi-property objects and object-shaped union variants. Name meaningful intermediate steps and separate guards, work, and results with blank lines.
- Prefer explicit branches for work. A simple ternary may select between two clear values where the project allows it.
- Keep domain rules with their owners. Use names that read accurately at the call site. Use functions for stateless operations and classes when object semantics earn their place.
- Handle failures where the code can act on them. Keep external input untrusted until validated. Preserve existing caller contracts unless the task changes them.
- Run the relevant project checks. Fix diagnostics in code or identify the exact policy conflict. Treat a rule change as a separate, explicit decision.

## References

Read the sections that match the work.

- [Formatting and control flow](references/formatting.md) for objects, spacing, branches, and intermediate values.
- [Naming](references/naming.md) for identifiers, ownership at call sites, and domain terms.
- [Modules and state](references/ownership.md) for private functions, classes, dependency direction, and lifecycle.
- [Errors and review](references/review.md) for error handling, documentation, and verification.
- [Operational correctness](references/operations.md) for changes to network, service, data, or security boundaries.
- [Opt-in lint profiles](references/lint-profiles.md) for projects that deliberately adopt custom enforcement.

For TypeScript, also use the [TypeScript skill](../typescript/SKILL.md).
