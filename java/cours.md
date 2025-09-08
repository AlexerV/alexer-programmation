# Java

## Extension des fichiers Java et comment lancer un programme
- Extension des fichiers Java : `.java`

Chaque fichier source Java se termine par `.java`.

- Compilation et exécution :

Sur Windows / Linux / macOS, si tu as installé le JDK (Java Development Kit), tu peux compiler et lancer un programme via le terminal (ou invite de commande) :
```bash
javac MonProgramme.java  # compile le fichier source, crée MonProgramme.class
java MonProgramme        # exécute le programme compilé
```

- Exemple simple :
```java
// MonProgramme.java
public class MonProgramme {
    public static void main(String[] args) {
        System.out.println("Bonjour Java !");
    }
}
```

Puis lancer :
```bash
javac MonProgramme.java
java MonProgramme
```

--- 

## Les bases
- Java est un langage **compilé** et **orienté objet**.
- Le point d’entrée d’un programme est toujours la méthode `main` :
```java
public static void main(String[] args) {
    // code ici
}
```
- Chaque instruction se termine par un point-virgule `;`.
- Les blocs de code sont délimités par des accolades `{ ... }`.
- La casse est importante (`maVariable` ≠ `mavariable`).

---

## Déclaration des variables
- Types de base (primitifs) en Java :
  - `int` : entier (ex : `5`)
  - `double` : nombre décimal (ex : `3.14`)
  - `boolean` : vrai/faux (`true` / `false`)
  - `char` : caractère (ex : `'A'`)
  - `String` : chaîne de caractères (ex : `"Hello"`)

- Exemple :
```java
int age = 21;
double taille = 1.73;
boolean estConnecte = true;
char initiale = 'J';
String nom = "Alexer";
```

---

## Opérations numériques
Java supporte les opérations classiques :
| Opération      | Symbole | Exemple  | Résultat |
| -------------- | ------- | -------- | -------- |
| Addition       | +       | `5 + 3`  | 8        |
| Soustraction   | -       | `5 - 3`  | 2        |
| Multiplication | \*      | `5 * 3`  | 15       |
| Division       | /       | `10 / 2` | 5        |
| Modulo         | %       | `10 % 3` | 1        |

Exemple :
```java
int a = 10;
int b = 3;
int reste = a % b;  // reste = 1
```

---

## Saisir des informations
Pour lire des entrées utilisateur, on utilise la classe `Scanner` :
```java
import java.util.Scanner;

public class ExempleLecture {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Entrez votre nom : ");
        String nom = sc.nextLine();

        System.out.print("Entrez votre âge : ");
        int age = sc.nextInt();

        System.out.println("Bonjour " + nom + ", vous avez " + age + " ans.");

        sc.close();
    }
}
```

---

## Opérateurs de comparaison
| Opérateur | Signification       | Exemple  |
| --------- | ------------------- | -------- |
| `==`      | égal à              | `a == b` |
| `!=`      | différent de        | `a != b` |
| `<`       | inférieur à         | `a < b`  |
| `>`       | supérieur à         | `a > b`  |
| `<=`      | inférieur ou égal à | `a <= b` |
| `>=`      | supérieur ou égal à | `a >= b` |

Exemple :
```java
if (a == b) {
    System.out.println("a est égal à b");
}
```

--- 

## Structure conditionnelles
Structure de base :
```java
if (condition) {
    // bloc exécuté si vrai
} else if (autreCondition) {
    // autre bloc
} else {
    // bloc sinon
}
```

Exemple :
```java
int note = 15;
if (note >= 10) {
    System.out.println("Admis");
} else {
    System.out.println("Échoué");
}
```

---

## Opérateurs logiques
- `&&` : ET logique (`a > 0 && b < 10`)
- `||` : OU logique (`a < 0 || b > 10`)
- `!` : NON logique (`!(a == b)`)

Exemple :
```java
if (age >= 18 && estConnecte) {
    System.out.println("Accès autorisé");
}
```

---

## Boucles
### Boucle `for`
```java
for (int i = 0; i < 5; i++) {
    System.out.println("i = " + i);
}
```

### Boucle `while`
```java
int i = 0;
while (i < 5) {
    System.out.println("i = " + i);
    i++;
}
```

### Boucle `do...while`
```java
int i = 0;
do {
    System.out.println("i = " + i);
    i++;
} while (i < 5);
```

### Quand utiliser quelle boucle en Java
| Type de boucle | Quand l’utiliser                                                                                                        | Exemple de situation                          |
| -------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| `for`          | Quand **le nombre d’itérations est connu à l’avance**                                                                   | Afficher les nombres de 1 à 10                |
| `while`        | Quand **on ne connaît pas à l’avance le nombre d’itérations**, mais on veut **répéter tant qu’une condition est vraie** | Lire un mot de passe tant qu’il est incorrect |
| `do...while`   | Quand on veut **exécuter au moins une fois**, puis **répéter tant qu’une condition est vraie**                          | Afficher un menu interactif au moins une fois |


---

## Fonctions (méthodes)
Déclaration d’une méthode simple :
```java
public static int addition(int a, int b) {
    return a + b;
}
```
Utilisation :
```java
int resultat = addition(5, 3);  // resultat = 8
System.out.println(resultat);
```

---

## Structures de base de données
### Listes (ArrayList) :
```java
import java.util.ArrayList;

ArrayList<String> fruits = new ArrayList<>();
fruits.add("Pomme");
fruits.add("Banane");
System.out.println(fruits.get(0));  // Pomme
```

### Dictionnaires (HashMap) :
```java
import java.util.HashMap;

HashMap<String, Integer> ages = new HashMap<>();
ages.put("Alice", 25);
ages.put("Bob", 30);
System.out.println(ages.get("Alice"));  // 25
```

---

## Switch case
```java
int jour = 3;
switch (jour) {
    case 1:
        System.out.println("Lundi");
        break;
    case 2:
        System.out.println("Mardi");
        break;
    case 3:
        System.out.println("Mercredi");
        break;
    default:
        System.out.println("Jour inconnu");
}
```
