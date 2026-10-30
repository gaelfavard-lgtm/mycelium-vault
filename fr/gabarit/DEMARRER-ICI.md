# Démarrer ici — mettre en place le coffre

## Ce qu'il te faut

- **Claude Code**, installé sur ton ordinateur.
- **Python 3**, pour les vérifications automatiques. Si tu ne sais pas s'il est installé, Claude
  vérifiera à l'étape 3.
- Le gabarit a été rodé sous **Windows**. Sur Mac ou Linux il marche aussi, mais Claude devra
  peut-être ajuster une commande.

## Mise en place

1. **Copie le dossier `gabarit`** à l'endroit où tu veux garder ton coffre, et renomme-le comme
   tu veux (par exemple `MonCoffre`). Pour commencer, évite un dossier synchronisé (Google Drive,
   OneDrive, iCloud) : c'est possible, mais il y a des pièges, décrits dans le `README.md`.
2. **Ouvre Claude Code dans ce dossier.** Au premier lancement, il demande si tu fais confiance
   au dossier : réponds oui. C'est ce qui active les vérifications automatiques.
3. **Demande-lui de l'installer**, par exemple :
   *« Lis le README.md et installe ce coffre avec moi : vérifie que Python marche, lance le test
   des vérifications automatiques, puis aide-moi à remplir mon profil. »*
4. **Remplis ton profil avec lui.** Il te pose des questions sur qui tu es et comment tu veux
   travailler, puis remplit les deux fiches de `_contexte/profil`. Elles sont lues à chaque
   conversation.
5. **Ajoute ton premier projet**, par exemple ton appli : *« Crée la fiche de mon projet
   d'application. »* Ensuite, chaque séance commence par la lecture du sommaire et du carnet :
   plus besoin de tout réexpliquer.

## Les trois règles à connaître

- Claude ne fait rien sans ton accord : dis **« vas-y »** quand tu veux qu'il agisse.
- Il ne supprime jamais : il met dans `a-supprimer`, c'est toi qui vides.
- Après chaque action, il note ce qu'il a fait au carnet de bord et met la fiche à jour.

## Commencer petit, et l'adapter à toi

Inutile de remplir tous les dossiers dès le départ. Commence avec **un seul projet**, celui sur
lequel tu travailles, et laisse le coffre grandir au fil des séances.

Les règles du gabarit sont les miennes : un point de départ, pas un mode d'emploi figé. **Tu vas
les modeler à ton image.** Quand une façon de faire ne te convient pas, dis-le à Claude : il
corrige la règle. Quand un problème revient une deuxième fois, vous écrivez ensemble la règle qui
manque. Les règles s'ajoutent ainsi **petit à petit**, nées de ton usage réel, et le coffre finit
par te ressembler.

## Confidentialité

Avec le temps, le coffre contiendra ta vie ou ton projet en détail. **Ne le publie pas**, et n'y
mets **ni mot de passe ni clé d'accès** : un dossier lu par une IA n'est pas un coffre-fort.

## Pour aller plus loin

Pour lire les fichiers toi-même, **Obsidian** (gratuit, obsidian.md) les rend plus agréables :
ouvre le dossier comme un coffre.

Le détail technique (scripts, réglages, pièges) est dans `README.md`. L'histoire de ces règles,
et pourquoi elles existent, est dans le dossier parent : commence par son `README.md`.
