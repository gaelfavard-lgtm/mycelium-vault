#!/usr/bin/env python3
"""
verifier-hooks.py — tester les hooks SANS Claude, sur une copie jetable du coffre.

Pourquoi : la plomberie casse à chaque évolution de l'outil, et un hook ne se
teste pas dans la session qui le modifie. Lancez ce script après une mise à jour
de Claude Code ou une modification d'un hook :

    python .claude/scripts/verifier-hooks.py

Il copie le coffre dans un dossier temporaire (seulement les fichiers utiles au
test), simule des fins de tour, et dit pour chaque cas OK ou ÉCHEC.
Il ne touche ni au coffre réel ni à l'état réel des hooks.
"""
import json, os, pathlib, shutil, subprocess, sys, tempfile, time

ICI = pathlib.Path(__file__).resolve().parent
COFFRE = ICI.parents[1]


def lancer(script, coffre, etat, entree):
    env = dict(os.environ, MEMOIRE_COFFRE=str(coffre), MEMOIRE_ETAT=str(etat))
    brut = entree if isinstance(entree, bytes) else json.dumps(entree).encode()
    r = subprocess.run([sys.executable, str(ICI / script)], input=brut,
                       capture_output=True, env=env, timeout=20)
    sortie = r.stdout.decode("utf-8", "replace").strip()
    return r.returncode, (json.loads(sortie) if sortie else {})


def main():
    resultats = []

    def cas(nom, condition):
        resultats.append(condition)
        print(("  OK     " if condition else "  ÉCHEC  ") + nom)

    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        coffre, etat = tmp / "coffre", tmp / "etat"
        (coffre / "0-Inbox").mkdir(parents=True)
        (coffre / "_contexte").mkdir()
        (coffre / "CARNET-DE-BORD.md").write_text("# Carnet\n", encoding="utf-8")
        (coffre / "_contexte" / "tickets-traites.md").write_text(
            "## Traités\n- ticket-exemple-2026-01-15.md\n\n## Gardés exprès\n"
            "- ticket-garde-2026-01-15.md\n", encoding="utf-8")
        transcript = tmp / "t.jsonl"
        transcript.write_text("", encoding="utf-8")
        time.sleep(0.05)
        base = {"session_id": "test1", "transcript_path": str(transcript)}

        print("garde-carnet.py")
        code, out = lancer("garde-carnet.py", coffre, etat, base)
        cas("tour 1 sans écriture : silence", code == 0 and out == {})

        (coffre / "fiche.md").write_text("x", encoding="utf-8")
        code, out = lancer("garde-carnet.py", coffre, etat, base)
        cas("fichier modifié, carnet intact : refus", out.get("decision") == "block")

        code, out = lancer("garde-carnet.py", coffre, etat, base)
        cas("un seul refus par session", out == {})

        code, out = lancer("garde-carnet.py", coffre, etat, dict(base, stop_hook_active=True))
        cas("relance après refus : silence", out == {})

        b2 = {"session_id": "test2", "transcript_path": str(transcript)}
        lancer("garde-carnet.py", coffre, etat, b2)
        time.sleep(0.05)
        (coffre / "CARNET-DE-BORD.md").write_text("# Carnet\n## entrée\n", encoding="utf-8")
        code, out = lancer("garde-carnet.py", coffre, etat, b2)
        cas("carnet modifié : silence", out == {})

        (coffre / "0-Inbox" / "ticket-exemple-2026-01-15.md").write_text("x", encoding="utf-8")
        (coffre / "0-Inbox" / "ticket-garde-2026-01-15.md").write_text("x", encoding="utf-8")
        code, out = lancer("garde-carnet.py", coffre, etat, {"session_id": "test3"})
        raison = out.get("reason", "")
        cas("fichier traité resté dans le sas : refus",
            out.get("decision") == "block" and "ticket-exemple" in raison)
        cas("« Gardés exprès » ignoré", "ticket-garde" not in raison)

        (etat / ".garde-carnet-sans-blocage").write_text("", encoding="utf-8")
        code, out = lancer("garde-carnet.py", coffre, etat, {"session_id": "test4"})
        cas("interrupteur : rappel sans refus", "decision" not in out and "systemMessage" in out)

        code, out = lancer("garde-carnet.py", coffre, etat, b"{pas du json")
        cas("entrée illisible : sortie 0 et panne signalée",
            code == 0 and "panne" in out.get("systemMessage", ""))

        print("notif-consignation.py")
        n = {"session_id": "notif1"}
        code, out = lancer("notif-consignation.py", coffre, etat, n)
        cas("premier passage : silence", out == {})
        time.sleep(0.05)
        (coffre / "CARNET-DE-BORD.md").write_text("# Carnet\n## autre\n", encoding="utf-8")
        code, out = lancer("notif-consignation.py", coffre, etat, n)
        cas("carnet modifié : confirmation", "Consignation faite" in out.get("systemMessage", ""))

    print("\n%d/%d cas OK" % (sum(resultats), len(resultats)))
    return 0 if all(resultats) else 1


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())
