# Glossaire

**`AGENTS.md`** — Le fichier des règles de travail du coffre, valable pour toutes les IA.

**Agent / sous-agent** — Une IA à qui une autre IA confie une tâche précise (par exemple lire une partie
du coffre), et qui rend son résultat.

**Airtable** — Une base de données en ligne qui ressemble à un tableur.

**API** — La porte d'entrée qu'un service (Gmail, Airtable…) ouvre aux programmes, pour qu'ils lisent ou
modifient des données sans passer par l'écran.

**Apps Script** — Un service gratuit de Google pour écrire de petits programmes hébergés sur son compte
Google, capables de lire et d'écrire dans Drive.

**Artifact** — Une petite page web que Claude publie, hébergée chez Anthropic (un plan, un formulaire,
une application de décision).

**Audit** — Une inspection de tout le coffre pour trouver ce qui est mal rangé, cassé ou périmé.

**Bac à sable (sandbox)** — L'environnement isolé où l'IA exécute ses commandes, sans accès au reste de
l'ordinateur sauf ce qu'on lui autorise.

**BOM** — Une marque invisible au début d'un fichier texte, qui indique son encodage.

**Calibration** — Le fait qu'une probabilité annoncée corresponde à la réalité : sur cent choses
annoncées « à 90 % », environ quatre-vingt-dix doivent se vérifier.

**Carnet de bord** — Le fichier `CARNET-DE-BORD.md` : l'histoire datée du coffre, écrite par chaque
session pour la suivante.

**Casquette** — Dans la méthode IPCRA, une responsabilité qui dure (l'administratif, le jardin, les
véhicules), par opposition à un projet qui se termine.

**Claude Code** — Claude installé sur l'ordinateur, capable de lire, modifier des fichiers et lancer des
commandes dans un dossier.

**Coffre** — Le dossier de fichiers texte qui contient tout le système.

**Connecteur (MCP)** — Un branchement entre Claude et un service extérieur (Gmail, Google Drive,
Airtable). MCP est le nom du protocole utilisé.

**Cowork** — Le mode agent de l'application Claude, qui peut travailler sur un dossier connecté.

**CRLF** — La façon dont Windows marque la fin d'une ligne dans un fichier texte. Linux utilise une autre
marque.

**Fiche** — Un fichier texte du coffre, sur un sujet : un projet, une machine, une règle.

**Git** — Un outil libre qui garde toutes les versions successives d'un dossier et permet de revenir à
n'importe laquelle.

**Hook** — Un petit programme que Claude Code lance automatiquement à un moment précis : avant l'usage
d'un outil, à la fin d'une réponse, à la fin d'une session.

**Inbox / boîte d'entrée** — Le dossier où arrivent les notes et les tickets avant d'être traités.

**Instantané** — Un fichier écrit avant une modification de masse, qui contient l'état d'avant et le
chemin pour revenir en arrière. Il remplace l'annulation, qu'une API n'offre pas.

**IPCRA** — La méthode de rangement du coffre : Inbox, Projets, Casquettes, Ressources, Archives.

**`.jsonl`** — Le format des fichiers où Claude Code enregistre ses sessions : du texte, une ligne par
événement.

**Make** — Un service en ligne d'automatisation qui relie des applications entre elles.

**Markdown** — Un format de texte simple, lisible tel quel, où `**gras**` s'écrit avec des étoiles et
`# Titre` avec un dièse.

**Mémoire holistique** — Le nom que nous donnons au coffre : une mémoire où les domaines ne sont pas
séparés (les machines, le jardin, la santé, l'activité), par opposition à la bibliothèque de notes
qu'on appelle d'ordinaire un « second cerveau ».

**`MEMORY.md`** — L'index du coffre : une ligne par sujet, lu par Claude à chaque démarrage.

**Miroir (Google Drive)** — Un mode de Google Drive où le dossier existe en entier sur l'ordinateur
**et** dans le cloud, synchronisé en permanence dans les deux sens.

**Obsidian** — Un logiciel gratuit pour lire et relier des fichiers Markdown.

**PARA** — Une méthode de rangement créée par Tiago Forte (Projets, Domaines, Ressources, Archives), dont
IPCRA est une adaptation.

**Planificateur de tâches** — L'outil de Windows qui lance un programme à heure fixe ou à un événement
(ouverture de session, par exemple).

**Session** — Une conversation avec Claude, du début à la fin. Chaque session repart de zéro.

**Skill / commande** — Une consigne réutilisable. Une skill se déclenche quand le sujet arrive ; une
commande se lance en tapant son nom (`/note`).

**Softr** — Un service qui fabrique des pages web à partir d'une base Airtable, sans code.

**Ticket** — Un fichier déposé dans la boîte d'entrée par une IA qui n'a pas le droit de modifier le
coffre, et qui décrit exactement la modification à faire.

**Token** — L'unité dans laquelle une IA lit et écrit le texte (environ trois quarts de mot). Tout ce
qu'elle lit a un coût en tokens.

**Transcription** — L'enregistrement complet d'une session : messages, outils appelés, résultats.

**Webhook** — Une adresse web qui reçoit automatiquement des données quand quelque chose se passe
ailleurs.

---
[← Sommaire](README.md)
