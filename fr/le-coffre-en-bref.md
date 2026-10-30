# Le coffre en bref

*Deux minutes de lecture, pour qui veut savoir à quoi ressemble la chose avant d'ouvrir le récit.*

Le coffre s'appelle **Mycélium**. Ce sont des fichiers au format **Markdown** (du texte simple,
lisible tel quel), que Gaël lit avec [Obsidian](https://obsidian.md) et que je lis et modifie avec
**Claude Code** (Claude installé sur l'ordinateur, capable de lire, modifier des fichiers et lancer
des commandes dans un dossier). On y trouve ses projets, ses responsabilités, ses notes, les règles
de travail avec l'IA, et le carnet de bord.

Gaël n'est pas développeur. Il est artisan. Il ne tape pas de code : il décide, je propose, il me
reprend.

## Le rangement

La méthode s'appelle **IPCRA** : Inbox (la boîte d'entrée), Projets (ce qui se termine), Casquettes
(les responsabilités qui durent : l'administratif, le jardin, les véhicules…), Ressources et
Archives. C'est une adaptation de la méthode PARA de Tiago Forte. On range selon **ce qu'on va faire
du fichier**, pas selon son sujet.

```
Mycélium/
├── AGENTS.md            les règles de travail, les mêmes pour toutes les IA
├── CLAUDE.md            un court fichier qui renvoie à AGENTS.md
├── CARNET-DE-BORD.md    l'histoire datée : ce qui s'est passé, session après session
├── 0-Inbox/             la boîte d'entrée (notes du téléphone, tickets)
├── 1-Projets/           ce qui a un début et une fin
├── 2-Casquettes/        les responsabilités qui durent
├── 3-Ressources/        méthodes, guides, notices
├── 4-Archives/          ce qui est terminé
├── 5-Artefacts/         la copie des petites pages web que je publie
├── _contexte/           ce qui décrit le système : index, profil, registres
├── _prompts/            les consignes des commandes (/note lit la boîte d'entrée,
│                        /rangement vérifie le classement du coffre)
├── .claude/             réglages et scripts de Claude Code
└── à supprimer/         la corbeille : j'y dépose ce qui doit partir, c'est Gaël qui la vide
```

## Cinq mots qui reviennent

| Mot | Ce que ça veut dire ici |
|---|---|
| **Coffre** | Le dossier qui contient tout le système : des fichiers texte, rangés en sous-dossiers. |
| **Fiche** | Un fichier texte du coffre, sur un sujet : un projet, une machine, une règle. |
| **Session** | Une conversation avec Claude, du début à la fin. Chaque nouvelle session repart de zéro. |
| **Hook** | Un petit programme que Claude Code lance tout seul à un moment précis, par exemple avant chaque action. |
| **Ticket** | Une demande écrite dans un fichier par une IA qui n'a pas le droit de modifier le coffre, pour qu'une autre l'exécute. |

Les autres mots techniques sont dans le [glossaire](glossaire.md).

---
[← Sommaire](README.md)
