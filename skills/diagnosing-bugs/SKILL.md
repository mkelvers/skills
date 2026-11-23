---
name: diagnosing-bugs
description: Diagnoses bugs by building a failing check before theorising; use when something is broken, erroring, failing, flaky or slow, or the user asks to debug.
---

# Diagnosing bugs

Find the cause by first building a command that fails on this exact bug, then using it to test one idea at a time. With a fast, reliable signal you will find the cause. Without one, reading code and guessing tends to produce a plausible story and a fix that doesn't hold.

Before starting, read the project's context notes (`CONTEXT.md`, architecture decision records) for the area. Skip a phase below only when you can say why it doesn't apply.

Redact secrets as `<REDACTED>` in every command, output and captured artifact you show. Keep credentials in environment variables, and quote only the lines of a captured request that carry the signal. If the redacted output isn't enough to diagnose, say so and ask.

## 1. Build the loop

Pick the cheapest signal that reaches the bug:

1. A failing test at the point in the code where the bug shows up.
2. A curl or HTTP script against the dev server.
3. A CLI run on a fixture, diffed against known-good output.
4. A browser script that asserts on the DOM, console or network.
5. A captured request or event log, replayed through the code path.
6. A small harness that calls the suspect function with stubbed dependencies.
7. A fuzz loop over many random inputs, for "sometimes the output is wrong".
8. A `git bisect run` script, when the bug appeared between two known versions.
9. Last resort: a script that walks the user through manual steps, [scripts/hitl-loop.template.sh](scripts/hitl-loop.template.sh).

Then improve it. Make it faster by narrowing scope and caching setup. Make it sharper by asserting the user's specific symptom, not "didn't crash". Make it deterministic by pinning time, seeding randomness and freezing the network. For a bug that only happens sometimes, raise the reproduction rate instead of waiting for a clean repro: run the trigger a hundred times, add load, narrow timing windows. A bug that fails half the time can be debugged; one that fails once in a hundred can't.

The phase is done when you have run one command (show it, redacted) that asserts the user's exact symptom, gives the same answer every time, runs fast, and needs nobody watching. If you notice yourself reading code to build a theory before that command exists, stop and finish the loop.

If you can't build one, list what you tried and ask for access to an environment that reproduces it, a redacted artifact (HAR file, log, core dump), or permission to add temporary instrumentation in production. Don't move on to theories without a loop.

## 2. Reproduce and reduce

Run the loop and confirm it shows the user's failure, not a different one nearby. Then remove inputs, callers, configuration and steps one at a time, rerunning after each. Stop when removing anything else makes the loop pass. The smaller the case, the fewer places the cause can hide.

## 3. Hypothesise

Write three to five ranked hypotheses before testing any. Each makes a prediction: "if X is the cause, changing Y makes the bug disappear." A hypothesis without a prediction can't be tested; sharpen it or drop it. Show the list to the user before testing, since they may know about a recent deploy or something already ruled out. If they're away, go ahead in your order.

## 4. Instrument

Make each probe test one prediction, and change one thing at a time, so a result points at one cause. Prefer a debugger or REPL to logs, and targeted logs to logging everything. Prefix every debug log with a unique tag such as `[DEBUG-a4f2]`, so removing them later is a single search. For performance problems, measure a baseline first (a timing harness, a profiler, a query plan) and bisect against it; logs mislead there.

## 5. Fix and lock it in

Write the regression test before the fix, at a point in the code that exercises the real bug the way callers hit it. A test of one caller doesn't protect against a bug with several. If no such point exists, report that as a finding: the design is preventing the bug from being locked down.

When there is one, turn the reduced case into a failing test, watch it fail, fix the code, watch it pass, then rerun the original loop from phase 1.

## 6. Clean up

Search for the debug tag and remove every hit. Delete throwaway harnesses. State the confirmed cause in the commit or pull request message.

## When not to use this

A typo, a failing type check with an obvious message, or a bug whose cause is already stated in the error doesn't need a loop. Fix it, and confirm with the check that reported it.
