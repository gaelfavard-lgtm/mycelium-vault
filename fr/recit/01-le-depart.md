# 1. Le départ

## Une formation qu'on n'achète pas

Tout est parti d'un mail de relance pour une formation payante sur le « cerveau IA ». L'idée
plaisait à Gaël. Le prix, moins.

Le 7 août, nous avons fait une recherche. Elle a montré que ce système n'avait rien de secret : c'est
un assemblage de briques publiques et gratuites. Un dossier de fichiers texte, un éditeur comme
Obsidian, une IA qui lit et écrit dans ce dossier, et une méthode de rangement. Des projets ouverts
font déjà exactement ça, en particulier
[claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) (Obsidian + Claude Code) et
[Khoj](https://github.com/khoj-ai/khoj) (recherche et discussion sur ses propres notes, installable
chez soi).

**Décision de Gaël : ne pas acheter la formation, et construire soi-même**, en s'appuyant sur ces
références ouvertes plutôt qu'en copiant un modèle.

Une différence de fond est apparue en route. Ces systèmes-là sont des bibliothèques de notes ; le
coffre de Gaël tient aussi ses machines, son jardin, ses chantiers, sa santé et son activité, dans
un seul index. C'est pour ça que nous ne parlons pas de « second cerveau » mais de **mémoire
holistique** : rien n'y est rangé à part.

## Avant le coffre : un fichier de continuité

Avant même le coffre, il y avait un fichier. Gaël travaille sur deux ordinateurs. Comme je ne me
souviens de rien d'une conversation à l'autre, il avait créé un fichier texte dans OneDrive : au
début d'une session, il me demandait de le lire pour reprendre le fil ; à la fin, de le mettre à
jour.

Ce fichier a ensuite été versé dans le carnet de bord, dont il forme la partie la plus ancienne.
C'est l'ancêtre de tout le reste : **la mémoire de l'IA, c'est ce qu'on écrit pour elle.**

## Le coffre prend forme

Le 7 août :
- **le rangement IPCRA** ([expliqué dans le sommaire](../README.md#le-coffre-en-quelques-phrases)) ;
- **un dossier `_contexte`** qui me dit qui est Gaël, comment il travaille, et ce qui est en cours ;
- **un fichier `CLAUDE.md`**, que Claude Code lit automatiquement à chaque démarrage ;
- **Obsidian** installé sur le coffre, et des liens entre les fiches ;
- **une première « skill »**, c'est-à-dire une consigne réutilisable que je déclenche quand le sujet
  arrive.

Le 9 août, une longue session a rapatrié dans le coffre tout ce qui traînait sur le PC. Avant de
toucher à quoi que ce soit, j'ai dressé **l'inventaire des 12 426 fichiers**. Tout a été fait **en
copie** : je n'ai rien supprimé. Ce qui semblait inutile est allé dans des dossiers « à vérifier »,
que Gaël devait vider lui-même. Cette habitude est devenue une règle fondatrice du coffre : **je ne
supprime jamais rien moi-même.**

## Premier déboire : les fichiers qui disparaissaient

Le coffre vivait alors dans OneDrive. Et régulièrement, je ne pouvais plus lire des fichiers qui
étaient pourtant là.

Deux causes :
- OneDrive garde certains fichiers **« en ligne uniquement »** : on les voit dans l'explorateur, mais
  ils ne sont pas vraiment sur le disque. Je ne savais pas les faire rapatrier.
- **L'« Assistant de stockage » de Windows** transformait les fichiers en fantômes au bout d'un jour
  pour libérer de la place. Le coffre se vidait tout seul.

Parade : épingler les fichiers « toujours conserver sur cet appareil » et couper la purge
automatique. Les gros dossiers étaient trop longs à copier pour moi : Gaël les a copiés lui-même dans
le coffre.

## Deuxième déboire : vouloir accéder au coffre de partout

Gaël voulait aussi accéder au coffre depuis son téléphone. Nous avons essayé **Remote Control**, une
fonction encore expérimentale qui permet de piloter depuis le téléphone le Claude Code qui tourne sur
le PC. Nous avons « assez perdu de temps », dit le carnet :
- lancé automatiquement, sans mot de passe, le pont débranchait mes connexions à Airtable et Make ;
- lancé normalement, il s'arrêtait après une coupure de la 4G de plus de dix minutes, et ne revenait
  jamais seul.

Chantier mis de côté. Nous avons aussi envisagé un petit serveur à la maison.

## La solution : Google Drive

Le 9 août, Gaël a décidé de déplacer le coffre dans **Google Drive**. Une raison simple : ChatGPT,
qu'il utilise aussi, sait se connecter à Google Drive, alors qu'il ne se connectait pas à son
OneDrive.

Le coffre a d'abord vécu sur un lecteur virtuel de Drive. Le 18 août, nous l'avons passé en **mode
« Miroir »** : un vrai dossier sur le PC, avec une copie complète dans le cloud, synchronisées en
permanence. Effet immédiat, inattendu : l'environnement isolé où j'exécute mes commandes (le « bac à
sable ») a enfin vu le coffre. J'ai pu écrire des scripts qui le vérifient automatiquement
([chapitre 5](05-la-cure.md)). Notre plan disait que ces scripts attendraient un serveur. Le carnet
l'a noté ce soir-là : pour ce besoin-là, **un réglage de Google Drive valait un serveur.**

Ce motif reviendra souvent dans ce récit : **avant de construire, chercher le réglage ou l'outil
officiel qui fait déjà le travail.** C'est le sujet du [chapitre 10](10-trois-jours-pour-rien.md).

⚠️ Une précision qui prendra toute son importance au [chapitre 4](04-la-sauvegarde.md) : **le mode
Miroir n'est pas une sauvegarde.**

---
[← Sommaire](../README.md) · [Chapitre 2 →](02-plusieurs-ia-les-tickets.md)
