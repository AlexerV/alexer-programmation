# 📜 Commandes utiles sous Linux

Ce document rassemble les commandes essentielles pour utiliser efficacement un terminal Linux (WSL ou autre), ainsi qu’une explication détaillée de la gestion des **droits d’accès avec `chmod`**.

> Ce guide est destiné aux débutants comme aux utilisateurs intermédiaires souhaitant se rafraîchir la mémoire.

---

## 📌 Sommaire

1. [Commandes de base](#commandes-de-base)
2. [Gestion des droits avec `chmod`](#gestion-des-droits-avec-chmod)
   - [Types d'utilisateurs](#types-dutilisateurs)
   - [Types de droits](#types-de-droits)
   - [Correspondances binaire/octale](#correspondances-binaire--octale)
   - [Exemple complet](#exemple-complet)
   - [Valeurs courantes](#valeurs-courantes)
   - [Lire les droits d’un fichier](#lire-les-droits-dun-fichier)
   - [Format des droits](#format-des-droits)

---

## 🧰 Commandes de base

| Commande        | Description |
|-----------------|-------------|
| `ls`            | Lister le contenu d’un répertoire |
| `pwd`           | Afficher le répertoire de travail actuel |
| `cd`            | Changer de répertoire (`cd home/`) |
| `cp`            | Copier des fichiers ou répertoires (`cp fichier`) |
| `rm`            | Supprimer un fichier ou dossier (`rm fichier`, `rm -r dossier`) |
| `mv`            | Déplacer ou renommer (`mv fichier dossier`) |
| `mkdir`         | Créer un répertoire (`mkdir nomDossier`) |
| `man`           | Affiche le manuel d’une commande (`man commande`) |
| `touch`         | Créer un fichier vide (`touch nomFichier`) |
| `chmod`         | Modifier les autorisations d’un fichier |
| `./fichier`     | Exécuter un fichier exécutable |
| `exit`          | Quitter la session terminal |
| `sudo`          | Exécuter en tant que superutilisateur |
| `apt`, `yum`, `pacman` | Gestionnaires de paquets |
| `cat`           | Affiche le contenu d’un fichier |
| `ps`            | Affiche les processus en cours |
| `history`       | Affiche l’historique des commandes |
| `tail`          | Affiche les dernières lignes d’un fichier |
| `head`          | Affiche les premières lignes d’un fichier |
| `grep`          | Recherche une chaîne dans un fichier |

---

## 🔐 Gestion des droits avec `chmod`

### Types d’utilisateurs

- **u** – utilisateur (propriétaire du fichier)
- **g** – groupe (utilisateurs appartenant au même groupe)
- **o** – autres (tout le reste)
- **a** – tous les utilisateurs (user + group + others)

### Types de droits

| Lettre | Droit       | Description              |
|--------|-------------|--------------------------|
| `r`    | read        | Lire un fichier          |
| `w`    | write       | Modifier un fichier      |
| `x`    | execute     | Exécuter un fichier      |

---

### Correspondances binaire / octale

| Binaire | Octal | Droits | Signification                  |
|---------|-------|--------|--------------------------------|
| 000     | 0     | ---    | Aucun droit                    |
| 001     | 1     | --x    | Exécution                      |
| 010     | 2     | -w-    | Écriture                       |
| 011     | 3     | -wx    | Écriture + Exécution           |
| 100     | 4     | r--    | Lecture                        |
| 101     | 5     | r-x    | Lecture + Exécution            |
| 110     | 6     | rw-    | Lecture + Écriture             |
| 111     | 7     | rwx    | Lecture + Écriture + Exécution |

---

### Exemple complet

Accorder les droits suivants à un fichier :

| Utilisateur     | Droits       | Binaire | Octal |
|-----------------|--------------|---------|-------|
| Propriétaire    | rwx          | 111     | 7     |
| Groupe          | r-x          | 101     | 5     |
| Autres          | --x          | 001     | 1     |

Commande à exécuter :
```bash
sudo chmod 751 monFichier
```

### Valeurs courantes
| Valeur | Description                                                                   |
| ------ | ----------------------------------------------------------------------------- |
| `644`  | Propriétaire : lecture/écriture ; autres : lecture                            |
| `666`  | Tout le monde : lecture/écriture (**déconseillé**)                            |
| `700`  | Propriétaire : tous les droits ; autres : aucun                               |
| `705`  | Propriétaire : tous les droits ; autres : lecture/exécution                   |
| `755`  | Propriétaire : tous les droits ; autres : lecture/exécution                   |
| `764`  | Propriétaire : tous les droits ; groupe : lecture/écriture ; autres : lecture |
| `774`  | Propriétaire + groupe : tous les droits ; autres : lecture                    |
| `775`  | Propriétaire + groupe : tous les droits ; autres : lecture + exécution        |
| `777`  | Tout le monde : tous les droits (**fortement déconseillé**)                   |

---

### Lire les droits d’un fichier

```bash
ls -l monFichier
```

Cela retourne une ligne comme :

```vbnet
-rwxr-x--x  1 user group 1234 date monFichier
```

Colonnes du résultat
| Colonne | Signification                           |
| ------- | --------------------------------------- |
| 1       | Type de fichier + droits (`-rwxr-x--x`) |
| 2       | Nombre de liens                         |
| 3       | Propriétaire                            |
| 4       | Groupe                                  |
| 5       | Taille (en octets)                      |
| 6–8     | Date et heure                           |
| 9       | Nom du fichier                          |

---

### Format des droits (1ère colonne `ls -l`)

Le format est toujours de 10 caractères :

- 1er caractère : type de fichier

  - `-` : fichier

  - `d` : dossier

  - `l` : lien symbolique

- 9 suivants : droits en triplets (utilisateur, groupe, autres)

  - Ex : `rwxr-x--x`
