#!/usr/bin/env python3
"""
consent-guard.py — no action that modifies something OUTSIDE the vault without
explicit consent in the user's message.                        (OPTIONAL)

Wired to the "PreToolUse" hook (.claude/settings.json), with a "matcher"
that only targets tools that WRITE elsewhere: sending mail, writing to
an online database, clicking or typing in a browser… Reads should not
come through here (adjust the matcher), or are let through below.

WHY
  "Do not act without explicit consent" written in the guidelines gets broken:
  an AI readily reads an intention ("we should…") as an order. This
  hook turns it into a mechanism: if the current turn contains no word of consent,
  the tool is refused and the AI must present its plan and then wait.

RULE
  The user's messages of the current turn (the one that opened it, plus
  those sent while the AI was working) must contain a consent:
  "go ahead", "do it", "yes" at the start, or an imperative verb (create, send…).
  CONSENTS list below, to adjust to the way you speak.

LIMITS — know them before installing it
  - A keyword does not read intent: a consent can be missed (false refusal) or
    misread ("don't send it" contains "send").
  - An order on ONE point lets through the whole following action in the same
    turn. The hook does not know whether the overall plan is validated.
  - Bash/PowerShell are not monitored (too broad).
  - Lesson from use: what worked best was not enriching the list,
    but the human getting into the habit of a clear word ("go ahead") when they want
    the action to happen.
  - On a script error: the tool passes (a broken guardrail must not
    block the session), BUT a visible message reports it.
"""
import sys, json, re, unicodedata, tempfile

CONSENTS = [
    r"\bgo ahead\b", r"\bgo for it\b", r"\bdo it\b", r"\bdo (this|that|them)\b",
    r"\byou can go ahead\b", r"\bgo\b", r"\bgreen light\b", r"\bi approve\b", r"\bapproved\b",
    r"\bok do\b", r"^yes\b",
    r"\bcreate\b", r"\bdelete\b", r"\brename\b", r"\blog (it|this|that)\b",
    r"\bpublish\b", r"\bsend\b", r"\bfix\b", r"\binstall\b", r"\bapply\b",
    r"\badd\b", r"\bmodify\b", r"\bchange\b", r"\benable\b", r"\bdisable\b", r"\breplace\b",
    r"\brun\b", r"\bexecute\b", r"\bput\b", r"\bbuild\b", r"\bcontinue\b",
]

# Browser actions that only look.
READ_NAV = {"screenshot", "zoom", "scroll", "scroll_to", "wait", "hover"}
READ_BATCH = {"find", "read_page", "get_page_text", "navigate", "tabs_context",
              "read_console_messages", "read_network_requests"}
# JavaScript that contains one of these patterns WRITES (click, DOM, request): refused.
JS_WRITES = (
    "click(", "setvalue(", "submit(", "dispatchevent(", "execcommand(", "focus(",
    "innerhtml", "outerhtml", "insertadjacent", "appendchild", "removechild",
    "createelement", "document.write", "localstorage.setitem", "sessionstorage.setitem",
    "clipboard.write", "xmlhttprequest", "websocket",
    '"post"', "'post'", '"patch"', "'patch'", '"put"', "'put'", '"delete"', "'delete'",
)

REFUSAL = ("Explicit consent missing. Present the plan in one sentence (where · what · result) "
           "and wait for the user to say to execute it.")


def normalize(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")   # no accents
    t = re.sub(r"<system-reminder>.*?</system-reminder>", " ", t, flags=re.S)
    return re.sub(r"[’'\-_]", " ", t).strip()


def js_read_only(payload):
    code = str((payload or {}).get("text") or "").lower()
    return bool(code) and not any(m in code for m in JS_WRITES)


def read_only(tool, payload):
    """True if the call only reads: we let it through without consent."""
    if tool.endswith("__computer"):
        return payload.get("action") in READ_NAV
    if tool.endswith("__javascript_tool"):
        return js_read_only(payload)
    if tool.endswith("__browser_batch"):
        for a in payload.get("actions") or []:
            name = a.get("name", "")
            if name == "computer":
                if (a.get("input") or {}).get("action") not in READ_NAV:
                    return False
            elif name == "javascript_tool":
                if not js_read_only(a.get("input") or {}):
                    return False
            elif name not in READ_BATCH:
                return False
        return True
    if tool in ("Edit", "Write"):
        # drafts in the system's temporary folder: free
        path = (payload.get("file_path") or "").replace("\\", "/").lower()
        return path.startswith(tempfile.gettempdir().replace("\\", "/").lower())
    return False


def turn_messages(path):
    """The user's messages of the current turn: the one that opened the turn,
    plus those sent while the AI was working ("queued_command").
    A clarification sent along the way therefore does not cancel the order given
    just before. The next message opens a new turn and resets.
    ⚠️ Depends on the internal format of Claude Code's transcript: re-check
    after an update (check-hooks.py does not test this point)."""
    turn = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            if '"user"' not in line and "queued_command" not in line:
                continue
            try:
                o = json.loads(line)
            except ValueError:
                continue
            if o.get("type") == "attachment":
                a = o.get("attachment") or {}
                if (a.get("type") == "queued_command"
                        and (a.get("origin") or {}).get("kind") == "human"
                        and turn and turn[0] == "text"):
                    turn[1].append(a.get("prompt") or "")
                continue
            if o.get("type") != "user" or o.get("isMeta"):
                continue
            if o.get("isCompactSummary"):
                turn = ("summary", [])
                continue
            c = (o.get("message") or {}).get("content")
            if isinstance(c, list):
                if any(isinstance(b, dict) and b.get("type") == "tool_result" for b in c):
                    continue
                c = " ".join(b.get("text", "") for b in c
                             if isinstance(b, dict) and b.get("type") == "text")
            if not isinstance(c, str):
                continue
            clean = re.sub(r"<system-reminder>.*?</system-reminder>", "", c, flags=re.S).strip()
            if not clean or clean.startswith("<"):
                continue
            turn = ("text", [clean])   # new turn: start again from this message
    return turn


def main():
    raw = sys.stdin.buffer.read().decode("utf-8-sig", "replace").strip()
    hook = json.loads(raw) if raw else {}
    tool = hook.get("tool_name") or ""
    if read_only(tool, hook.get("tool_input") or {}):
        return
    turn = turn_messages(hook.get("transcript_path") or "")
    if turn is None or turn[0] == "summary":
        return   # resumed after an automatic summary: consent was given before
    for message in turn[1]:
        text = normalize(message)
        if any(re.search(p, text) for p in CONSENTS):
            return
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": REFUSAL,
    }}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(json.dumps({"systemMessage": "consent-guard.py is down, the tool passes without "
                                           "a check: %s" % type(e).__name__}))
    sys.exit(0)
