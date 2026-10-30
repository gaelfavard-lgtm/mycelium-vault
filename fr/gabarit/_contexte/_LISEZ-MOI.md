# `_contexte/` — ce qui décrit le système, pas le travail

Vit à côté d'IPCRA. On y trouve :
- `MEMORY.md` — l'index lu à chaque démarrage (plafond ~60 lignes) ;
- `profil/` — les 2 fiches lues au démarrage (`profil.md`, `consignes-de-travail.md`), plus
  celles qui ne s'ouvrent qu'à la demande ;
- `tickets-traites.md` — le registre des fichiers sortis de `0-Inbox` (lu par `garde-carnet.py`) ;
- `journal-sessions/` — créé par le hook optionnel `extrait-session.py`. **Ne fait foi sur rien.**

Le budget de démarrage (300 lignes, `AGENTS.md` §7) compte `MEMORY.md` et les 2 fiches de profil.
