# `0-Inbox/` — le sas

Tout ce qui entre dans le coffre sans place évidente arrive ici : notes dictées au téléphone,
photos, documents, et les **tickets** déposés par une IA qui ne peut pas modifier les fichiers
(`ticket-<sujet>-<AAAA-MM-JJ>.md` : cible, opération, contenu exact).

**Rien n'y stagne.** À chaque démarrage, l'IA relève le sas, traite, inscrit le fichier à
`_contexte/tickets-traites.md` et le **sort** (à sa place, ou vers `a-supprimer/`).
Un fichier présent depuis plus de 3 jours est signalé en tête de séance.

*Les fichiers dont le nom commence par `_` ou `.` (comme celui-ci) sont ignorés par le hook.*
