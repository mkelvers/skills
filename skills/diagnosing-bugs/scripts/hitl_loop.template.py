#!/usr/bin/env python3
"""A reproduction loop the user follows by hand.

Copy this file, edit the steps in `main`, and run it with `python3`. The
agent runs the script; the user answers the prompts in their terminal.

Two helpers:
    step("instruction")         shows an instruction and waits for Enter
    capture("KEY", "question")  shows a question and records the answer

At the end, the answers are printed as KEY=VALUE lines for the agent to read.
Captured answers are printed back to the terminal, so capture observations
only, and leave signing in to the user as a step.
"""

answers: dict[str, str] = {}


def step(instruction: str) -> None:
    print(f"\n>>> {instruction}")
    input("    [Enter when done] ")


def capture(key: str, question: str) -> None:
    print(f"\n>>> {question}")
    answers[key] = input("    > ")


def main() -> None:
    # --- edit below -----------------------------------------------------

    step("Open the app at http://localhost:3000 and sign in.")
    capture("ERRORED", "Click the 'Export' button. Did it throw an error? (y/n)")
    capture("ERROR_MSG", "Paste the error message (or 'none'):")

    # --- edit above -----------------------------------------------------

    print("\n--- Captured ---")

    for key, value in answers.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
