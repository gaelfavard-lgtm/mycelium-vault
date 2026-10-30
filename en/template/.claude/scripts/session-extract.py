#!/usr/bin/env python3
"""
session-extract.py — readable extract of a Claude Code session, dropped into the vault.
                                                              (OPTIONAL)

Wired to the "SessionEnd" hook (.claude/settings.json). Receives on stdin the
hook's JSON, which contains `transcript_path` and `session_id`.

WHY
  The raw logs (.jsonl) live outside the vault (~/.claude/projects/), hence
  outside the sync and outside the backup, and they are heavy (tool outputs).
  The extract keeps only the exchanged text (~10% of the raw), in Markdown: the
  backup picks it up without changing anything.
  ⚠️ An extract is authoritative on nothing (AGENTS.md §4.4): it says what was
  said, not what was done. The state of a matter is read in its note.

  Claude Code purges its raw logs after 30 days by default; to keep
  them longer: "cleanupPeriodDays" in settings.json.

⚠️ PRIVACY
  Everything that was said in session enters the vault — hence its
  sync and its backup. If your vault is shared or published,
  exclude `_context/session-logs/` (or do not install this hook).

RULES
  - One file per session, OVERWRITTEN at every run: the raw log only
    grows, the last write contains everything. (/clear and resuming
    trigger SessionEnd several times for the same session.)
  - Never deletes anything.
  - Writes a log line at every run, OK or FAILURE: a breakdown is visible.
  - Never makes the session fail: always exit 0.

SETTINGS (optional environment variables)
  MEMORY_VAULT  path of the vault (default: two folders above this script)
  MEMORY_NAME   name displayed for your messages (default: "User")
"""
import sys, os, json, datetime, pathlib, traceback

HERE = pathlib.Path(__file__).resolve()
VAULT = pathlib.Path(os.environ.get("MEMORY_VAULT") or HERE.parents[2])
DEST = VAULT / "_context" / "session-logs"
LOG = DEST / "_extracts-log.txt"
HUMAN = os.environ.get("MEMORY_NAME") or "User"
AI = "Claude"


def note(line):
    try:
        DEST.mkdir(parents=True, exist_ok=True)
        with LOG.open("a", encoding="utf-8") as f:
            f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "  " + line + "\n")
    except Exception:
        pass


def text_of(message):
    """The text of a message, without tool outputs."""
    c = message.get("content")
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return "\n".join(b.get("text", "") for b in c
                         if isinstance(b, dict) and b.get("type") == "text")
    return ""


def main():
    # utf-8-sig: tolerates a BOM depending on the shell that calls the hook
    raw = sys.stdin.buffer.read().decode("utf-8-sig", "replace").strip()
    hook = json.loads(raw) if raw else {}
    path = hook.get("transcript_path")
    sid = hook.get("session_id") or "unknown"
    reason = hook.get("reason") or "?"

    if not path or not pathlib.Path(path).is_file():
        note("FAILURE  transcript not found  session=%s" % sid[:8])
        return

    src = pathlib.Path(path)
    lines, n = [], 0
    with src.open("r", encoding="utf-8", errors="replace") as f:
        for l in f:
            l = l.strip()
            if not l:
                continue
            try:
                o = json.loads(l)
            except Exception:
                continue
            m = o.get("message")
            if not isinstance(m, dict) or not m.get("role"):
                continue
            t = text_of(m).strip()
            if not t:
                continue
            who = HUMAN if m["role"] == "user" else AI
            lines.append("### " + who + "\n\n" + t)
            n += 1

    DEST.mkdir(parents=True, exist_ok=True)
    day = datetime.datetime.fromtimestamp(src.stat().st_mtime).strftime("%Y-%m-%d")
    target = DEST / ("%s-%s.md" % (day, sid[:8]))
    header = (
        "# Session of %s — %s\n\n"
        "*Automatic extract, exchanged text only. Authoritative on nothing.*\n"
        "*Raw: `%s` (outside the vault) · end: `%s` · %d messages · generated on %s.*\n\n---\n\n"
        % (day, sid[:8], src.name, reason, n,
           datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    )
    target.write_text(header + "\n\n".join(lines) + "\n", encoding="utf-8")
    note("OK     %s  %d messages  %.0f KB  (reason: %s)"
         % (target.name, n, target.stat().st_size / 1024, reason))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        note("FAILURE  " + traceback.format_exc(limit=2).replace("\n", " | "))
    sys.exit(0)
