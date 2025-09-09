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

Exemple :
```c
int age = 21;
float taille = 1.73;
char initiale = 'J';
char nom[] = "Alexer";
```

---

## Entrées / sorties
### Affichage (C)
```c
#include <stdio.h>
printf("Bonjour %s, tu as %d ans.\n", nom, age);
```

### Lecture clavier (C)
```c
#include <stdio.h>

int main() {
    int age;
    printf("Entrez votre âge : ");
    scanf("%d", &age);
    printf("Vous avez %d ans.\n", age);
    return 0;
}
```

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

## Conditions
```c
if (age >= 18) {
    printf("Majeur\n");
} else {
    printf("Mineur\n");
}
```

---

## Boucles
### Boucle `for`
```c
for (int i = 0; i < 5; i++) {
    printf("i = %d\n", i);
}
```

### Boucle `while`
```c
int i = 0;
while (i < 5) {
    printf("i = %d\n", i);
    i++;
}
```

### Boucle `do...while`
```c
int i = 0;
do {
    printf("i = %d\n", i);
    i++;
} while (i < 5);
```

---

## Fonctions
```c
#include <stdio.h>

int addition(int a, int b) {
    return a + b;
}

int main() {
    int resultat = addition(5, 3);
    printf("Résultat = %d\n", resultat);
    return 0;
}
```

---

## Tableaux
Un tableau permet de stocker plusieurs valeurs du même type :
```c
int notes[5] = {12, 15, 9, 18, 14};
for (int i = 0; i < 5; i++) {
    printf("Note %d = %d\n", i, notes[i]);
}
```

---

## Structures
Une structure regroupe plusieurs variables sous un même nom :
```c
struct Personne {
    char nom[50];
    int age;
};

int main() {
    struct Personne p1 = {"Alice", 22};
    printf("%s a %d ans\n", p1.nom, p1.age);
    return 0;
}
```

---

## Passage au C++
En C++, on garde la syntaxe de base, mais on peut aussi utiliser :
- `cin` et `cout` pour les entrées/sorties.
- Les classes pour l’orienté objet.

### Exemple (C++)
```cpp
#include <iostream>
using namespace std;

int main() {
    int age;
    cout << "Quel est ton âge ? ";
    cin >> age;

    if (age >= 18) {
        cout << "Majeur" << endl;
    } else {
        cout << "Mineur" << endl;
    }
    return 0;
}
```
