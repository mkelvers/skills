# Errors, documentation, and review

❌ **Don't** catch a failing write, log it, and report success. Avoid placeholder defaults for required data and assertions that hide invalid input.

✅ **Do** catch at the boundary that can recover, translate, or explicitly report failure. Preserve the underlying cause when translating. Return the project's result type for expected outcomes callers branch on. Throw a meaningful error for exceptional failure. Observe asynchronous work the caller depends on.

Document assumptions, effects, ordering, ownership, and failure modes where they are part of the contract. Follow local requirements for exported documentation. Explain why a non-obvious decision exists and omit comments that merely narrate syntax.

Inspect the relevant diff and trace normal entry points, existing callers, older data, and failure paths. Verify with the project's formatter, lint, and appropriate checks. Add regression coverage when needed to prove a specific behavior. Distinguish static results, runtime behavior, and deployment verification. Report review findings with a location, evidence, and a correction.
