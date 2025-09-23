# Bash / Shell

---

## Indicateur de script (shebang)

À mettre en première ligne d’un script pour indiquer quel interpréteur utiliser :

```bash
#!/bin/bash
```

---

## Exécution d’un script bash

```bash
$ sudo chmod 755 fichier.sh      # Donner les droits d’exécution (lecture, écriture, exécution)
$ ./fichier.sh                   # Exécuter le script
```

---

## Déclaration de variables

```bash
var1=a
var2="texte"
var3="texte avec espaces"
var4=55
var5=$var1           # Affecte la valeur de var1 à var5
var6=$0              # Valeur spéciale : nom du script
```

Affichage :

```bash
echo -e "valeur de var1: $var1\nvaleur de var2: $var2\nvaleur de var3: $var3\nvaleur de var4: $var4\nvaleur de var5: $var5\nvar6: $var6"
```

---

## Variables avancées
### Variables d’environnement : utilisées par le shell et les programmes lancés depuis le script
```bash
export MON_ENV="valeur"
echo $MON_ENV
```
> Utile pour partager des valeurs entre plusieurs scripts ou commandes.

### Variables readonly (non modifiables) : empêchent toute modification après déclaration
```bash
readonly PI=3.14
```
> Bon pour protéger les constantes dans vos scripts.

### Variables avec valeur par défaut : pratique si une variable n’est pas définie
```bash
echo ${VAR:-"valeur_par_defaut"}
```
> Si `VAR` n’existe pas, le shell utilise `"valeur_par_defaut"`.

### Substitution de commande : stocke le résultat d’une commande dans une variable.
```bash
date=$(date)
echo "La date actuelle est : $date"
```
> Permet de récupérer dynamiquement des infos système.

---

## Opérations arithmétiques

```bash
expr 3 + 5       # Affiche 8
expr $a \* $b    # Multiplie $a et $b (ex: 3 * 2)
```
> Note : L’astérisque doit être échappé avec un backslash `\*` ou placé entre guillemets `"*"`.

---

## Manipulation de chaînes
### Accès aux caractères ou sous-chaînes :
```bash
texte="Bonjour"
echo ${texte:0:3}  # "Bon"
```
> Très utile pour extraire une partie d’une chaîne.

### Longueur d’une chaîne :
```bash
texte="Bonjour"
echo ${#texte}  # 7
```
> Permet de vérifier ou limiter la taille d’une entrée utilisateur.

### Remplacement dans une chaîne :
```bash
texte="Bonjour"
echo ${texte/B/j}  # "jonjour"
```
> Pour modifier rapidement un texte sans créer de nouvelles variables.

---

## Saisie utilisateur

```bash
read variable    # Lit une entrée utilisateur dans la variable
```

Exemple 1 :
```bash
echo "Veuillez entrer votre nom : "
read nom
echo "Ton nom est $nom"
```

Exemple 2 (plusieurs variables) :
```bash
echo "Veuillez entrer votre nom et prénom :"
read nom prenom
echo "Tu t'appelles $nom $prenom"
```

---

## Structures conditionnelles

⚠️ Attention à la syntaxe, notamment les espaces entre crochets et conditions.

### If simple
```bash
age=19
if [ "$age" -ge 18 ]; then
  echo "Tu es majeur"
fi
```

### If...else
```bash
age=19
if [ "$age" -ge 18 ]; then
  echo "Tu es majeur"
else
  echo "Tu es mineur"
fi
```

### If...elif...else
```bash
feu="vert"
if [ "$feu" = "rouge" ]; then
  echo "N'avancez pas"
elif [ "$feu" = "orange" ]; then
  echo "Ralentissez"
else
  echo "Allez-y"
fi
```

### Plusieurs conditions
```bash
age=101
if [ "$age" -le 0 ] || [ "$age" -ge 100 ]; then
  echo "L'âge entré n'est pas correct"
fi
```

---

### Opérateurs de comparaison numérique
| Expression | Signification          | Exemple                |
| ---------- | ---------------------- | ---------------------- |
| `-eq`      | égal à                 | `[ "$nombre" -eq 27 ]` |
| `-ne`      | différent de           | `[ "$nombre" -ne 27 ]` |
| `-lt`      | inférieur à (<)        | `[ "$nombre" -lt 27 ]` |
| `-le`      | inférieur ou égal (<=) | `[ "$nombre" -le 27 ]` |
| `-gt`      | supérieur à (>)        | `[ "$nombre" -gt 27 ]` |
| `-ge`      | supérieur ou égal (>=) | `[ "$nombre" -ge 27 ]` |

---

## Case (sélecteur multiple)
```bash
#!/bin/bash
echo "Quel est ton OS préféré ?"
echo "1- Windows  2- Linux  3- Mac OS  4- Autre"
read choix
case "$choix" in
  1) echo "Tu préfères Windows" ;;
  2) echo "Tu préfères Linux" ;;
  3) echo "Tu préfères Mac OS" ;;
  4) echo "Tu préfères un autre OS" ;;
  *) echo "Tu dois taper un nombre entre 1 et 4" ;;
esac
```

---

## Select (menu interactif)
```bash
select systeme in "Windows" "Linux" "BSD" "Mac OS" "MS DOS"; do
  echo "Ton système favori est $systeme"
  break
done
```

---

## Boucles

> En Bash, on choisit une boucle en fonction de la **condition de sortie** et de la **logique de répétition** :
>
- **`while`** : la boucle s’exécute **tant qu’une condition est vraie**.
- **`until`** : la boucle s’exécute **tant qu’une condition est fausse**.
- **`for`** : utilisée pour **répéter un bloc un nombre connu de fois** ou **parcourir une liste**.

### While
```bash
i=1
while [ $i -le 5 ]; do
  echo "Tour de boucle n° $i"
  i=$(expr $i + 1)
done
```

Exemple avec saisie utilisateur :
```bash
continuer=o
while [ "$continuer" = "o" ]; do
  echo "Tu veux recommencer ? o/n"
  read continuer
done
```

---

### Until
```bash
i=1
until [ $i -gt 5 ]; do
  echo "Tour de boucle n° $i"
  i=$(expr $i + 1)
done
```

Avec saisie :
```bash
continuer=o
until [ "$continuer" = "n" ]; do
  echo "Veux-tu recommencer ? o/n"
  read continuer
done
```

---

### For
```bash
echo "Combien tu veux d'étoiles ?"
read nombre
for i in $(seq $nombre); do
  echo -n "*"
done
echo ""
```

---

## Tableaux (arrays)
```bash
fruits=("pomme" "banane" "cerise")
echo ${fruits[0]}         # pomme
echo ${fruits[@]}         # tous les éléments
echo ${#fruits[@]}        # nombre d’éléments

# Parcourir un tableau
for fruit in "${fruits[@]}"; do
  echo "J’aime $fruit"
done
```

### Définition et accès :
```bash
fruits=("pomme" "banane" "cerise")
echo ${fruits[0]}  # pomme
```
> Les tableaux sont très pratiques pour stocker plusieurs valeurs liées.

### Parcours d’un tableau :
```bash
for fruit in "${fruits[@]}"; do
  echo "J’aime $fruit"
done
```
> On peut ainsi traiter tous les éléments sans répéter le code.

---

## Passage de paramètres au script
```bash
#!/bin/bash
echo "Tu as passé les $# paramètres suivants :"
echo "Paramètre 1 : $1"
echo "Paramètre 2 : $2"
echo "Paramètre 3 : $3"
echo "Paramètre 4 : $4"
echo "Tous les paramètres : $*"
```

Exécution :
```bash
$ ./fichier.sh 42 alexer toto 5
# Paramètre 1 = 42 
# Paramètre 2 = alexer
# Paramètre 3 = toto
# Paramètre 4 = 5
# Tous les paramètres : 42 alexer toto 5
```

> Il existe aussi des [Variables Spéciales](cours.md#variables-spéciales--0-1--etc)

---

## Fonctions

```bash
#!/bin/bash

# Déclaration de la fonction
function multiplier() {
  resultat=$(expr $1 \* $2)
  echo $resultat
}

echo "Entrez 2 nombres :"
read nb1
read nb2

multiplier $nb1 $nb2  # Appel de la fonction
```

---

## Fonctions avec retour et paramètres
```bash
function additionner() {
  local somme=$(($1 + $2))
  echo $somme
}

resultat=$(additionner 5 7)
echo "Résultat = $resultat"
```
- `$1` et `$2` sont les paramètres passés à la fonction.
- `local` limite la portée des variables à l’intérieur de la fonction.
- `echo` permet de retourner une valeur et la récupérer avec `$()`.

---

## Tests sur fichiers et répertoires

On peut utiliser des conditions pour vérifier l’existence ou les propriétés d’un fichier ou d’un dossier :

### Exemples de tests

```bash
if [ -f fichier.txt ]; then
  echo "C'est un fichier ordinaire"
fi

if [ -d mon_dossier ]; then
  echo "C'est un répertoire"
fi

if [ -s fichier.txt ]; then
  echo "Le fichier n'est pas vide"
fi

if [ -r fichier.txt ]; then
  echo "Le fichier est lisible"
fi

if [ -w fichier.txt ]; then
  echo "Le fichier est modifiable (écriture autorisée)"
fi

if [ -x script.sh ]; then
  echo "Le fichier est exécutable"
fi

if [ ! -e fichier.txt ]; then
  echo "Le fichier n'existe pas"
fi
```
> ℹ️ Tu peux combiner ces tests avec && ou || pour créer des conditions complexes.

### Récapitulatif des opérateurs de test sur fichiers
| Test         | Signification                  |
| ------------ | ------------------------------ |
| `-f fichier` | Fichier ordinaire              |
| `-d dossier` | Répertoire                     |
| `-e fichier` | Existe (fichier ou dossier)    |
| `-s fichier` | Taille non nulle (non vide)    |
| `-r fichier` | Lisible                        |
| `-w fichier` | Écriture autorisée             |
| `-x fichier` | Exécutable                     |
| `!`          | Négation (ex : `! -e fichier`) |

---

## Gestion des signaux et trap
```bash
trap "echo 'Script interrompu !'; exit" SIGINT

echo "Appuyez sur Ctrl+C pour tester"
while true; do
  sleep 1
done
```
- `trap` intercepte un signal (ex: `Ctrl+C`) et exécute un code.
> Permet de faire un nettoyage ou afficher un message avant que le script ne s’arrête.

---

## Redirections et pipes

### Rediriger la sortie d'une commande

```bash
commande > fichier.txt      # Remplace le contenu
commande >> fichier.txt     # Ajoute à la fin du fichier
```

### Lire un fichier comme entrée

```bash
commande < fichier.txt
```

### Chaîner des commandes avec un pipe

Le pipe permet d’envoyer la sortie d’une commande comme entrée à une autre :

```bash
cat fichier.txt | grep "mot"      # Recherche "mot" dans le fichier
ps aux | grep firefox             # Cherche les processus liés à Firefox
```
> Ces enchaînements sont très puissants pour créer des scripts efficaces et dynamiques.

### Gestion des erreurs
```bash
commande 2> erreur.txt      # Redirige uniquement les erreurs
commande > sortie.txt 2>&1  # Redirige la sortie ET les erreurs dans un seul fichier
```

---

## Redirections avancées
- Rediriger uniquement la sortie standard ou les erreurs :
```bash
commande > sortie.txt       # stdout
commande 2> erreur.txt      # stderr
commande &> tout.txt        # stdout + stderr
```
> Important pour déboguer un script ou conserver un historique.

- Pipe avec `tee` pour afficher et sauvegarder en même temps :
```bash
ls -l | tee fichier.txt
```
> Affiche le résultat à l’écran et l’enregistre dans un fichier simultanément.

---

## Gestion des erreurs et contrôle des retours de commandes

En Bash, il est important de contrôler l'exécution des commandes pour s'assurer qu'elles se passent bien et réagir en cas d'échec. On peut utiliser l'opérateur `||` pour exécuter une commande si la première échoue, et `&&` pour enchaîner une commande qui ne s'exécute que si la première réussit.

Exemple :
```bash
#!/bin/bash

# Si la commande échoue, on affiche un message et on arrête le script
commande || { echo "La commande a échoué"; exit 1; }

# Si la commande réussit, on affiche un message
command1 && echo "Command 1 succeeded" || echo "Command 1 failed"
```

- `commande || { echo "La commande a échoué"; exit 1; }` : Si la commande échoue (c'est-à-dire qu'elle retourne un code de sortie non nul), on affiche un message d'erreur et on arrête le script avec `exit 1`.
- `command1 && echo "Command 1 succeeded" || echo "Command 1 failed"` : Si `command1` réussit, on affiche "Command 1 succeeded", sinon on affiche "Command 1 failed".

---

## `set -e` pour arrêter l'exécution en cas d'erreur

L'option `set -e` fait en sorte que le script s'arrête dès qu'une commande échoue. Cela permet de garantir que le script ne continue pas son exécution avec des résultats incorrects ou imprévus.

Exemple :
```bash
#!/bin/bash
set -e  # Arrête l'exécution en cas d'erreur

echo "Cette commande va échouer"
ls nonexistentfile  # Cette commande échouera
echo "Ce message ne sera jamais affiché"
```

- Si une commande retourne une erreur, le script s'arrête immédiatement. Dans cet exemple, la commande `ls nonexistentfile` échoue, donc le script s'arrête avant d'afficher le dernier message.

---

## Variables spéciales : `$0`, `$1`, `$#`, etc.

Les variables spéciales en Bash permettent d'interagir avec les arguments passés au script. Par exemple :
- `$0` : Nom du script
- `$1`, `$2`, ... : Paramètres passés au script
- `$#` : Nombre de paramètres passés au script
- `$*` : Tous les paramètres passés en tant que chaîne de caractères
- `$@` : Tous les paramètres passés, mais chaque paramètre est séparé.

Exemple :
```bash
#!/bin/bash

echo "Le nom du script est : $0"
echo "Le premier paramètre est : $1"
echo "Le nombre total de paramètres passés est : $#"
echo "Tous les paramètres passés : $*"
```

- Si tu exécutes ce script avec la commande suivante :
```bash
./script.sh param1 param2 param3
```
Tu obtiendras :
```bash
Le nom du script est : ./script.sh
Le premier paramètre est : param1
Le nombre total de paramètres passés est : 3
Tous les paramètres passés : param1 param2 param3
```

---

## Redirection des erreurs et des sorties (stderr, stdout)
En Bash, tu peux rediriger la sortie standard (stdout) et la sortie d'erreur (stderr) vers des fichiers ou d'autres commandes. Cela permet de mieux gérer les logs et les erreurs dans les scripts.

Exemple :
```bash
#!/bin/bash

# Rediriger la sortie standard (stdout) vers un fichier
echo "Ceci est un message normal" > sortie.txt

# Rediriger la sortie d'erreur (stderr) vers un fichier
ls nonexistentfile 2> erreur.txt

# Rediriger stdout et stderr dans le même fichier
ls nonexistentfile &> tout.txt
```

- `> sortie.txt` : Redirige la sortie standard de `echo` vers le fichier `sortie.txt`.
- `2> erreur.txt` : Redirige les erreurs (stderr) vers le fichier `erreur.txt`.
- `&> tout.txt` : Redirige à la fois la sortie standard et les erreurs vers le fichier `tout.txt`.

---

## Exemple avancé de `trap` pour nettoyer après interruption

Le `trap` est utilisé pour intercepter des signaux comme `SIGINT` (Ctrl+C) ou `SIGTERM` (arrêt du processus) et exécuter une commande de nettoyage avant la sortie du script.

Exemple :
```bash
#!/bin/bash
trap "echo 'Nettoyage'; rm -f /tmp/tempfile; exit" SIGINT SIGTERM

# Créer un fichier temporaire
echo "Fichier temporaire" > /tmp/tempfile
echo "Appuyez sur Ctrl+C pour tester le nettoyage"

# Attendre l'interruption du signal
sleep 60
```

- Le script crée un fichier temporaire `/tmp/tempfile` et attend 60 secondes. Si tu appuies sur `Ctrl+C`, le signal `SIGINT` est intercepté, et la commande `rm -f /tmp/tempfile` est exécutée avant que le script ne se termine.

---

## Utilisation de `find` pour rechercher des fichiers dans un script

`find` est une commande puissante qui permet de rechercher des fichiers dans un répertoire selon des critères précis. C'est particulièrement utile dans des scripts où tu veux trouver des fichiers spécifiques ou effectuer des opérations sur ceux-ci.

Exemple :
```bash
#!/bin/bash

# Rechercher tous les fichiers .txt dans le répertoire courant et afficher leur contenu
find . -type f -name "*.txt" -exec cat {} \;
```

- `find . -type f -name "*.txt"` : Recherche tous les fichiers `.txt` dans le répertoire courant.
- `-exec cat {} \;` : Pour chaque fichier trouvé, exécute la commande `cat` pour afficher son contenu.

---

## Utilisation de `xargs` pour manipuler les résultats des commandes

`xargs` permet de traiter les résultats d'une commande en les passant comme arguments à une autre commande. Cela est très utile lorsqu'une commande génère une liste de résultats, que tu veux utiliser dans une autre commande.

Exemple :
```bash
#!/bin/bash

# Rechercher tous les fichiers .txt et compter les lignes
find . -type f -name "*.txt" | xargs wc -l
```

- `find . -type f -name "*.txt"` : Recherche tous les fichiers `.txt`.
- `| xargs wc -l` : Passe la liste des fichiers trouvés à `xargs`, qui les passe ensuite à la commande `wc -l` pour compter le nombre de lignes dans chaque fichier.

---

## Mots-clés Bash courants

Voici une liste des mots-clés et commandes spécifiques utilisés dans ce cours, avec une courte explication pour chacun.

| Mot-clé        | Description                                                                 |
|----------------|------------------------------------------------------------------------------|
| `#!/bin/bash`  | Shebang : indique quel interpréteur utiliser pour exécuter le script.       |
| `echo`         | Affiche du texte à l'écran.                                                  |
| `read`         | Attend une saisie utilisateur et la stocke dans une variable.               |
| `if / elif / else / fi` | Permet de créer des conditions (branches logiques).              |
| `then`         | Introduit le bloc de code exécuté si la condition est vraie.                |
| `[ ]`          | Enveloppe une condition (attention aux espaces !).                          |
| `-eq`, `-ne`, `-lt`, `-le`, `-gt`, `-ge` | Opérateurs de comparaison numérique.           |
| `=` ou `!=`    | Comparaison de chaînes de caractères.                                       |
| `||` / `&&`    | OU / ET logiques pour combiner plusieurs conditions.                        |
| `case` / `esac`| Alternative au `if` pour gérer plusieurs cas.                               |
| `select` / `in` / `do` / `done` | Menu interactif pour proposer plusieurs choix.           |
| `while` / `until` | Boucles basées sur une condition (true ou false).                       |
| `for` / `in` / `do` / `done` | Boucle sur une séquence ou une liste.                       |
| `break`        | Interrompt immédiatement la boucle en cours.                                |
| `continue`     | Passe à l’itération suivante de la boucle, sans finir le bloc courant.      |
| `function`     | Permet de déclarer une fonction dans le script.                             |
| `$0`, `$1`, `$2`, ..., `$*`, `$#` | Variables spéciales pour les paramètres du script.     |
| `expr`         | Permet de faire des calculs arithmétiques simples.                          |
| `chmod`        | Change les droits d’accès à un fichier (lecture, écriture, exécution).     |
| `./fichier.sh` | Lance un script exécutable dans le répertoire courant.                      |

---

## Expressions régulières / `grep` / `sed` / `awk`
```bash
# grep pour filtrer
cat fichier.txt | grep "mot"

# sed pour remplacer dans un fichier
sed 's/ancien/nouveau/' fichier.txt

# awk pour extraire une colonne
awk '{print $2}' fichier.txt
```

### `grep` : recherche d’un motif dans un fichier.
```bash
cat fichier.txt | grep "mot"
```

### `sed` : modifier un texte en flux ou fichier.
```bash
sed 's/ancien/nouveau/' fichier.txt
```

### `awk` : traitement avancé de colonnes et de champs.
```bash
awk '{print $2}' fichier.txt
```

> Ces outils sont puissants pour automatiser la manipulation de fichiers texte.



---

Tu peux consulter le manuel de n’importe quelle commande avec :

```bash
man <commande>
```

Exemple :
```bash
man chmod
```
