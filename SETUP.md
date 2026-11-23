# Set up the skills

Clone this repository to a stable location. Keep each skill directory intact so references remain available. Local project instructions and lint rules govern work within that project.

```sh
git clone https://github.com/mkelvers/skills.git
cd skills
```

## Link one skill

Choose the destination supported by your agent. These examples install `code-style` for Codex and Claude Code. Link its TypeScript companion too if you work in TypeScript.

```sh
mkdir -p "$HOME/.codex/skills" "$HOME/.claude/skills"
ln -s "$PWD/skills/code-style" "$HOME/.codex/skills/code-style"
ln -s "$PWD/skills/code-style" "$HOME/.claude/skills/code-style"
```

Run the commands from the clone root. If a destination exists, inspect it before making a replacement. For a project-local installation, link or copy the entire skill directory into the project's supported discovery path. If a skill points to another skill, install that companion beside it as well. Keep the clone outside the project if you want updates to flow through symlinks without committing the skill source into the project.

Open a new agent session after linking. Verify that the skill appears and can open a referenced file.

## Use the full personal setup

The dotfiles checkout pins this repository at `agents/`. From the dotfiles root, initialize it first.

```sh
git submodule update --init -- agents
sh agents/link.sh
```

Use `sh link.sh` from a standalone clone for the same full setup. The script needs Python 3. It links all skills and personal instructions into Codex and Claude Code, refreshes symlinks at those paths, and applies personal plugin and skill preferences to the Codex configuration. Use the single-skill procedure if you only want the skill content.

## Update or remove

In a standalone clone, run `git pull --ff-only` when you want the latest version. In the dotfiles checkout, run the submodule update command after updating dotfiles to get its pinned version. To intentionally advance the pin, check out the intended skills commit in `agents/` and commit the updated pointer in dotfiles.

To remove a skill, inspect its link with `readlink` and remove that link if it points into this checkout. If you used the full installer, also review the linked instruction files and restore your prior Codex preferences if desired. Remove the clone only after removing any links you still rely on.
