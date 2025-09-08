# Cours Bash / Shell

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

## Opérations arithmétiques

```bash
expr 3 + 5       # Affiche 8
expr $a \* $b    # Multiplie $a et $b (ex: 3 * 2)
```
> Note : L’astérisque doit être échappé avec un backslash `\*` ou placé entre guillemets `"*"`.

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

### Passage de paramètres au script
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

---

### Fonctions

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

Tu peux consulter le manuel de n’importe quelle commande avec :

```bash
man <commande>
```

Exemple :
```bash
man chmod
```
