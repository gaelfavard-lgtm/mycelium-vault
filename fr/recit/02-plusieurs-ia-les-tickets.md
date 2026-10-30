# 2. Plusieurs IA, un seul coffre : les tickets

## Le problème : toutes les IA n'ont pas les mêmes droits

Gaël ne travaille pas qu'avec moi dans Claude Code sur son PC. Selon le moment, il utilise :
- Claude Code sur l'ordinateur, qui peut tout faire dans le coffre ;
- Claude sur le téléphone, ou dans « Cowork » (le mode agent de l'application Claude) ;
- ChatGPT, qui passe par sa connexion à Google Drive.

Toutes ces IA lisent le coffre. Mais celles qui passent par une connexion à Google Drive, depuis le
téléphone notamment, ont moins de droits. Dès le 10 août, nous l'avions noté ; le 14 août, nous avons
précisé la limite : **elles peuvent lire, créer un fichier et le déplacer, mais pas modifier un
fichier existant.** Or presque tout le travail dans un coffre consiste à modifier des fiches : ajouter
une ligne, corriger un statut, noter une décision.

## Une seule règle du jeu, pour toutes

Les consignes étaient éparpillées : une partie dans `CLAUDE.md`, que seul Claude lit, une partie dans
des fiches, une partie dans la mémoire propre à ChatGPT. Chaque IA avait sa version.

Un fichier **`AGENTS.md`** existait déjà. Le 16 août, il est devenu **la source unique des règles**,
valable pour toute IA. `CLAUDE.md` ne fait plus que dire « lis `AGENTS.md` ». En cas de désaccord
entre deux textes, `AGENTS.md` l'emporte. Et Gaël reste au-dessus de tout.

Quelques jours plus tôt, le 10 août, nous avions importé la mémoire que ChatGPT avait accumulée sur
Gaël. Environ 80 % était déjà dans le coffre, et une partie du reste était **fausse** : un animal de
la maison qui n'existait pas, des règles de nommage de fichiers à l'envers. Règle posée : **le coffre
fait foi, la mémoire d'une IA non.**

## Le déboire qui a créé le rituel de démarrage

Le 16 août, une session a vu dans sa liste un outil nommé `update_file` (« modifier un fichier ») et
a annoncé : **« accès complet »**. Elle ne l'avait pas essayé. C'était faux, et Gaël a dû retirer la
demande qu'il venait de lancer sur cette base.

Depuis, chaque session commence par **vérifier réellement** ce qu'elle peut faire : lire, créer,
déplacer, modifier. En cas de doute, elle essaie sur un petit fichier témoin prévu pour ça
(`_test_claude.txt`). On ne déduit rien du nom d'un outil. Et dans le doute, on annonce le niveau
d'accès le plus bas.

## L'invention : les tickets

Une IA qui ne peut pas modifier le coffre pourrait simplement s'arrêter. Mais alors, tout ce qu'elle
a appris dans la conversation serait perdu.

Des sessions sur téléphone avaient déjà pris l'habitude de déposer des fiches dans la boîte d'entrée
pour qu'on les range plus tard. Le 10 août, nous avons mis cette pratique par écrit. C'est **le
ticket** :

1. L'IA à accès limité **ne touche à rien.** À la place, elle crée un fichier dans la boîte d'entrée
   `0-Inbox/`. Elle le dépose **d'office** : elle n'annonce pas sa limite et ne demande pas s'il faut
   un ticket — c'est une règle de Gaël, qui ne veut pas arbitrer la plomberie.
2. Ce ticket décrit **exactement** l'opération voulue : quel fichier, quelle section, et **le texte
   exact** à insérer ou à remplacer.
3. Au démarrage suivant, une session qui a l'accès complet **traite tous les tickets avant toute
   autre demande**, note ce qu'elle a fait dans le carnet, puis déplace le ticket vers la corbeille
   `à supprimer/`.
4. Un **registre**, `tickets-traites.md`, garde la trace de ce qui a été fait. Un ticket qui y figure
   ne se retraite jamais.

Voici à quoi ressemble un ticket (exemple inventé) :

```markdown
# Ticket — ajouter la pièce à commander pour la tondeuse

Cible : 2-Casquettes/outillage/tondeuse.md
Opération : remplacer la section « ## Pièce à commander »
Nouveau contenu :
## Pièce à commander
- Courroie réf. 1234-567, 18,90 € chez le fournisseur A (prix vérifié le 19/08)
```

Et voici à quoi ressemble le registre (exemple inventé, sur le modèle du vrai) :

| Ticket | Ce qui a été fait |
|---|---|
| `ticket-tondeuse-v1.md` | **Obsolète**, remplacé par la v2. Non appliqué. |
| `ticket-tondeuse-v2.md` | Section remplacée, entrée au carnet. |
| `ticket-debroussailleuse.md` | Appliqué **en version corrigée** : le ticket disait une pièce usée, une mesure faite depuis sur la machine dit le contraire. |

Ces deux cas sont réels :
- le 17 août, dix-sept tickets en attente ont été traités d'un coup : quinze appliqués, et deux
  écartés parce que c'étaient d'anciennes versions d'un même ticket ;
- le 19 août, un ticket avait été écrit à partir d'une première version d'une fiche. Entre-temps, une
  mesure sur la machine l'avait démentie. **La session qui applique un ticket relit la fiche sur le
  disque avant d'écrire** ; elle ne l'applique pas aveuglément.

## Le contournement refusé

Le 14 août, une astuce a été envisagée : puisqu'une IA à accès limité ne peut pas modifier un
fichier, elle peut **en créer un nouveau complet** et mettre l'ancien à la corbeille. Sur le papier,
ça marche.

Gaël l'a refusé. C'est **un écrasement déguisé** : on remplace un fichier sans passer par la voie
prévue, et l'historique des versions de Google Drive est perdu au passage. Une session à accès limité
**ne touche à rien d'autre que son ticket.**

## Ce que les autres en ont dit

Le 18 août, nous avons fait relire tout le dispositif par d'autres IA, qui ne l'avaient pas construit
([chapitre 5](05-la-cure.md)). Leur verdict sur les tickets : *« la vraie invention du coffre »*.
C'est l'un des rares mécanismes que la cure de simplification n'a pas touchés.

Plus tard, le 28 août, la distinction entre « ticket » et « note » a disparu : **un fichier dans la
boîte d'entrée se traite, quel que soit son nom.** Les notes dictées au téléphone passent par le même
chemin ([chapitre 3](03-appli-mycelium.md)).

## Les limites

- **Une session sur le téléphone ne laisse aucune trace sur le PC.** Si elle oublie de déposer un
  ticket, ce qu'elle a appris est perdu.
- **Le registre doit être tenu.** Le 4 septembre, nous avons découvert qu'il n'avait pas bougé depuis
  le 27 août : sept tickets attendaient dans la boîte d'entrée, jamais traités.
- **Cowork ne charge pas les réglages du coffre** ; voir le [chapitre 9](09-pieges-de-claude-code.md).

---
[← Chapitre 1](01-le-depart.md) · [Sommaire](../README.md) · [Chapitre 3 →](03-appli-mycelium.md)
