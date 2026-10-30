#!/usr/bin/env python3
"""
notif-consignation.py — dire « consignation faite » quand CARNET-DE-BORD.md a bougé.

Branché sur le hook « PostToolUse » (.claude/settings.json), après chaque
Write, Edit ou Bash. Le pendant de garde-carnet.py : celui-là surveille
l'ABSENCE d'écriture au carnet, celui-ci confirme sa PRÉSENCE — l'utilisateur
n'a pas à demander la consignation, il en reçoit juste une petite confirmation.

COMMENT
  On ne regarde pas le chemin passé à l'outil : le carnet s'écrit aussi bien
  par Write que par une redirection shell. On compare la date de modification
  du fichier avant / après, ce qui attrape tous les chemins d'écriture.

RÈGLES
  - Ne bloque jamais : sortie 0 toujours.
  - Ne parle qu'une fois par session.
  - L'état vit HORS du coffre.
  - En cas d'erreur : une ligne dans le journal d'erreurs (pas de message à
    chaque outil : ce serait du bruit ; garde-carnet.py, lui, signale sa panne).

RÉGLAGES : MEMOIRE_COFFRE, MEMOIRE_ETAT (voir garde-carnet.py).
"""
import sys, json, os, re, pathlib, datetime, traceback

ICI = pathlib.Path(__file__).resolve()
COFFRE = pathlib.Path(os.environ.get("MEMOIRE_COFFRE") or ICI.parents[2])
CARNET = COFFRE / "CARNET-DE-BORD.md"
ETAT = pathlib.Path(os.environ.get("MEMOIRE_ETAT")
                    or pathlib.Path.home() / ".claude" / ".etat-garde-carnet") / "notif"
JOURNAL_ERREURS = ETAT.parent / "erreurs.log"

MESSAGE = "Consignation faite — CARNET-DE-BORD.md mis à jour."


def main():
    brut = sys.stdin.buffer.read().decode("utf-8-sig", "replace").strip()
    hook = json.loads(brut) if brut else {}
    sid = re.sub(r"[^A-Za-z0-9_-]", "", hook.get("session_id") or "inconnue")[:16]

    ETAT.mkdir(parents=True, exist_ok=True)
    marqueur = ETAT / (sid + ".json")
    mtime = CARNET.stat().st_mtime if CARNET.is_file() else 0.0

    if not marqueur.is_file():
        # Premier passage de la session : on note l'état de départ, rien à dire.
        marqueur.write_text(json.dumps({"mtime_depart": mtime, "annonce": False}),
                            encoding="utf-8")
        return

    etat = json.loads(marqueur.read_text(encoding="utf-8"))
    if etat.get("annonce") or mtime <= etat.get("mtime_depart", 0.0):
        return

    etat["annonce"] = True
    marqueur.write_text(json.dumps(etat), encoding="utf-8")
    print(json.dumps({"systemMessage": MESSAGE}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        try:
            ETAT.parent.mkdir(parents=True, exist_ok=True)
            with JOURNAL_ERREURS.open("a", encoding="utf-8") as j:
                j.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "  notif  "
                        + traceback.format_exc(limit=2).replace("\n", " | ") + "\n")
        except Exception:
            pass
    sys.exit(0)
