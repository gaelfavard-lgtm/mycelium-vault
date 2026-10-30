# CLAUDE.md — Claude bootstrap

Read automatically by Claude Code at startup. **All the rules live in `AGENTS.md`** —
single source, all AIs. Duplicate nothing here.

## Memory — loaded at every startup
@_context/MEMORY.md

## Claude-specific mechanics
- **Skills**: `.claude/skills/<name>/SKILL.md` (automatic triggering); **commands**:
  `.claude/commands/<name>.md` (`/<name>`). Convention: one prompt = one file `_prompts/<name>.md`;
  skill and command only point to it, so that another AI can read it too.
- **Hooks**: `.claude/settings.json` wires the scripts in `.claude/scripts/` (see `README.md`).
  A hook cannot be tested in the session that modifies it: the effect shows in the next one.
- ⚠️ Some environments (desktop application, "connected folder" mode) do not load the
  vault's `.claude/` — no skills, no commands, no hooks. There, read `_prompts/<name>.md` and
  apply it by hand. **Check on your own setup** before relying on a hook.
- **End of session**: log in `LOGBOOK.md` according to `AGENTS.md` §4.
