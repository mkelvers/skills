#!/usr/bin/env python3
"""Links every skill in this checkout, and the shared instructions, into Claude Code and Codex.

Usage: python3 link.py

Existing files that aren't symlinks are left alone. Broken links that point
into this checkout, left behind by a removed skill, are deleted.
"""

import sys
from pathlib import Path

here = Path(__file__).resolve().parent
home = Path.home()


def link(target: Path, path: Path) -> None:
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    if path.exists() and not path.is_symlink():
        print(f"skip (exists, not a symlink): {path}", file=sys.stderr)
        return

    if path.is_symlink():
        path.unlink()

    path.symlink_to(target)


def sync(directory: Path) -> None:
    for skill in sorted((here / "skills").iterdir()):
        if (skill / "SKILL.md").is_file():
            link(skill, directory / skill.name)

    for entry in directory.iterdir():
        stale = entry.is_symlink() and not entry.exists()

        if stale and (here / "skills") in entry.resolve().parents:
            entry.unlink()


if __name__ == "__main__":
    sync(home / ".claude" / "skills")
    sync(home / ".codex" / "skills")

    link(here / "AGENTS.md", home / ".claude" / "CLAUDE.md")
    link(here / "AGENTS.md", home / ".codex" / "AGENTS.md")
