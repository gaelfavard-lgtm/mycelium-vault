# CLAUDE.md — amorçage Claude

Lu automatiquement par Claude Code au démarrage. **Toutes les règles vivent dans `AGENTS.md`** —
source unique, toutes IA. Ne rien dupliquer ici.

## Mémoire — chargée à chaque démarrage
@_contexte/MEMORY.md

## Mécanique propre à Claude
- **Skills** : `.claude/skills/<nom>/SKILL.md` (déclenchement automatique) ; **commandes** :
  `.claude/commands/<nom>.md` (`/<nom>`). Convention : un prompt = un fichier `_prompts/<nom>.md` ;
  skill et commande ne font que pointer vers lui, pour qu'une autre IA puisse le lire aussi.
- **Hooks** : `.claude/settings.json` branche les scripts de `.claude/scripts/` (voir `README.md`).
  Un hook ne se teste pas dans la session qui le modifie : l'effet se voit à la suivante.
- ⚠️ Certains environnements (application de bureau, mode « dossier connecté ») ne chargent pas le
  `.claude/` du coffre — ni skills, ni commandes, ni hooks. Là-bas, lire `_prompts/<nom>.md` et
  l'appliquer à la main. **Vérifiez chez vous** avant de compter sur un hook.
- **Fin de session** : consigner au `CARNET-DE-BORD.md` selon `AGENTS.md` §4.
