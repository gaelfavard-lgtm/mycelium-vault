#!/usr/bin/env python3
"""
logging-notice.py — say "logging done" when LOGBOOK.md has moved.

Wired to the "PostToolUse" hook (.claude/settings.json), after every
Write, Edit or Bash. The counterpart of logbook-guard.py: that one watches
for the ABSENCE of a logbook write, this one confirms its PRESENCE — the user
does not have to ask for logging, they just receive a small confirmation.

HOW
  We do not look at the path passed to the tool: the logbook can be written
  by Write as well as by a shell redirection. We compare the file's modification
  time before / after, which catches every write path.

RULES
  - Never blocks: always exit 0.
  - Only speaks once per session.
  - The state lives OUTSIDE the vault.
  - On error: one line in the error log (no message at
    every tool: that would be noise; logbook-guard.py, for its part, reports its failure).

SETTINGS: MEMORY_VAULT, MEMORY_STATE (see logbook-guard.py).
"""
import sys, json, os, re, pathlib, datetime, traceback

HERE = pathlib.Path(__file__).resolve()
VAULT = pathlib.Path(os.environ.get("MEMORY_VAULT") or HERE.parents[2])
LOGBOOK = VAULT / "LOGBOOK.md"
STATE = pathlib.Path(os.environ.get("MEMORY_STATE")
                     or pathlib.Path.home() / ".claude" / ".logbook-guard-state") / "notice"
ERROR_LOG = STATE.parent / "errors.log"

MESSAGE = "Logging done — LOGBOOK.md updated."


def main():
    raw = sys.stdin.buffer.read().decode("utf-8-sig", "replace").strip()
    hook = json.loads(raw) if raw else {}
    sid = re.sub(r"[^A-Za-z0-9_-]", "", hook.get("session_id") or "unknown")[:16]

    STATE.mkdir(parents=True, exist_ok=True)
    marker = STATE / (sid + ".json")
    mtime = LOGBOOK.stat().st_mtime if LOGBOOK.is_file() else 0.0

    if not marker.is_file():
        # First run of the session: record the starting state, nothing to say.
        marker.write_text(json.dumps({"mtime_start": mtime, "announced": False}),
                          encoding="utf-8")
        return

    state = json.loads(marker.read_text(encoding="utf-8"))
    if state.get("announced") or mtime <= state.get("mtime_start", 0.0):
        return

    state["announced"] = True
    marker.write_text(json.dumps(state), encoding="utf-8")
    print(json.dumps({"systemMessage": MESSAGE}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        try:
            STATE.parent.mkdir(parents=True, exist_ok=True)
            with ERROR_LOG.open("a", encoding="utf-8") as j:
                j.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "  notice  "
                        + traceback.format_exc(limit=2).replace("\n", " | ") + "\n")
        except Exception:
            pass
    sys.exit(0)
