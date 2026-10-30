# `_prompts/` — one prompt = one file

Each repeatable procedure (filing audit, inbox processing, monthly review…) is written here,
in `_prompts/<name>.md`, **as text readable by any AI**.

For Claude Code, the skill (`.claude/skills/<name>/SKILL.md`) and the command
(`.claude/commands/<name>.md`) only **point** to this file:

```markdown
---
name: <name>
description: <when to trigger it, in one precise sentence>
---
Read `_prompts/<name>.md` and apply it.
```

That way an AI without skills (or an environment that does not load `.claude/`) reads the same guideline.
**Few prompts**: 3 to 5 actually used are worth more than 25.
