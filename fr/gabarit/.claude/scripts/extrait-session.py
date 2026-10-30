#!/usr/bin/env python3
"""
extrait-session.py — extrait lisible d'une session Claude Code, déposé dans le coffre.
                                                              (FACULTATIF)

Branché sur le hook « SessionEnd » (.claude/settings.json). Reçoit sur stdin le
JSON du hook, qui contient `transcript_path` et `session_id`.

POURQUOI
  Les journaux bruts (.jsonl) vivent hors du coffre (~/.claude/projects/), donc
  hors synchronisation et hors sauvegarde, et pèsent lourd (sorties d'outils).
  L'extrait ne garde que le texte échangé (~10 % du brut), en Markdown : la
  sauvegarde le ramasse sans rien changer.
  ⚠️ Un extrait ne fait foi sur rien (AGENTS.md §4.4) : il dit ce qui s'est
  dit, pas ce qui s'est fait. L'état d'une affaire se lit dans sa fiche.

  Claude Code purge ses journaux bruts après 30 jours par défaut ; pour les
  garder plus longtemps : "cleanupPeriodDays" dans settings.json.

⚠️ CONFIDENTIALITÉ
  Tout ce qui a été dit en séance entre dans le coffre — donc dans sa
  synchronisation et sa sauvegarde. Si votre coffre est partagé ou publié,
  excluez `_contexte/journal-sessions/` (ou n'installez pas ce hook).

RÈGLES
  - Un fichier par session, ÉCRASÉ à chaque passage : le brut ne fait que
    grossir, la dernière écriture contient tout. (/clear et la reprise
    déclenchent SessionEnd plusieurs fois pour une même session.)
  - Ne supprime jamais rien.
  - Écrit une ligne de journal à chaque passage, OK ou ÉCHEC : une panne se voit.
  - Ne fait jamais échouer la session : sortie 0 toujours.

RÉGLAGES (variables d'environnement facultatives)
  MEMOIRE_COFFRE  chemin du coffre (par défaut : deux dossiers au-dessus de ce script)
  MEMOIRE_PRENOM  nom affiché pour vos messages (par défaut : « Utilisateur »)
"""
import sys, os, json, datetime, pathlib, traceback

ICI = pathlib.Path(__file__).resolve()
COFFRE = pathlib.Path(os.environ.get("MEMOIRE_COFFRE") or ICI.parents[2])
DEST = COFFRE / "_contexte" / "journal-sessions"
JOURNAL = DEST / "_journal-extraits.txt"
HUMAIN = os.environ.get("MEMOIRE_PRENOM") or "Utilisateur"
IA = "Claude"


def note(ligne):
    try:
        DEST.mkdir(parents=True, exist_ok=True)
        with JOURNAL.open("a", encoding="utf-8") as f:
            f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "  " + ligne + "\n")
    except Exception:
        pass


def texte(message):
    """Le texte d'un message, sans les sorties d'outils."""
    c = message.get("content")
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return "\n".join(b.get("text", "") for b in c
                         if isinstance(b, dict) and b.get("type") == "text")
    return ""


def main():
    # utf-8-sig : tolère un BOM selon le shell qui appelle le hook
    brut = sys.stdin.buffer.read().decode("utf-8-sig", "replace").strip()
    hook = json.loads(brut) if brut else {}
    chemin = hook.get("transcript_path")
    sid = hook.get("session_id") or "inconnue"
    raison = hook.get("reason") or "?"

    if not chemin or not pathlib.Path(chemin).is_file():
        note("ECHEC  transcript introuvable  session=%s" % sid[:8])
        return

    src = pathlib.Path(chemin)
    lignes, n = [], 0
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
            t = texte(m).strip()
            if not t:
                continue
            qui = HUMAIN if m["role"] == "user" else IA
            lignes.append("### " + qui + "\n\n" + t)
            n += 1

    DEST.mkdir(parents=True, exist_ok=True)
    jour = datetime.datetime.fromtimestamp(src.stat().st_mtime).strftime("%Y-%m-%d")
    cible = DEST / ("%s-%s.md" % (jour, sid[:8]))
    entete = (
        "# Session du %s — %s\n\n"
        "*Extrait automatique, texte échangé seulement. Ne fait foi sur rien.*\n"
        "*Brut : `%s` (hors coffre) · fin : `%s` · %d messages · généré le %s.*\n\n---\n\n"
        % (jour, sid[:8], src.name, raison, n,
           datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    )
    cible.write_text(entete + "\n\n".join(lignes) + "\n", encoding="utf-8")
    note("OK     %s  %d messages  %.0f Ko  (raison: %s)"
         % (cible.name, n, cible.stat().st_size / 1024, raison))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        note("ECHEC  " + traceback.format_exc(limit=2).replace("\n", " | "))
    sys.exit(0)
