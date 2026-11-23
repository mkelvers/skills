# Optional frontmatter and per-tool settings

Read this when a skill needs to control how or when it runs. Most skills need none of it.

## The open standard

Any tool that supports Agent Skills accepts these fields beside `name` and `description`:

- `license`: a license name, or the name of a license file in the skill folder.
- `compatibility`: what the skill needs to run (a product, system packages, network access), up to 500 characters.
- `metadata`: a map of extra string keys and values.
- `allowed-tools`: tools the skill may use without asking, for example `Bash(git:*) Read`. Support varies by tool.

## Claude Code

Claude Code also reads these. Other Claude surfaces (claude.ai uploads, the API) reject them, so use them only for skills that live in Claude Code.

- `disable-model-invocation: true`: only the user can run the skill, by typing `/name`. Use it for skills with side effects, such as deploying or sending messages.
- `user-invocable: false`: hides the skill from the `/` menu, so only Claude decides when to load it.
- `argument-hint: "[issue-number]"`: shown when the user types `/name`. The arguments arrive in the body as `$ARGUMENTS`.
- `when_to_use`: extra trigger text appended to the description.
- `paths`: glob patterns; the skill only activates for matching files.
- `context: fork`: runs the skill in a separate subagent.
- `model`, `effort`: the model or reasoning effort for the turn the skill runs in.

Run a bundled script from any directory with `${CLAUDE_SKILL_DIR}/scripts/name.py`.

## Codex

Codex reads `agents/openai.yaml` in the skill folder:

```yaml
interface:
  display_name: "Reviewing migrations"
  short_description: "Review migrations for safe deploys"
  default_prompt: "Use $reviewing-migrations to check the migration in this branch."
policy:
  allow_implicit_invocation: false
```

- `short_description`: 25 to 64 characters.
- `default_prompt`: one sentence that mentions the skill as `$name`.
- `policy.allow_implicit_invocation: false`: Codex only uses the skill when the user names it with `$name`. This is the Codex counterpart of `disable-model-invocation`.
