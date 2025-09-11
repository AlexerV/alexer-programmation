# 📜 Commandes utiles sous Linux

Ce document rassemble les commandes essentielles pour utiliser efficacement un terminal Linux (WSL ou autre), ainsi qu’une explication détaillée de la gestion des **droits d’accès avec `chmod`**.

> Ce guide est destiné aux débutants comme aux utilisateurs intermédiaires souhaitant se rafraîchir la mémoire.

---

## 📌 Sommaire

1. [Commandes de base](#🧰-commandes-de-base)
2. [Navigation & gestion de fichiers](#navigation--gestion-de-fichiers)
3. [Manipulation de texte](#manipulation-de-texte)
4. [Système & processus](#système--processus)
5. [Réseau](#réseau)
6. [Gestion des droits avec `chmod`](#gestion-des-droits-avec-chmod)
   - [Types d'utilisateurs](#types-dutilisateurs)
   - [Types de droits](#types-de-droits)
   - [Correspondances binaire/octale](#correspondances-binaire--octale)
   - [Exemple complet](#exemple-complet)
   - [Valeurs courantes](#valeurs-courantes)
   - [Lire les droits d’un fichier](#lire-les-droits-dun-fichier)
   - [Format des droits](#format-des-droits)

---

## 🧰 Commandes de base

| Commande                  | Description |
|---------------------------|-------------|
| `ls` / `ls -l` / `ls -a` | Lister le contenu d’un répertoire (+ détails / fichiers cachés) |
| `pwd`                     | Afficher le répertoire de travail actuel |
| `cd chemin`               | Changer de répertoire (`cd ..` = remonter, `cd -` = précédent) |
| `cp fichier1 fichier2`    | Copier un fichier |
| `rm fichier`              | Supprimer un fichier |
| `rm -r dossier`           | Supprimer un dossier et son contenu |
| `rm -rf dossier` ⚠️       | Suppression forcée et récursive (**dangereux**) |
| `mv source cible`         | Déplacer ou renommer |
| `mkdir nomDossier`        | Créer un répertoire |
| `man commande`            | Afficher le manuel d’une commande |
| `touch nomFichier`        | Créer un fichier vide |
| `cat fichier`             | Afficher le contenu d’un fichier |
| `./fichier`               | Exécuter un fichier exécutable |
| `exit`                    | Quitter la session terminal |
| `sudo commande`           | Exécuter en tant que superutilisateur |
| `apt install paquet`      | Installer un paquet (Ubuntu/Debian) <br> *(autres distributions : `yum`, `pacman`)* |
| `history`                 | Afficher l’historique des commandes |

---

## 📂 Navigation & gestion de fichiers

| Commande          | Description |
|-------------------|-------------|
| `tree`            | Afficher l’arborescence (si installé) |
| `stat fichier`    | Détails complets sur un fichier |
| `lsblk`           | Lister les périphériques de stockage |
| `df -h`           | Espace disque utilisé/libre |
| `du -sh dossier`  | Taille d’un dossier |

---

## 📑 Manipulation de texte

| Commande                 | Description |
|--------------------------|-------------|
| `less fichier`           | Lire un fichier page par page |
| `head fichier`           | Afficher les premières lignes |
| `tail fichier`           | Afficher les dernières lignes |
| `tail -f fichier.log`    | Suivre un fichier en temps réel |
| `grep "mot" fichier`     | Rechercher un mot |
| `grep -r "mot" dossier`  | Recherche récursive |
| `nano fichier`           | Éditer un fichier (éditeur simple) |
| `vim fichier`            | Éditer un fichier (éditeur avancé) |
| `echo "texte" >> fichier`| Ajouter du texte à un fichier |

---

## ⚙️ Système & processus

| Commande            | Description |
|---------------------|-------------|
| `ps`                | Afficher les processus en cours |
| `top`               | Surveiller les processus (en temps réel) |
| `htop`              | Version améliorée de `top` (si installé) |
| `kill PID`          | Tuer un processus par son ID |
| `kill -9 PID` ⚠️    | Forcer l’arrêt d’un processus |
| `uname -a`          | Infos système |
| `whoami`            | Nom de l’utilisateur courant |
| `uptime`            | Depuis combien de temps le système tourne |

---

## 🌐 Réseau

| Commande            | Description |
|---------------------|-------------|
| `ping site.com`     | Tester la connexion réseau |
| `curl url`          | Télécharger ou requêter une ressource |
| `wget url`          | Télécharger un fichier |
| `ifconfig` / `ip a` | Afficher les interfaces réseau |
| `netstat -tulnp`    | Ports et connexions en écoute |

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
