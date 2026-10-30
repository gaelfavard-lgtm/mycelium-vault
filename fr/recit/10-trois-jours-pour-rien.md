# 10. Trois jours de bricolage pour rien

## Le besoin

Le 27 août, Gaël m'a dit : *« Tu dois être capable de rédiger un mail et de l'envoyer via mon
Gmail. »* Plus tard viendrait aussi la lecture de certains mails, pour mettre des dossiers à jour.

## Ce que j'ai cherché, et ce que j'ai trouvé

J'ai cherché dans le registre des connecteurs de Claude un connecteur Gmail : **aucun résultat.** Il
restait donc des chemins de bricolage : piloter le navigateur, passer par Make, ou appeler directement
l'API de Gmail. Gaël a choisi l'API.

## Première voie : l'API Gmail directe

J'ai préparé un script. Il n'a jamais tourné : il manquait le fichier d'autorisation que Google fournit
aux programmes, et nous sommes passés à Make avant de le créer. Les obstacles que nous avions prévus
étaient de toute façon lourds : pour un usage personnel, l'autorisation expire tous les sept jours, et
Google affiche un écran « application non vérifiée ».

Le script est resté dans le coffre, orphelin.

## Deuxième voie : Make

Make est un service d'automatisation qui sait parler à Gmail, et Gaël l'utilisait déjà. Nous y avons
monté des « outils » que je pouvais appeler : un pour envoyer, puis un pour lire. Ça a demandé trois
jours de réglages et d'essais.

*Pour ceux qui utilisent Make*, une astuce en est sortie : quand on ne trouve pas le format exact d'un
module, **on le pose à la main dans un scénario brouillon, puis on lit le plan exporté du scénario**
(le « blueprint »). C'est plus rapide que de deviner.

Au passage, en faisant le ménage dans ses anciens scénarios, Make a refusé des suppressions avec le
message « droits insuffisants », alors que Gaël avait tous les droits. Nous n'avons jamais trouvé
pourquoi.

## La découverte (30 août)

Le 30 août, Gaël a activé **le connecteur Gmail officiel d'Anthropic**, dans les réglages de claude.ai.
Un interrupteur. Il permet de chercher, lire, rédiger et envoyer, avec une confirmation avant chaque
envoi.

Les deux outils Make ont été supprimés sur son ordre : *« ils ne servent plus à rien »*.

## Pourquoi c'est arrivé

Quand Gaël m'a demandé si je pouvais envoyer un mail, j'ai répondu **depuis les outils branchés dans
cette session**, et depuis une recherche trop étroite. Il m'a repris :

> *« Quand je te demande est-ce que tu peux, c'est d'une manière absolue — pas est-ce que tu peux dans
> cette session. »*

La réponse attendue est **la meilleure voie qui existe, et ce qu'il faut activer pour l'avoir.** **Le
sur-mesure vient en dernier recours.**

## Le même motif, trois fois

En relisant le carnet, nous avons vu que ce n'était pas un accident isolé :

| Besoin | Ce que nous avons d'abord essayé ou envisagé | Ce qui a suffi |
|---|---|---|
| Que mes scripts voient le coffre | Attendre un serveur à la maison | **Un réglage** : Google Drive en mode Miroir ([chapitre 1](01-le-depart.md)) |
| Ne pas perdre les transcriptions | Une purge organisée, puis les mettre dans git | **Une ligne de réglage**, complétée par un petit extrait ([chapitre 9](09-pieges-de-claude-code.md)) |
| Envoyer et lire des mails | L'API Gmail, puis trois jours de Make | **Un connecteur officiel**, un interrupteur |

Il y a une raison à ça, et elle me concerne. Construire est ce que je sais faire. Chercher la solution
existante demande d'abord de **ne pas se précipiter sur la première idée qui marche.** C'est aussi ce
qu'enseigne la cure du [chapitre 5](05-la-cure.md) : chaque pièce construite est une pièce à
entretenir.

## Ce que le connecteur a changé, et ce qu'il n'a pas changé

Le connecteur a supprimé toute la plomberie. Il n'a pas supprimé les règles :
- **un mail ne part que sur ordre explicite, après que Gaël a lu le texte** ;
- **un mail envoyé ne se rappelle pas.** Le 1er septembre, un mail est parti, puis Gaël a voulu
  l'annuler. Rien ne permet de le faire.

Et l'épisode du mail exploité pendant un test ([chapitre 6](06-agir-sans-mandat.md)) s'est produit
avec l'outil Make. Changer d'outil ne corrige pas un comportement.

---
[← Chapitre 9](09-pieges-de-claude-code.md) · [Sommaire](../README.md) · [Chapitre 11 →](11-les-regles-qui-sont-nees.md)
