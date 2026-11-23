# Skills

Shared agent skills for code style, TypeScript, debugging, design, and writing. Each skill starts at its own `SKILL.md` and links to detailed references.

Keep the checkout at a stable path. To link all skills and the shared `AGENTS.md` into Codex and Claude Code, run this from the repository root:

```sh
sh link.sh
```

The script refreshes symlinks and removes broken skill links into this checkout. It leaves regular files and directories in place and reports those paths as skipped.

To install just one skill, link its entire directory into your agent's skills directory instead. Keep any companion skills beside it so relative references work. Start a new agent session after linking.

Update the checkout with `git pull --ff-only`.

To uninstall, remove only the symlinks pointing into this checkout, including the linked instruction files. Remove the checkout after removing those links.
