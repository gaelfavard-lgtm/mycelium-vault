# Registre des tickets `0-Inbox` traités

**Fait foi** : avant de traiter `0-Inbox`, comparer à ce registre — ne **jamais** retraiter un
fichier qui y figure. Inscrire le **nom complet du fichier**, puis le sortir du sas
(`AGENTS.md` §5). Le hook `garde-carnet.py` lit ce registre : un fichier qui y figure et qui est
encore dans `0-Inbox` fait refuser la fin de tour.

## Traités

| Fichier | Traité le | Ce qui a été fait | Où il est parti |
|---|---|---|---|
| `ticket-renommer-plans-abri-2026-01-15.md` *(exemple fictif)* | 2026-01-16 | 3 plans renommés, 1 fiche corrigée | `a-supprimer/` |

## Gardés exprès

*Fichiers que l'utilisateur veut voir rester dans `0-Inbox` malgré leur traitement. Le hook les
ignore. Une ligne par fichier, avec la raison et la date.*
