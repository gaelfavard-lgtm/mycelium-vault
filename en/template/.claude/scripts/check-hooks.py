#!/usr/bin/env python3
"""
check-hooks.py — test the hooks WITHOUT Claude, on a throwaway copy of the vault.

Why: the plumbing breaks at every evolution of the tool, and a hook cannot be
tested in the session that modifies it. Run this script after a Claude Code
update or a change to a hook:

    python .claude/scripts/check-hooks.py

It copies the vault into a temporary folder (only the files needed for the
test), simulates ends of turn, and says OK or FAILURE for each case.
It touches neither the real vault nor the real state of the hooks.
"""
import json, os, pathlib, shutil, subprocess, sys, tempfile, time

HERE = pathlib.Path(__file__).resolve().parent
VAULT = HERE.parents[1]


def run(script, vault, state, payload):
    env = dict(os.environ, MEMORY_VAULT=str(vault), MEMORY_STATE=str(state))
    raw = payload if isinstance(payload, bytes) else json.dumps(payload).encode()
    r = subprocess.run([sys.executable, str(HERE / script)], input=raw,
                       capture_output=True, env=env, timeout=20)
    output = r.stdout.decode("utf-8", "replace").strip()
    return r.returncode, (json.loads(output) if output else {})


def main():
    results = []

    def case(name, condition):
        results.append(condition)
        print(("  OK       " if condition else "  FAILURE  ") + name)

    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        vault, state = tmp / "vault", tmp / "state"
        (vault / "0-Inbox").mkdir(parents=True)
        (vault / "_context").mkdir()
        (vault / "LOGBOOK.md").write_text("# Logbook\n", encoding="utf-8")
        (vault / "_context" / "tickets-done.md").write_text(
            "## Done\n- ticket-example-2026-01-15.md\n\n## Kept on purpose\n"
            "- ticket-kept-2026-01-15.md\n", encoding="utf-8")
        transcript = tmp / "t.jsonl"
        transcript.write_text("", encoding="utf-8")
        time.sleep(0.05)
        base = {"session_id": "test1", "transcript_path": str(transcript)}

        print("logbook-guard.py")
        code, out = run("logbook-guard.py", vault, state, base)
        case("turn 1 without a write: silence", code == 0 and out == {})

        (vault / "note.md").write_text("x", encoding="utf-8")
        code, out = run("logbook-guard.py", vault, state, base)
        case("file modified, logbook untouched: refusal", out.get("decision") == "block")

        code, out = run("logbook-guard.py", vault, state, base)
        case("a single refusal per session", out == {})

        code, out = run("logbook-guard.py", vault, state, dict(base, stop_hook_active=True))
        case("re-run after refusal: silence", out == {})

        b2 = {"session_id": "test2", "transcript_path": str(transcript)}
        run("logbook-guard.py", vault, state, b2)
        time.sleep(0.05)
        (vault / "LOGBOOK.md").write_text("# Logbook\n## entry\n", encoding="utf-8")
        code, out = run("logbook-guard.py", vault, state, b2)
        case("logbook modified: silence", out == {})

        (vault / "0-Inbox" / "ticket-example-2026-01-15.md").write_text("x", encoding="utf-8")
        (vault / "0-Inbox" / "ticket-kept-2026-01-15.md").write_text("x", encoding="utf-8")
        code, out = run("logbook-guard.py", vault, state, {"session_id": "test3"})
        reason = out.get("reason", "")
        case("processed file left in the inbox: refusal",
             out.get("decision") == "block" and "ticket-example" in reason)
        case("\"Kept on purpose\" ignored", "ticket-kept" not in reason)

        (state / ".logbook-guard-no-block").write_text("", encoding="utf-8")
        code, out = run("logbook-guard.py", vault, state, {"session_id": "test4"})
        case("switch: reminder without refusal", "decision" not in out and "systemMessage" in out)

        code, out = run("logbook-guard.py", vault, state, b"{not json")
        case("unreadable input: exit 0 and failure reported",
             code == 0 and "is down" in out.get("systemMessage", ""))

        print("logging-notice.py")
        n = {"session_id": "notice1"}
        code, out = run("logging-notice.py", vault, state, n)
        case("first run: silence", out == {})
        time.sleep(0.05)
        (vault / "LOGBOOK.md").write_text("# Logbook\n## other\n", encoding="utf-8")
        code, out = run("logging-notice.py", vault, state, n)
        case("logbook modified: confirmation", "Logging done" in out.get("systemMessage", ""))

    print("\n%d/%d cases OK" % (sum(results), len(results)))
    return 0 if all(results) else 1


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())
