#!/usr/bin/env python3
"""Checks a skill folder against the Agent Skills format.

Usage: python3 validate.py path/to/skill

Prints each problem and exits with status 1 when there is one.
"""

import re
import sys
from pathlib import Path


class Skill:
    """A skill folder and the problems found in it."""

    def __init__(self, folder: Path):
        self.folder = folder
        self.problems: list[str] = []

    def check(self) -> list[str]:
        entry = self.folder / "SKILL.md"

        if not entry.is_file():
            return [f"{entry} does not exist"]

        text = entry.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)

        if not match:
            return ["SKILL.md must start with frontmatter between two --- lines"]

        fields = self.fields(match.group(1))
        body = match.group(2)

        self.check_name(fields.get("name", ""))
        self.check_description(fields.get("description", ""))
        self.check_body(body)

        return self.problems

    def fields(self, frontmatter: str) -> dict[str, str]:
        found: dict[str, str] = {}

        for line in frontmatter.splitlines():
            match = re.match(r"^([a-z_-]+):\s*(.*)$", line)

            if match:
                found[match.group(1)] = match.group(2).strip().strip("\"'")

        return found

    def check_name(self, name: str) -> None:
        if not name:
            self.problems.append("frontmatter is missing name")
            return

        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
            self.problems.append(
                f"name {name!r} must be lowercase letters, digits and single hyphens, at most 64 characters"
            )

        if name != self.folder.resolve().name:
            self.problems.append(f"name {name!r} must match the folder name {self.folder.resolve().name!r}")

        if "anthropic" in name or "claude" in name:
            self.problems.append(f"name {name!r} uses a reserved word")

    def check_description(self, description: str) -> None:
        if not description:
            self.problems.append("frontmatter is missing description")
            return

        if len(description) > 1024:
            self.problems.append(f"description is {len(description)} characters; the limit is 1024")

        if "<" in description or ">" in description:
            self.problems.append("description must not contain < or >")

        if len(description) > 300:
            print(f"note: description is {len(description)} characters; one sentence is usually enough")

    def check_body(self, body: str) -> None:
        lines = len(body.splitlines())

        if lines > 500:
            self.problems.append(f"SKILL.md body is {lines} lines; keep it under 500 and move detail to references/")

        for link in re.findall(r"\]\(([^)#\s]+)", body):
            if "://" in link:
                continue

            if not (self.folder / link).exists():
                self.problems.append(f"link to {link} points to a file that does not exist")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: validate.py path/to/skill")

    problems = Skill(Path(sys.argv[1])).check()

    for problem in problems:
        print(f"error: {problem}")

    if problems:
        sys.exit(1)

    print("ok")
