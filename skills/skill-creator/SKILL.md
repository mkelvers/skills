---
name: skill-creator
description: Creates a new agent skill from a short interview; use when the user wants to make, start or scaffold a skill.
---

# Skill creator

Turn what the user knows into a small, working skill: a folder with a `SKILL.md` that an agent loads at the right moment and then follows. Aim for something the size of a focused writing or review skill, not a large multi-reference system. A first version that works and gets improved through use beats a long one that was never tested.

## 1. Interview

Ask a few questions, in one message, and wait for the answers. Skip any the user has already answered.

1. **What should the agent do differently with this skill?** One or two sentences.
2. **When should it kick in?** The requests, file types or moments that should trigger it, and any that look similar but shouldn't.
3. **Show me an example.** A real request and what a good result looks like. If there is a bad result they keep getting, that is even more useful.
4. **What are the rules?** The things the agent gets wrong without the skill, and why each one matters.
5. **Where should it live?** In the user's personal skills (every project), or in this repository (only here, shared with whoever clones it).

If an answer is thin, ask one follow-up about it rather than guessing. The skill can only be as specific as what the user tells you, and the agent that reads it already knows everything general. What it needs is what is particular to this user.

## 2. Write the frontmatter

```yaml
---
name: reviewing-migrations
description: Reviews database migrations for safety; use when a change adds or edits a migration file.
---
```

**`name`:** lowercase letters, digits and single hyphens, at most 64 characters, and identical to the folder name. Prefer an action (`reviewing-migrations`, `writing-commits`) or a plain noun (`code-style`). Avoid vague words (`helper`, `utils`, `tools`) and the reserved words `anthropic` and `claude`.

**`description`:** one sentence that says what the skill does and when to use it, in the third person. It is the only part of the skill an agent sees before deciding whether to load it, so put the trigger words a user would actually say up front. When many skills are installed, agents shorten long descriptions, so a short one survives intact. Keep it well under the 1,024-character limit, and leave out `<` and `>`.

```text
❌ Helps with documents.                     → no trigger; the agent can't tell when it applies
❌ I can help you write better commits.      → first person, and "better" says nothing
✅ Writes commit messages from the staged diff; use when the user asks to commit or describe changes.
```

A skill that should run on every response or every code change can say so directly ("Always trigger whenever the AI writes a response to the user."). A skill that should only run when the user asks for it by name needs a tool-specific flag instead; see [references/frontmatter.md](references/frontmatter.md).

## 3. Write the body

Start from [assets/SKILL.template.md](assets/SKILL.template.md). Keep the body short, ideally under 150 lines for a simple skill and never over 500.

- **Open with one sentence** that states the goal the agent is working toward.
- **Give every rule its reason.** An agent that knows why a rule exists applies it sensibly to cases the rule didn't foresee. A bare "NEVER" in capitals gets followed rigidly or not at all.
- **Show, don't only tell.** A short ❌/✅ pair with a one-line comment saying what is wrong and what is right teaches more than a paragraph.
- **Say when a rule doesn't apply.** Name the exceptions and who decides (the project, the user).
- **Leave out what any capable agent already knows.** Every line costs context on every use. Keep what is specific to this user, their projects or their taste.
- **Use the imperative,** addressed to the agent: "Read the diff first", not "The agent should read the diff".
- **End with a short checklist** when the skill produces something checkable.

## 4. Add files only when they earn it

A simple skill is one `SKILL.md`. Add more only for a concrete reason:

- **`references/`** for detail the agent needs only sometimes, such as a long rule list or per-language notes. Link each file from `SKILL.md` with a line saying when to read it, and keep links one level deep (references don't point to more references).
- **`scripts/`** for work that must be done exactly the same way every time, like validation or generating a file. Run every script yourself before finishing.
- **`assets/`** for files the skill copies into its output, such as templates.

The user's own skills also carry `agents/openai.yaml`, which sets how the skill is shown in Codex:

```yaml
interface:
  display_name: "Reviewing migrations"
  short_description: "Review migrations for safe deploys"
```

Quote the values, and keep `short_description` between 25 and 64 characters.

## 5. Put it in place

- **Personal skill:** if the user keeps a skills repository (for example `~/.config/agents/skills/`, linked into each agent by a `link.sh` script), create the folder there and run the link script. Otherwise use `~/.claude/skills/<name>/` for Claude Code and `~/.agents/skills/<name>/` for Codex.
- **Project skill:** `.claude/skills/<name>/` for Claude Code, `.agents/skills/<name>/` for Codex.

Check before writing that no skill with the same name already exists there. Then validate the skill:

```sh
python3 scripts/validate.py path/to/skill
```

## 6. Try it

Give the user two or three realistic requests that should trigger the skill, and one that looks similar but shouldn't. Ask them to try these in a new session, since skills are discovered when a session starts (Claude Code also picks up edits live). If the skill doesn't trigger, the description is the first thing to fix. If it triggers but the result is wrong, fix the body.

## Before you finish

- The folder name and `name` match, and the validator passes.
- The description is one sentence with real trigger words.
- Every rule in the body says why.
- Nothing in the body is general knowledge the agent already has.
- The user knows how to try it.
