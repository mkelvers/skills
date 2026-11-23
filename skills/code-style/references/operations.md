# Operational correctness

Use the sections that reach the changed code. Identify the obligation first, then choose a mechanism that satisfies it.

- **Concurrent writes and jobs.** Identify who owns work and which invariants must survive concurrent execution, retries, duplicate delivery, and restart. Use transactions for writes that must commit together, constraints or conditional updates for competing writers, and deduplication or reconciliation for effects outside the transaction. Verify the relevant failure path.
- **Network calls.** Set a deadline and define cancellation where supported. Bound retries by attempts and total time, respect rate limits, and use backoff with jitter when clients could retry together. Retry only eligible failures for operations safe to repeat or with receiver-side deduplication. Define how partial results and invalid responses reach callers.
- **Public contracts and persistence.** Treat identifiers, pagination order, cursors, error shapes, and serialization as contracts. Specify units, time zones, precision, and absence semantics where they matter. Account for old clients and overlapping deployments, keep applied migration history intact, and verify recovery where it matters.
- **Security boundaries.** Validate input, authenticate the caller where needed, and authorize each requested action on the specific resource. Parameterize SQL, encode HTML for its output context, and pass structured process arguments without a shell where possible. Apply a destination policy to server-side fetches, including redirect destinations. Check CSRF when browsers attach credentials automatically. Bound caller-controlled cost and keep secrets out of diagnostics. Prevent unintended opener access and choose referrer policy separately.
- **Configuration and lifecycle.** Validate required configuration at startup, document precedence, and define readiness and liveness where needed. Stop accepting work on shutdown, drain or safely release work within a deadline, and close owned resources. Provide useful correlation for failures and account for secret rotation.
- **Interactive UI.** Check accessible names, keyboard behavior, focus movement and restoration, and status announcements for the changed flow. Use automated checks alongside direct interaction.

Before adding a mechanism, state what it will cost to maintain, migrate, and undo in a year.
