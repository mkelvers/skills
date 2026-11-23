---
name: diagnosing-bugs
description: Diagnoses bugs by building a pass/fail feedback loop before theorizing. Use when the user reports something broken, throwing errors, failing, flaky, or slow, or asks to debug or diagnose an issue.
---

# Diagnosing bugs

The feedback loop is the skill. With a fast, deterministic command that goes red on this exact bug, you will find the cause. Without one, reading code will not save you. Read `CONTEXT.md` and any ADRs for the area first. Skip a phase only with a stated reason.

Redact every secret as `<REDACTED>` before showing commands, output, or captured artifacts. Keep credentials in env vars, and quote only the lines of a captured request that carry the signal. If redacted output is not enough to diagnose, say so and ask.

## 1. Build the loop

Pick the cheapest signal that reaches the bug:

1. A failing test at the seam that reaches it.
2. A curl or HTTP script against the dev server.
3. A CLI run on a fixture, diffed against a known-good snapshot.
4. A Playwright script that asserts on DOM, console, or network.
5. A captured request or event log, replayed through the code path.
6. A throwaway harness that calls the suspect function with mocked dependencies.
7. A fuzz loop of 1000 random inputs, for "sometimes wrong output".
8. A `git bisect run` script or old-vs-new diff, when the bug appeared between two known states.
9. Last resort: a script that drives the user through the manual steps, `scripts/hitl-loop.template.sh`.

Then tighten it: faster (narrow scope, cache setup), sharper (assert the specific symptom, not "didn't crash"), more deterministic (pin time, seed RNG, freeze network). For a non-deterministic bug, raise the reproduction rate instead of chasing a clean repro. Loop the trigger 100 times, add stress, narrow timing windows. A 50% flake is debuggable, 1% is not.

This phase is done when one command that you have already run (show it, redacted) is red-capable (asserts the user's exact symptom), deterministic, fast, and runnable unattended. If you are reading code to build a theory before that command exists, stop. If you cannot build a loop, list what you tried and ask for access to a reproducing environment, a redacted artifact (HAR, log, core dump), or permission to add temporary production instrumentation. Do not hypothesize without one.

## 2. Reproduce and minimise

Run the loop and confirm it shows the user's failure, not a nearby one. Then cut inputs, callers, config, and steps one at a time, rerunning after each cut. Stop when removing any remaining element turns the loop green.

## 3. Hypothesise

Write 3 to 5 ranked hypotheses before testing any. Each states a prediction: "if X is the cause, changing Y makes the bug disappear." A hypothesis with no prediction gets sharpened or dropped. Show the list to the user before testing, since they may know a recent deploy or a ruled-out cause. Proceed on your ranking if they are away.

## 4. Instrument

Each probe maps to one prediction, and you change one variable at a time. Prefer a debugger or REPL over logs, and targeted logs over "log everything and grep". Prefix every debug log with a unique tag such as `[DEBUG-a4f2]` so cleanup is one grep. For performance regressions, measure a baseline (timing harness, profiler, query plan) and bisect, because logs mislead there.

## 5. Fix and lock it down

Write the regression test before the fix, but only at a seam that exercises the real bug pattern at the call site. A single-caller unit test for a multi-caller bug gives false confidence. If no correct seam exists, that is a finding. Report it, because the architecture is preventing the bug from being locked down. With a seam: turn the minimised repro into a failing test, watch it fail, fix, watch it pass, then rerun the phase 1 loop on the original scenario.

## 6. Clean up

Grep for the debug tag and remove every hit. Delete throwaway prototypes. State the confirmed cause in the commit or PR message.
