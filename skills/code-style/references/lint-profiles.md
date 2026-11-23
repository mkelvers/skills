# Opt-in lint profiles

The bundled [Oxlint rules](../oxlint/code-style/) are available for projects that choose stricter enforcement. They include project preferences such as a name-length cap and limits on private module-level functions. Those checks are a profile choice.

Sora already vendors its chosen rules and anti-slop. Its existing local policy continues to apply, including its ternary, assertion, and helper restrictions. A shared prose change does not require resyncing any vendored copy.

When opting a project into custom lint, inspect the individual rules, match the plugin package version to the project's Oxlint version, and verify the configured subset. Keep the project config, rule source, and rule tests aligned. Use the existing project checks rather than silently replacing them. Change lint policy explicitly and separately from a feature or fix.
