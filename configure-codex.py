"""Apply personal skill preferences while preserving other Codex configuration."""

import json
from pathlib import Path
import re
import sys


def configure(config, system_skills):
    text = config.read_text() if config.exists() else ""
    start = "# BEGIN personal skill preferences"
    end = "# END personal skill preferences"
    text = re.sub(r"(?m)^" + re.escape(start) + r"\n.*?^" + re.escape(end) + r"\n?", "", text, flags=re.S)

    # Leave bundled files in place so application updates cannot undo file deletions.
    entries = []
    for name in ("openai-docs", "skill-creator", "skill-installer"):
        path = system_skills / name / "SKILL.md"
        entries.append('[[skills.config]]\npath = ' + json.dumps(str(path)) + '\nenabled = false')

    for name in ("pdf", "documents", "presentations", "spreadsheets", "template-creator"):
        header = '[plugins."' + name + '@openai-primary-runtime"]'
        pattern = r"(?m)^" + re.escape(header) + r"[^\n]*\n(?:(?!^\[).)*"
        match = re.search(pattern, text, flags=re.S)
        if match:
            section = match.group()
            if re.search(r"(?m)^enabled\s*=", section):
                updated = re.sub(r"(?m)^enabled\s*=.*$", "enabled = false", section)
            else:
                updated = section.rstrip() + "\nenabled = false\n\n"
            text = text[:match.start()] + updated + text[match.end():]
        else:
            entries.append(header + "\nenabled = false")

    result = text.rstrip() + "\n\n" + start + "\n" + "\n\n".join(entries) + "\n" + end + "\n"
    config.parent.mkdir(parents=True, exist_ok=True)
    if result != (config.read_text() if config.exists() else ""):
        config.write_text(result)


if __name__ == "__main__":
    configure(Path(sys.argv[1]), Path(sys.argv[2]))
