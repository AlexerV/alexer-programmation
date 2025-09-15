# Python

## Les bases de Python

```python
print("Hello World")    # permet d'afficher la chaîne de caractères "Hello World"
# ceci est un commentaire
```
- L’extension d’un fichier Python est `.py` (exemple : `monFichier.py`)
- Pour exécuter un fichier Python, dans le terminal Windows :
```bash
python monFIchier.py
```
- Pour exécuter un fichier Python, dans le terminal Linux :
```bash
python3 monFichier.py
```

---

## Déclaration d’une variable
```bash
nomVariable = valeur
```

Exemples :
```python
prenom = "Alexer"
age = 21
endroit = "Quelque part dans ce monde"
```

---

## Opérations arithmétiques
| Symbole | Description                                   |
| ------- | --------------------------------------------- |
| `+`     | addition                                      |
| `-`     | soustraction                                  |
| `*`     | multiplication                                |
| `/`     | division flottante (résultat en float)        |
| `%`     | modulo (reste de la division)                 |
| `**`    | puissance (exposant)                          |
| `//`    | division entière (partie entière du quotient) |

Exemples :
```python
nombre1 = 100
nombre2 = 50

print(nombre1 + nombre2)  # affiche 150
```

---

## Saisir des informations
La fonction `input()` permet de récupérer une entrée utilisateur :
```python
mot = input()
print(mot)
```

On peut aussi afficher un message avant la saisie :
```python
mot = input("Entrez un pays : ")
print(mot)
```

Attention : la valeur retournée par `input()` est toujours une chaîne (`str`). Pour convertir en un type numérique, utiliser `int()` ou `float()` :
```python
nombreEntier = int(input("Entrez un nombre entier : "))
print(nombreEntier)
```

```python
nombreFlottant = float(input("Entrez un nombre flottant : "))
print(nombreFlottant)
```

Fusion avec opérations :
```python
nombre = int(input("Entrez un nombre positif quelconque : "))
print("Le carré de", nombre, "vaut", nombre**2)
```

---

## Opérateurs de comparaison
Utilisés souvent dans les structures conditionnelles :
| Opérateur | Description                | Exemple  |
| --------- | -------------------------- | -------- |
| `==`      | égalité (valeur et type)   | `x == y` |
| `!=`      | différent (valeur ou type) | `x != y` |
| `<`       | strictement inférieur      | `x < y`  |
| `>`       | strictement supérieur      | `x > y`  |
| `<=`      | inférieur ou égal          | `x <= y` |
| `>=`      | supérieur ou égal          | `x >= y` |

---

## Structures conditionnelles
### if simple
```python
if condition:
    instruction
```

Exemple où la condition est vraie :
```python
x = 15
if x > 10:
    print(x, "est plus grand que 10")
print("Fin")
```

Exemple où la condition est fausse :
```python
x = 3
if x > 10:
    print(x, "est plus grand que 10")
print("Fin")
```

### if...else
```python
if condition:
    instruction_1
else:
    instruction_2
```

Exemple où la condition est vraie :
```python
x = 5
if x > 0:
    print(x, "est positif")
else:
    print(x, "est négatif ou nul")
print("Fin")
```

Exemple où la condition est fausse :
```python
x = -2
if x > 0:
    print(x, "est positif")
else:
    print(x, "est négatif ou nul")
print("Fin")
```

### if...elif...else
```python
if condition_1:
    instruction_1
elif condition_2:
    instruction_2
else:
    instruction_3
```

Exemple :
```python
x = 5
if x > 0:
    print(x, "est positif")
elif x < 0:
    print(x, "est négatif")
else:
    print(x, "est nul")
print("Fin")
```
Tu peux mettre autant d’`elif` que tu veux.

---

## Opérateurs logiques
| Opérateur | Description                               | Exemple           |
| --------- | ----------------------------------------- | ----------------- |
| `and`     | et logique (les deux conditions vraies)   | `2 < 3 and 3 < 4` |
| `or`      | ou logique (au moins une condition vraie) | `2 < 3 or 3 > 4`  |
| `not`     | négation                                  | `not (2 < 3)`     |

---

## Boucles

### Boucle for

```python
for i in [0, 1, 2, 3]:
    print("i a pour valeur", i)
```

On peut utiliser la fonction `range()` pour générer la séquence :
```pyhton
for i in range(4):
    print("i a pour valeur", i)
```

Pour parcourir les indices d’une liste :
```python
a = ["Alexer", "est", "un", "bon", "développeur"]
for i in range(len(a)):
    print("i vaut", i, "et a[i] vaut", a[i])
```

Ou directement les éléments :
```python
a = ["Alexer", "est", "un", "bon", "développeur"]
for mot in a:
    print("mot vaut", mot)
```

### Boucle while

```python
while condition:
    instruction
```

Exemple :
```python
x = 1
while x < 10:
    print("x a pour valeur", x)
    x = x + 1
print("Fin")
```
Remarques :

- Si la condition est fausse au départ, le corps de la boucle n’est jamais exécuté.

- Si la condition reste vraie indéfiniment, boucle infinie.

### Que choisir entre boucle for et while ?

- Utilise `for` quand tu connais le nombre d’itérations à l’avance.

- Utilise `while` quand la condition d’arrêt dépend d’un test dynamique.

---

## Fonctions

Déclaration :
```python
def nom_fonction(param1, param2):
    # bloc d'instructions
```

Exemple simple :
```python
def compteur():
    i = 0
    while i < 3:
        print(i)
        i = i + 1

print("bonjour")
compteur()
```

Fonction appelant une autre fonction :
```python
def compteur():
    i = 0
    while i < 3:
        print(i)
        i = i + 1

def double_compteur():
    compteur()
    compteur()

print("bonjour")
double_compteur()
```

Fonction avec paramètres :
```python
def compteur(stop):
    i = 0
    while i < stop:
        print(i)
        i = i + 1

compteur(4)
compteur(2)
```

---

## Structures de données de base

### Les listes
```python
fruits = ["pomme", "banane", "cerise"]
print(fruits[0])  # affiche "pomme"
```

Les dictionnaires
```python
personne = {"nom": "Alexer", "age": 21}
print(personne["nom"])  # affiche "Alexer"
```

---

## Match / Case (Python 3.10+)
La structure `match` permet de faire des tests conditionnels multiples similaires au `switch` d’autres langages.

```python
match variable:
    case valeur_1:
        # action 1
    case valeur_2:
        # action 2
    case _:
        # cas par défaut
```

Exemple :
```python
lang = input("Quel est le langage de programmation que vous souhaitez apprendre ? ")

match lang:
    case "JavaScript":
        print("Vous pouvez devenir un développeur WEB.")
    case "Python":
        print("Vous pouvez devenir Data Scientist.")
    case "PHP":
        print("Vous pouvez devenir développeur backend.")
    case "Solidity":
        print("Vous pouvez devenir développeur Blockchain.")
    case "Java":
        print("Vous pouvez devenir développeur d’applications mobiles.")
    case _:
        print("La langue n'a pas d'importance, ce qui compte c'est de résoudre les problèmes.")
```

*Note : `match` est disponible à partir de **Python 3.10**.*

---

à ajouter :
- Types de données avancés
  - Tuple : liste immuable
  - Set (ensemble) : collection non ordonnée, sans doublons
  - Booléens : True / False
- Listes et dictionnaires avancés
  - Compréhension de liste
  - Dictionnaire avec compréhension
  - Méthodes utiles pour les listes
- Fonctions avancées
  - Paramètres par défaut
  - Paramètres variables
  - Retour multiple
  - Fonctions lambda (anonymes)
- Modules et packages
  - Importer des modules intégrés
  - Importer une fonction spécifique
  - Installer et utiliser des packages avec pip
- Fichiers
  - Lecture et écriture
  - Lecture ligne par ligne
- Gestion des erreurs
  - Try / Except
  - Else et finally
- Programmation orientée objet
  - Héritage
  - Encapsulation (private/protected)
- Bibliothèques utiles
  - Mathématiques : math, random
  - Manipulation de dates : datetime
  - Gestion des fichiers JSON : json
  - Requêtes HTTP : requests
  - Web scraping : BeautifulSoup, selenium
  - Data Science : numpy, pandas, matplotlib
