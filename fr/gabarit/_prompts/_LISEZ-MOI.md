# `_prompts/` — un prompt = un fichier

Chaque procédure répétable (audit de rangement, traitement du sas, revue mensuelle…) s'écrit ici,
dans `_prompts/<nom>.md`, **en texte lisible par n'importe quelle IA**.

Pour Claude Code, la skill (`.claude/skills/<nom>/SKILL.md`) et la commande
(`.claude/commands/<nom>.md`) ne font que **pointer** vers ce fichier :

```markdown
---
name: <nom>
description: <quand la déclencher, en une phrase précise>
---
Lis `_prompts/<nom>.md` et applique-le.
```

Ainsi une IA sans skills (ou un environnement qui ne charge pas `.claude/`) lit la même consigne.
**Peu de prompts** : 3 à 5 réellement utilisés valent mieux que 25.
