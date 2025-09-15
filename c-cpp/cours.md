# C / C++

## Extension des fichiers et lancement
- Les fichiers **C** se terminent par `.c`.
- Les fichiers **C++** se terminent par `.cpp`.

### Compilation et exécution (Linux / WSL / macOS)
```bash
gcc MonProgramme.c -o MonProgramme   # compilation C
./MonProgramme

g++ MonProgramme.cpp -o MonProgramme # compilation C++
./MonProgramme
```

### Exemple minimal C
```c
#include <stdio.h>

int main() {
    printf("Bonjour C !\n");
    return 0;
}
```
- `#include <stdio.h>` : inclut la bibliothèque standard.
- `int main()` : point d’entrée du programme.
- `printf` : affiche du texte.

### Exemple minimal C++
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Bonjour C++ !" << endl;
    return 0;
}
```

### Activer les warnings : utile pour détecter des erreurs ou mauvaises pratiques.
```bash
gcc -Wall MonProgramme.c -o MonProgramme   # C
g++ -Wall MonProgramme.cpp -o MonProgramme # C++
```
> ⚠️ `-Wall` active la plupart des avertissements du compilateur. Corriger ces warnings rend le code plus sûr.

---

## Les bases
- C est un langage **compilé** : le code source est traduit en code machine par un compilateur.
- C++ est une extension de C, ajoutant la **programmation orientée objet**.
- Le point d’entrée d’un programme est toujours la fonction `main`.
- Chaque instruction se termine par un point-virgule `;`.
- Les blocs de code sont délimités par des accolades `{ ... }`.
- La casse est importante (`maVariable` ≠ `mavariable`).

---

## Déclaration des variables
Types de base en C :
- `int` : entier (`5`)
- `float` : nombre à virgule flottante (`3.14`)
- `double` : nombre flottant plus précis
- `char` : caractère (`'A'`)
- `char[]` : chaîne de caractères (`"Bonjour"` en C)
- En C++ : on peut utiliser `string` (avec `#include <string>`).

Exemple :
```c
int age = 21;
float taille = 1.73;
char initiale = 'J';
char nom[] = "Alexer";
```

---

## Constantes et macros
En C, on peut définir des constantes de deux manières :
### Avec `#define`
```c
#define PI 3.14159
printf("PI = %f\n", PI);
```
Ici, `PI` sera remplacé par `3.14159` au moment de la **compilation**.

### Avec `const`
```c
const int TAILLE = 10;
```
Contrairement à `#define`, `const` respecte le typage et est plus sûr.
👉 En C++, on privilégie `const`.

---

## Entrées / sorties
### Affichage avec `printf`
`printf` utilise des **spécificateurs de format** :
- `%d` → entier
- `%f` → nombre flottant
- `%c` → caractère
- `%s` → chaîne de caractère

Exemple :
```c
int age = 21;
char nom[] = "Alexer";

printf("Nom : %s, Âge : %d\n", nom, age);
```

### Lecture avec `scanf`
```c
int age;
scanf("%d", &age); // & = adresse de la variable
```
> ⚠️ En C, il faut toujours donner l’adresse (`&`) de la variable pour que `scanf` écrive dedans.

---

## Chaînes de caractères en C
En C, une chaîne est un **tableau de `char` terminé par `\0`**.
```c
char mot[] = "Bonjour";
printf("%s\n", mot);
```
Pour manipuler des chaînes, on utilise `<string.h>` :
```c
#include <string.h>

char a[] = "Hello";
char b[] = "World";

printf("Longueur : %lu\n", strlen(a));   // 5
strcpy(b, a);                            // copie a dans b
printf("b = %s\n", b);                   // Hello
```
👉 En C++, on utilise plutôt `string` qui est beaucoup plus pratique.

---

## Opérations numériques
| Opération      | Symbole | Exemple  | Résultat |
| -------------- | ------- | -------- | -------- |
| Addition       | +       | `5 + 3`  | 8        |
| Soustraction   | -       | `5 - 3`  | 2        |
| Multiplication | \*      | `5 * 3`  | 15       |
| Division       | /       | `10 / 2` | 5        |
| Modulo         | %       | `10 % 3` | 1        |

---

## Opérateurs avancés
| Opérateur                        | Type                  | Exemple        | Résultat    |            |           |
| -------------------------------- | --------------------- | -------------- | ----------- | ---------- | --------- |
| `++` / `--`                      | incrément / décrément | `i++` ou `--i` | `i` +1 / -1 |            |           |
| `+=`, `-=`, `*=`, `/=`           | affectation combinée  | `x += 5`       | `x = x + 5` |            |           |
| `==`, `!=`, `<`, `>`, `<=`, `>=` | comparaison           | `a == b`       | vrai/faux   |            |           |
| `&&`, \`                         |                       | `, `!\`        | logique     | `(a && b)` | vrai/faux |

> Très utile pour les conditions complexes et les boucles.

---

## Conditions
### If simple
```c
if (age >= 18) {
    printf("Majeur\n");
}
```

### If / Else
```c
if (age >= 18) {
    printf("Majeur\n");
} else {
    printf("Mineur\n");
}
```

### If / Else If / Else
```c
if (note >= 16) {
    printf("Très bien\n");
} else if (note >= 10) {
    printf("Suffisant\n");
} else {
    printf("Échec\n");
}
```

---

## Boucles
Les boucles permettent de répéter du code plusieurs fois.
### Boucle `for`
Utilisée quand on connaît le nombre d’itérations.
```c
for (int i = 0; i < 5; i++) {
    printf("i = %d\n", i);
}
```

### Boucle `while`
Utilisée quand on répète tant qu’une condition est vraie.
```c
int i = 0;
while (i < 5) {
    printf("i = %d\n", i);
    i++;
}
```

### Boucle `do...while`
Comme `while`, mais s’exécute au moins une fois.
```c
int i = 0;
do {
    printf("i = %d\n", i);
    i++;
} while (i < 5);
```

### Quand utiliser quelle boucle ?
| Boucle       | Quand l’utiliser                                                                                            |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| `for`        | Quand on sait combien de fois on doit répéter (par ex. parcourir un tableau de 10 cases).                   |
| `while`      | Quand on répète tant qu’une condition reste vraie (par ex. lire tant que l’utilisateur ne tape pas "exit"). |
| `do...while` | Quand on veut exécuter **au moins une fois** avant de tester la condition (par ex. afficher un menu).       |

---

## Fonctions
Une fonction permet de **réutiliser du code**.
```c
#include <stdio.h>

int addition(int a, int b) {
    return a + b;
}

int main() {
    printf("Résultat = %d\n", addition(5, 3));
    return 0;
}
```

---

## Fonctions avancées
### Passage par valeur (par défaut en C)
```c
void test(int x) {
    x = 100;
}
```
Ici, `x` est une copie → la variable originale ne change pas.

### Passage par adresse (avec pointeurs)
```c
void test(int *x) {
    *x = 100;
}

int main() {
    int a = 5;
    test(&a);
    printf("%d\n", a); // 100
}
```
👉 Le passage par adresse permet de modifier la variable d’origine.

### Valeurs par défaut en C++ :
```cpp
#include <iostream>
using namespace std;

void direBonjour(string nom = "inconnu") {
    cout << "Bonjour " << nom << endl;
}

int main() {
    direBonjour();       // Bonjour inconnu
    direBonjour("Alexer"); // Bonjour Alexer
}
```
> Permet d’appeler une fonction avec ou sans certains paramètres.

### Fonctions inline : petites fonctions pour éviter le coût d’appel.
```cpp
inline int carre(int x) {
    return x*x;
}
```

---

## Tableaux
Un tableau est une suite de cases mémoire consécutives du même type.
> ⚠️ En C, les indices commencent toujours à **0**.
Exemple :
```c
int notes[5] = {12, 15, 9, 18, 14};
printf("Première note : %d\n", notes[0]); // 12
printf("Dernière note : %d\n", notes[4]); // 14
```

On peut parcourir un tableau avec une boucle :
```c
for (int i = 0; i < 5; i++) {
    printf("Note %d = %d\n", i, notes[i]);
}
```

---

## Tableaux et pointeurs
```c
int tab[5] = {1,2,3,4,5};
int *p = tab;   // p pointe sur le premier élément
printf("%d\n", *(p+2)); // 3
```
> En C, le nom d’un tableau est déjà un pointeur vers le premier élément.

---

## Tableaux multidimensionnels
Un tableau à 2 dimensions ressemble à un tableau de tableaux.
```c
int matrice[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};

printf("%d\n", matrice[1][2]); // 6
```
On peut les parcourir avec deux boucles imbriquées :
```c
for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
        printf("%d ", matrice[i][j]);
    }
    printf("\n");
}
```

---

## Pointeurs
Un pointeur est une variable qui contient l’adresse d’une autre variable.
### Exemple simple
```c
int x = 10;
int *p = &x;   // p contient l’adresse de x

printf("Valeur de x = %d\n", x);
printf("Adresse de x = %p\n", p);
printf("Valeur via pointeur = %d\n", *p); // *p = valeur pointée
```
- `&x` = adresse de la variable `x`.
- `*p` = valeur stockée à l’adresse contenue dans `p`.

### Utilisation pratique
```c
void incrementer(int *n) {
    (*n)++;
}

int main() {
    int valeur = 5;
    incrementer(&valeur);
    printf("Nouvelle valeur = %d\n", valeur); // 6
}
```
👉 Les pointeurs sont très utilisés pour manipuler des tableaux, des chaînes et l’allocation mémoire.

---

## Structures
Une structure permet de regrouper plusieurs informations de types différents dans un même objet.
```c
struct Personne {
    char nom[50];
    int age;
};

int main() {
    struct Personne p1 = {"Alexer", 22};
    printf("%s a %d ans\n", p1.nom, p1.age);
    return 0;
}
```
Ici, `struct Personne` contient à la fois une chaîne (`nom`) et un entier (`age`).

---

## Structures avancées
### Structures imbriquées
```c
struct Adresse {
    char ville[50];
    int codePostal;
};

struct Personne {
    char nom[50];
    int age;
    struct Adresse adresse;
};

int main() {
    struct Personne p = {"Alexer", 21, {"Paris", 75000}};
    printf("%s habite à %s (%d)\n", p.nom, p.adresse.ville, p.adresse.codePostal);
}
```

### Tableaux de structures
```c
struct Etudiant {
    char nom[50];
    int note;
};

int main() {
    struct Etudiant classe[2] = {
        {"Bob", 17},
        {"Alexer", 18}
    };

    for (int i = 0; i < 2; i++) {
        printf("%s a eu %d/20\n", classe[i].nom, classe[i].note);
    }
}
```

---

## Énumérations (enum)
Une énumération permet de définir un ensemble de valeurs possibles.
```c
enum Jour {Lundi, Mardi, Mercredi, Jeudi, Vendredi};

int main() {
    enum Jour aujourdHui = Mardi;
    if (aujourdHui == Mardi) {
        printf("C'est mardi !\n");
    }
}
```
👉 Par défaut, chaque élément vaut un entier (`Lundi=0`, `Mardi=1`, etc.).

---

## Lire et écrire dans des fichiers
### Écriture
```c
#include <stdio.h>

int main() {
    FILE *f = fopen("notes.txt", "w");
    fprintf(f, "Alexer 15\nBob 12\n");
    fclose(f);
}
```

### Lecture
```c
#include <stdio.h>

int main() {
    FILE *f = fopen("notes.txt", "r");
    char nom[50];
    int note;

    while (fscanf(f, "%s %d", nom, &note) != EOF) {
        printf("%s a %d/20\n", nom, note);
    }

    fclose(f);
}
```
👉 `fopen` peut ouvrir un fichier en mode **lecture** (`"r"`), **écriture** (`"w"`), ou **ajout** (`"a"`).

---

## Passage au C++
En C++, on garde la syntaxe de base, mais on peut aussi utiliser :
- `cin` et `cout` pour les entrées/sorties.
- La classe `string` pour manipuler les chaînes de caractères.
- La programmation orientée objet.

### Exemple (C++)
```cpp
#include <iostream>
using namespace std;

int main() {
    string nom;
    int age;

    cout << "Entrez votre nom : ";
    cin >> nom;

    cout << "Entrez votre âge : ";
    cin >> age;

    cout << "Bonjour " << nom << ", vous avez " << age << " ans." << endl;
    return 0;
}
```
#### À quoi sert `using namespace std;` ?
- En C++, les fonctions comme `cout` et `cin` appartiennent à l’espace de noms `std`.
- Sans `using namespace std;`, il faudrait écrire :
```cpp
std::cout << "Bonjour !" << std::endl;
```
- Avec `using namespace std;`, on peut simplement écrire :
```cpp
cout << "Bonjour !" << endl;
```
> ⚠️ Dans les grands projets, certains préfèrent éviter `using namespace std;` pour éviter les conflits de noms. Mais pour débuter, c’est pratique.

---

## Chaînes en C++
### Concaténation :
```cpp
string a = "Bonjour";
string b = "Alexer";
string c = a + " " + b;
cout << c << endl; // Bonjour Alexer
```

### Longueur :
```cpp
cout << "Longueur : " << c.size() << endl;
```

### Comparaison :
```cpp
if(a == b) { cout << "Identiques"; }
```

### Boucle sur string :
```cpp
for(char ch : c) {
    cout << ch << "-";
}
```

---

## Entrées utilisateurs avancées (C++)
### Lecture de plusieurs mots :
```cpp
string nomComplet;
getline(cin, nomComplet);
cout << "Nom complet : " << nomComplet << endl;
```
> `cin` seul lit jusqu’au premier espace, `getline` lit toute la ligne.

### Vérification des entrées :
```cpp
int age;
cin >> age;
if(cin.fail()) {
    cout << "Erreur: vous devez entrer un entier." << endl;
    cin.clear();
    cin.ignore(1000, '\n');
}
```

---

## Aller plus loin en C++
### Références
En C++, une référence est un alias d’une variable.  
C’est comme un surnom donné à une variable existante : toute modification via la référence modifie aussi la variable originale.

Exemple :
```cpp
#include <iostream>
using namespace std;

void doubler(int &x) {
    x = x * 2;
}

int main() {
    int a = 5;
    doubler(a); 
    cout << "a = " << a << endl; // a = 10
}
```
📌 Différence avec pointeurs :
- Un **pointeur** contient une adresse (`*p` = valeur pointée).
- Une **référence** est une autre façon de désigner la même variable → pas besoin de `*` ni de `&` à chaque fois.

👉 Pour débuter : utilise les références, elles sont **plus simples** et **plus sûres** que les pointeurs.

### Vecteurs
Un tableau classique en C/C++ a une taille fixe.
Un `vector` (fourni par la bibliothèque standard en C++) est comme un tableau dynamique qui peut grandir ou rétrécir tout seul.
```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> notes;

    notes.push_back(12); // ajoute 12
    notes.push_back(15); // ajoute 15
    notes.push_back(18); // ajoute 18

    cout << "Première note : " << notes[0] << endl; // 12

    // Parcourir le vector
    for (int i = 0; i < notes.size(); i++) {
        cout << "Note " << i << " = " << notes[i] << endl;
    }
}
```
👉 Avantages de `vector` :
- Pas besoin de connaître la taille à l’avance.
- Plus sûr et plus pratique que les tableaux classiques.
- Fournit des fonctions utiles (`size()`, `push_back()`, etc.).

### Classes simples
En C++, on peut regrouper données + fonctions dans une classe.  
Une classe, c’est comme un plan pour créer des objets.
```cpp
#include <iostream>
using namespace std;

class Personne {
public:          // accessible partout
    string nom;
    int age;

    void afficher() {
        cout << nom << " a " << age << " ans" << endl;
    }
};

int main() {
    Personne p;      // on crée un objet "p" de type Personne
    p.nom = "Alexer";
    p.age = 21;
    p.afficher();    // affiche "Alexer a 21 ans"

    return 0;
}
```

📌 Vocabulaire :
- `class` = plan / modèle
- `objet` = instance de la classe (ici `p`)
- `attributs` = variables internes (ici `nom`, `age`)
- `méthodes` = fonctions internes (ici `afficher()`)

👉 Les classes sont la base de la **programmation orientée objet (POO)**.
Elles permettent de mieux organiser le code, surtout dans des projets complexes.

---

## Introduction à la POO (C++)
### Constructeur :
```cpp
class Personne {
public:
    string nom;
    int age;

    Personne(string n, int a) { nom = n; age = a; }

    void afficher() { cout << nom << " a " << age << " ans\n"; }
};

int main() {
    Personne p("Alexer", 21);
    p.afficher();
}
```

### Encapsulation :
```cpp
class Personne {
private:
    int age;
public:
    void setAge(int a) { if(a>0) age=a; }
    int getAge() { return age; }
};
```
> Les attributs privés ne peuvent être modifiés directement, ce qui sécurise les données.

### Constructeur par défaut et surcharge :
```cpp
Personne() { nom="inconnu"; age=0; }
```

### Héritage :
```cpp
class Etudiant : public Personne {
public:
    int note;
};
```
