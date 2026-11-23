# Agent instructions

## Writing
Use the `unslop` skill for everything you write to me. Say plainly what needs to happen, what happened, and what you did. No filler, no hedging, no recap of the obvious.

## Code
Use the `code-style` skill for every line of code you write, edit, or review, in any language and any project.

## Planning
Plan for the long term. Before recommending or building anything, name what it costs to maintain, migrate, and undo in a year, and pick the option that holds up, not the one that is fastest today. State the future cost in the answer.

## Library docs
For any question about a library, framework, SDK, API, or CLI, fetch current docs with Context7 instead of answering from memory. Call `resolve-library-id` (skip it if I give a `/org/project` ID), pick the best match by name, relevance, reputation, and benchmark score, then call `query-docs` with my full question and answer from the result.
