# `1-Projets/` — ce qui a un début et une fin

Question filtre : **« ça fait avancer un livrable ? »** Un projet = un dossier = **une fiche
obligatoire** (`projet-<nom>.md`) avec objectif et statut daté. Quand le projet est fini et que
l'utilisateur le dit, le dossier part **d'un bloc** dans `4-Archives/`.

Une date décidée s'écrit dans le nom : `voyage-avril-2027`, `chantier-3-au-8-septembre-2026` ;
une date pressentie : `voyage-avril-2027-a-confirmer`. Rien d'arrêté : pas de date.

## Modèle de fiche — la carte en tête (40 lignes de base)

```markdown
# Projet — <nom>

## Carte (≤ 40 lignes)
**À quoi il sert** : <une phrase>
**Garde-fous** : <ce qu'il ne faut jamais faire sur ce projet>
**Où on en est** (JJ/MM) : <l'état, daté>
**Où trouver quoi** : <liens vers le détail>
— fin de carte —

## À préciser
## Détail
## Historique
```

L'IA lit la carte jusqu'à « — fin de carte — » et n'ouvre le détail que si le sujet l'exige.
