#!/usr/bin/env python3
"""
logbook-guard.py — do not hand back control without having logged the session.

Wired to Claude Code's "Stop" hook (.claude/settings.json), so it runs at
EVERY end of turn. It must stay quiet and fast: it only speaks once
per session.

WHAT IT DOES
  1. Logbook check. If, since the start of the session,
       - a vault file has been modified,
       - or the session has reached TURN_THRESHOLD exchanges,
     and LOGBOOK.md has NOT moved, it refuses the end of turn ONCE:
     the AI must log (AGENTS.md §4), or say in one sentence why there is
     nothing to log.
  2. Inbox check. Any file in 0-Inbox whose name is listed in the register
     _context/tickets-done.md (hence processed) but which is still there makes it
     refuse the end of turn ONCE (AGENTS.md §5). The "Kept on purpose" section
     of the register is ignored.

  It writes NOTHING in the vault: writing takes judgement, that is the AI's
  job. It only automates the CHECK.

DESIGN RULES
  - A single refusal per session and per check (flag set BEFORE answering:
    never a loop, even if the write fails afterwards).
  - Never a refusal if the logbook has moved since the start of the session.
  - The state lives OUTSIDE the vault (home folder), so as not to pollute
    the sync or the backup.
  - Walk of the vault capped at MAX_TIME seconds: on a slow cloud folder,
    an incomplete check beats a hook that exceeds its timeout.
  - On error: never a block (exit 0), BUT a visible message and
    a line in a log. A guardrail that goes quiet is worse than
    no guardrail: you stop checking.

HOW TO ROLL BACK, WITHOUT AN AI
  1. Keep the reminder, turn off the refusal — create an empty file named
     .logbook-guard-no-block in the state folder (see STATE below):
         Git Bash / macOS / Linux : touch ~/.claude/.logbook-guard-state/.logbook-guard-no-block
         PowerShell : New-Item -ItemType File "$HOME\\.claude\\.logbook-guard-state\\.logbook-guard-no-block"
     Deleting that file re-enables the refusal.
  2. Turn everything off — remove the "Stop" block from .claude/settings.json.
  (A hook cannot be tested in the session that modifies it: the effect shows in the
  next session. To test it without Claude: .claude/scripts/check-hooks.py)

SETTINGS (optional environment variables)
  MEMORY_VAULT  path of the vault (default: two folders above this script)
  MEMORY_STATE  state folder (default: ~/.claude/.logbook-guard-state)
"""
import sys, json, os, re, time, pathlib, datetime, traceback

# --- Settings -----------------------------------------------------------------
TURN_THRESHOLD = 5       # number of exchanges that triggers the check even without a write
MAX_TIME = 3.0           # max seconds to walk the vault
AUTHOR_SUFFIXES = ()     # e.g. ("alex", "sam") if your notes are named note-<date>-alex.md

HERE = pathlib.Path(__file__).resolve()
VAULT = pathlib.Path(os.environ.get("MEMORY_VAULT") or HERE.parents[2])
LOGBOOK = VAULT / "LOGBOOK.md"
INBOX = VAULT / "0-Inbox"
REGISTER = VAULT / "_context" / "tickets-done.md"
STATE = pathlib.Path(os.environ.get("MEMORY_STATE")
                     or pathlib.Path.home() / ".claude" / ".logbook-guard-state")
SWITCH = STATE / ".logbook-guard-no-block"
ERROR_LOG = STATE / "errors.log"

# Machinery or noise: a write in there does not count as logging.
# (worktrees and .trash: other vaults saw their checks drowned in false positives.)
IGNORED = {".obsidian", ".git", "__pycache__", "session-logs", "worktrees", ".trash",
           "node_modules"}

# --- Messages -----------------------------------------------------------------
MESSAGE = (
    "Guardrail reminder: {cause}, and LOGBOOK.md has not moved. "
    "AGENTS.md §4: every action has two halves. Log before closing."
)
MESSAGE_BLOCK = (
    "Logbook guardrail: end of turn refused once ({cause}, nothing in the logbook). "
    "The AI must log, or say why there is nothing to log."
)
INSTRUCTION = (
    "The logbook guardrail reports that this session has logged nothing ({cause}). "
    "Apply AGENTS.md §4 before handing back control: dated entry in LOGBOOK.md "
    "(marker [content] or [maintenance], signed), update of the relevant reference "
    "note, and removal of what the action makes false. If the session really does not "
    "deserve an entry — a question, a read, nothing decided — say so in one sentence "
    "rather than ignoring it."
)
INSTRUCTION_INBOX = (
    "Inbox guardrail: these files in 0-Inbox are listed in the tickets-done.md register, "
    "so they are processed, but have not been taken out: {files}. AGENTS.md §5: a processed "
    "file never stays in 0-Inbox — file it in its place if it has value of its own, "
    "otherwise move it to to-delete/. If it must stay on purpose, it is up to the user to say so: "
    "then write it under \"Kept on purpose\" in the register."
)


def vault_touched(since):
    """Relative path of the first file modified since `since`, or None.
    Stops as soon as it finds one, or after MAX_TIME seconds."""
    logbook = str(LOGBOOK).lower()
    deadline = time.time() + MAX_TIME
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in IGNORED]
        if time.time() > deadline:
            return None
        for f in files:
            path = os.path.join(root, f)
            if path.lower() == logbook:
                continue
            try:
                if os.path.getmtime(path) > since:
                    return os.path.relpath(path, VAULT)
            except OSError:
                continue
    return None


def _key(name):
    """note-2026-01-15-1346-3.jpg -> note-2026-01-15-1346
    (no extension, no sync "(1)", no -N attachment suffix)."""
    base = os.path.splitext(name)[0]
    base = re.sub(r" \(\d+\)$", "", base)
    base = re.sub(r"-\d$", "", base)
    return base


def forgotten_in_inbox():
    """Files in 0-Inbox whose name is listed in the register, outside "Kept on purpose"."""
    if not INBOX.is_dir() or not REGISTER.is_file():
        return []
    text = REGISTER.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"(?ims)^##[^\n]*kept on purpose.*?(?=^## |\Z)", "", text)
    forgotten = []
    for f in sorted(os.listdir(INBOX)):
        if f.startswith((".", "_")) or f.lower() == "desktop.ini":
            continue
        if not (INBOX / f).is_file():
            continue
        key = _key(f)
        candidates = {key}
        if AUTHOR_SUFFIXES:
            candidates.add(re.sub(r"-(%s)$" % "|".join(map(re.escape, AUTHOR_SUFFIXES)), "", key))
        # minimum length: avoid a short name ("note") matching anything at all
        if any(len(c) >= 10 and c in text for c in candidates):
            forgotten.append(f)
    return forgotten


def write(marker, state):
    marker.write_text(json.dumps(state), encoding="utf-8")


def main():
    raw = sys.stdin.buffer.read().decode("utf-8-sig", "replace").strip()
    hook = json.loads(raw) if raw else {}
    sid = re.sub(r"[^A-Za-z0-9_-]", "", hook.get("session_id") or "unknown")[:16]

    # Already re-run after a refusal: never chain two refusals.
    if hook.get("stop_hook_active"):
        return

    STATE.mkdir(parents=True, exist_ok=True)
    marker = STATE / (sid + ".json")
    mtime = LOGBOOK.stat().st_mtime if LOGBOOK.is_file() else 0.0

    if marker.is_file():
        state = json.loads(marker.read_text(encoding="utf-8"))
    else:
        # Start of session: the transcript's creation time is authoritative, otherwise
        # now (the first turn's writes would then be missed).
        start = time.time()
        t = hook.get("transcript_path")
        if t:
            try:
                start = os.path.getctime(t)
            except OSError:
                pass
        state = {"mtime_start": mtime, "t_start": start, "turns": 0, "warned": False}
        # Logbook modified during this first turn: it has moved.
        if mtime > start:
            state["mtime_start"] = -1.0

    state["turns"] += 1
    write(marker, state)

    # --- 1. Inbox check, independent of the logbook (once per session) ---
    if not state.get("warned_inbox"):
        forgotten = forgotten_in_inbox()
        if forgotten:
            state["warned_inbox"] = True
            write(marker, state)
            files = ", ".join(forgotten[:15]) + (" ..." if len(forgotten) > 15 else "")
            text = INSTRUCTION_INBOX.format(files=files)
            output = {
                "systemMessage": "Inbox guardrail: %d processed file(s) still in 0-Inbox."
                                 % len(forgotten),
                "hookSpecificOutput": {"hookEventName": "Stop", "additionalContext": text},
            }
            if not SWITCH.exists():
                output["decision"] = "block"
                output["reason"] = text
            print(json.dumps(output))
            return

    # --- 2. Logbook check ---
    if state["warned"]:
        return
    if mtime > state["mtime_start"]:
        return  # the logbook has moved: nothing to say

    touched = vault_touched(state.get("t_start", 0.0))
    if touched:
        cause = "the vault has been modified (" + touched + ")"
    elif state["turns"] >= TURN_THRESHOLD:
        cause = "%d exchanges" % state["turns"]
    else:
        return

    # Flag set BEFORE answering: at worst a single refusal per session.
    state["warned"] = True
    write(marker, state)

    output = {
        "systemMessage": MESSAGE.format(cause=cause),
        "hookSpecificOutput": {"hookEventName": "Stop",
                               "additionalContext": INSTRUCTION.format(cause=cause)},
    }
    if not SWITCH.exists():
        output["decision"] = "block"
        output["reason"] = INSTRUCTION.format(cause=cause)
        output["systemMessage"] = MESSAGE_BLOCK.format(cause=cause)
    print(json.dumps(output))


def report_failure():
    """Never a block on failure, but never silence either."""
    try:
        STATE.mkdir(parents=True, exist_ok=True)
        with ERROR_LOG.open("a", encoding="utf-8") as j:
            j.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "  "
                    + traceback.format_exc(limit=3).replace("\n", " | ") + "\n")
    except Exception:
        pass
    print(json.dumps({"systemMessage": "logbook-guard.py is down (the logbook check "
                                       "is not running). Details: " + str(ERROR_LOG)}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        report_failure()
    sys.exit(0)
