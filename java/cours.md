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

En Java, chaque fichier source (.java) contient généralement une ou plusieurs classes. Il existe cependant une règle importante à respecter :
> Le nom du fichier doit être exactement le même que le nom de la classe déclarée comme `public` dans le fichier.

Par exemple :
- Si la classe s'appelle `MaClasse`, alors le fichier doit s'appeler `MaClasse.java`.
- Si aucune classe dans le fichier n’est déclarée comme `public`, tu peux choisir un nom de fichier librement (mais c’est rare en pratique).
> ⚠️ En cas de non-respect de cette règle, le programme ne compilera pas et une erreur sera renvoyée.

Cela garantit une organisation claire des fichiers et facilite la maintenance des projets Java, surtout lorsqu'ils deviennent plus complexes.

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

---

## Programmation orientée objet
### Classe et Objet
La base de la programmation Java repose sur les classes et les objets. Une classe est un plan ou un modèle pour créer des objets. Un objet est une instance de cette classe.

Exemple :
```java
public class Voiture {
    String marque;
    int vitesseMax;

    // Constructeur
    public Voiture(String marque, int vitesseMax) {
        this.marque = marque;
        this.vitesseMax = vitesseMax;
    }

    // Méthode
    public void afficherInfo() {
        System.out.println("Marque: " + marque + ", Vitesse Max: " + vitesseMax + " km/h");
    }
}

public class Main {
    public static void main(String[] args) {
        Voiture maVoiture = new Voiture("Toyota", 180);
        maVoiture.afficherInfo();  // Affiche Marque: Toyota, Vitesse Max: 180 km/h
    }
}
```

### Encapsulation
L'encapsulation est une technique qui consiste à cacher les détails internes d'une classe et à permettre l'accès à ses données via des méthodes publiques (getters et setters).

Exemple :
```java
public class Personne {
    private String nom;
    private int age;

    // Getter
    public String getNom() {
        return nom;
    }

    // Setter
    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age > 0) {
            this.age = age;
        }
    }
}
```

### Héritage (extends)
L'héritage permet à une classe d'hériter des propriétés et des méthodes d'une autre classe. Cela permet de réutiliser du code.

Exemple :
```java
class Animal {
    void manger() {
        System.out.println("L'animal mange.");
    }
}

class Chien extends Animal {
    void aboyer() {
        System.out.println("Le chien aboie.");
    }
}
```

### Polymorphisme
Le polymorphisme permet de redéfinir une méthode dans une classe dérivée tout en conservant la signature de la méthode de la classe de base.

Exemple :
```java
class Animal {
    void parler() {
        System.out.println("L'animal parle");
    }
}

class Chien extends Animal {
    @Override
    void parler() {
        System.out.println("Le chien aboie");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal monAnimal = new Chien();
        monAnimal.parler();  // Affiche "Le chien aboie"
    }
}
```

---

## Exceptions et gestion d’erreurs
En Java, les exceptions permettent de gérer les erreurs qui se produisent à l'exécution, afin d’éviter que le programme ne se termine brutalement.

### Gestion des exceptions
```java
try {
    int division = 10 / 0;  // Génère une exception
} catch (ArithmeticException e) {
    System.out.println("Erreur : division par zéro");
}
```

### Créer une exception personnalisée
Tu peux également créer tes propres exceptions pour mieux gérer les erreurs spécifiques à ton application.
```java
class MonException extends Exception {
    public MonException(String message) {
        super(message);
    }
}

public class TestException {
    public static void main(String[] args) {
        try {
            throw new MonException("C'est une erreur personnalisée");
        } catch (MonException e) {
            System.out.println(e.getMessage());
        }
    }
}
```

---

## Fichiers et entrées/sorties
### Lire un fichier (Lecture de texte)
Tu peux utiliser les classes de la bibliothèque `java.io` pour lire et écrire dans des fichiers.

Exemple de lecture de fichier texte :
```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class LectureFichier {
    public static void main(String[] args) {
        try {
            File fichier = new File("monfichier.txt");
            Scanner sc = new Scanner(fichier);
            while (sc.hasNextLine()) {
                System.out.println(sc.nextLine());
            }
            sc.close();
        } catch (FileNotFoundException e) {
            System.out.println("Fichier non trouvé !");
        }
    }
}
```

### Écrire dans un fichier (Sortie de texte)
Pour écrire dans un fichier en Java, tu peux utiliser des classes comme `FileWriter` ou `BufferedWriter` pour écrire des données.
#### Exemple avec `FileWriter` :
```java
import java.io.FileWriter;
import java.io.IOException;

public class EcritureFichier {
    public static void main(String[] args) {
        try {
            // Créer un objet FileWriter pour ouvrir ou créer le fichier
            FileWriter writer = new FileWriter("monfichier.txt");
            
            // Écrire une ligne dans le fichier
            writer.write("Bonjour, ceci est un test d'écriture dans un fichier.\n");
            writer.write("Ligne 2 de texte.");
            
            // Fermer le fichier après écriture
            writer.close();
            
            System.out.println("Données écrites dans le fichier avec succès !");
        } catch (IOException e) {
            System.out.println("Erreur d'écriture dans le fichier : " + e.getMessage());
        }
    }
}
```

#### Exemple avec `BufferedWriter` :
Le `BufferedWriter` est une version optimisée pour écrire des données de manière plus efficace dans un fichier.
```java
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class EcritureFichierBuffered {
    public static void main(String[] args) {
        try {
            // Créer un BufferedWriter avec FileWriter
            BufferedWriter writer = new BufferedWriter(new FileWriter("monfichier.txt"));
            
            // Écrire plusieurs lignes dans le fichier
            writer.write("Bonjour, ceci est un test d'écriture dans un fichier avec BufferedWriter.\n");
            writer.write("Ligne 2 de texte.");
            
            // Fermer le BufferedWriter
            writer.close();
            
            System.out.println("Données écrites dans le fichier avec succès !");
        } catch (IOException e) {
            System.out.println("Erreur d'écriture dans le fichier : " + e.getMessage());
        }
    }
}
```

#### Ajouter une nouvelle ligne avec `newLine()` dans `BufferedWriter` :
```java
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class EcritureFichierAvecNouvelleLigne {
    public static void main(String[] args) {
        try {
            // Créer un BufferedWriter
            BufferedWriter writer = new BufferedWriter(new FileWriter("monfichier.txt"));
            
            // Écrire du texte dans le fichier avec un retour à la ligne
            writer.write("Ligne 1 de texte.");
            writer.newLine();  // Ajouter une nouvelle ligne
            writer.write("Ligne 2 de texte.");
            
            // Fermer le writer
            writer.close();
            
            System.out.println("Données écrites avec des retours à la ligne !");
        } catch (IOException e) {
            System.out.println("Erreur d'écriture dans le fichier : " + e.getMessage());
        }
    }
}
```

### Points importants :
- Si le fichier spécifié n'existe pas, Java le crée automatiquement. Si le fichier existe déjà, son contenu est **écrasé**.
- Pour ajouter des données sans écraser le fichier existant, tu peux utiliser un second paramètre dans `FileWriter` :
```java
FileWriter writer = new FileWriter("monfichier.txt", true);  // 'true' pour ajouter
```

---

## Java 8+ (Fonctionnalités modernes)
### Lambda Expressions
Les expressions lambda permettent de simplifier les implémentations des interfaces fonctionnelles.

Exemple de lambda avec `Runnable` :
```java
Runnable tache = () -> System.out.println("Tâche exécutée");
Thread t = new Thread(tache);
t.start();
```

### Streams pour manipuler les collections
Les Streams permettent de traiter des collections de manière déclarative et fonctionnelle. Cela permet d'effectuer des opérations comme le filtrage, la transformation, et l'agrégation des données de manière concise.

Exemple de filtrage et de transformation d'une liste :
```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class StreamExemple {
    public static void main(String[] args) {
        List<Integer> nombres = Arrays.asList(1, 2, 3, 4, 5, 6);
        List<Integer> pairs = nombres.stream()
                                     .filter(n -> n % 2 == 0)
                                     .collect(Collectors.toList());
        System.out.println(pairs);  // Affiche [2, 4, 6]
    }
}
```

---

## Threads et Concurrence
### Création d’un Thread
Tu peux créer un thread en étendant la classe `Thread` ou en implémentant l'interface `Runnable`.

Exemple de thread avec `Runnable` :
```java
class Tache implements Runnable {
    public void run() {
        System.out.println("Le thread s'exécute");
    }
}

public class Main {
    public static void main(String[] args) {
        Tache tache = new Tache();
        Thread thread = new Thread(tache);
        thread.start();  // Exécute le thread
    }
}
```

### Synchronisation de threads
Si plusieurs threads accèdent à des ressources partagées, tu dois utiliser la synchronisation pour éviter des comportements imprévus.
```java
class Compteur {
    private int compte = 0;

    public synchronized void incrementer() {
        compte++;
    }

    public int getCompte() {
        return compte;
    }
}

public class Main {
    public static void main(String[] args) {
        Compteur c = new Compteur();
        Runnable tache = () -> {
            for (int i = 0; i < 1000; i++) {
                c.incrementer();
            }
        };

        Thread t1 = new Thread(tache);
        Thread t2 = new Thread(tache);

        t1.start();
        t2.start();
    }
}
```

---

## Bibliothèques utiles
### `java.util` : Collections, dates, etc.
La bibliothèque `java.util` fournit des classes pratiques pour travailler avec des collections (listes, ensembles, cartes, etc.) et des utilitaires pour manipuler les dates, les calendriers, et les ressources.

Les collections les plus courantes sont :
- Listes (`ArrayList`, `LinkedList`) : pour stocker des éléments dans un ordre défini.
- Ensembles (`HashSet`, `TreeSet`) : pour stocker des éléments uniques.
- Cartes (`HashMap`, `TreeMap`) : pour stocker des paires clé-valeur.

#### Exemple avec une `ArrayList` :
```java
import java.util.ArrayList;

public class ExempleArrayList {
    public static void main(String[] args) {
        ArrayList<String> fruits = new ArrayList<>();
        fruits.add("Pomme");
        fruits.add("Banane");
        fruits.add("Orange");

        // Affichage de la liste
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
    }
}
```

#### Exemple avec un `HashMap` :
```java
import java.util.HashMap;

public class ExempleHashMap {
    public static void main(String[] args) {
        HashMap<String, Integer> ages = new HashMap<>();
        ages.put("Alexer", 21);
        ages.put("Bob", 30);

        System.out.println("Âge d'Alexer : " + ages.get("Alexer"));
    }
}
```

#### Manipulation des dates :
Java 8 a introduit la nouvelle API `java.time` (voir ci-dessous), mais `java.util` possède encore des classes utiles pour la manipulation des dates, comme `Date` et `Calendar`.

#### Exemple avec `Date` :
```java
import java.util.Date;

public class ExempleDate {
    public static void main(String[] args) {
        Date date = new Date();  // Date actuelle
        System.out.println("Date actuelle : " + date);
    }
}
```

### `java.time` : API moderne pour gérer les dates/temps
La bibliothèque `java.time` a été introduite avec Java 8 et remplace largement l'ancienne API `java.util.Date` et `Calendar`. Elle fournit des classes immutables pour gérer les dates, heures, et périodes de manière plus précise.

#### Exemple avec `LocalDate` et `LocalTime` :
```java
import java.time.LocalDate;
import java.time.LocalTime;

public class ExempleDateHeure {
    public static void main(String[] args) {
        LocalDate date = LocalDate.now();  // Date actuelle
        LocalTime heure = LocalTime.now();  // Heure actuelle
        
        System.out.println("Date actuelle : " + date);
        System.out.println("Heure actuelle : " + heure);
    }
}
```

#### Exemple avec `LocalDateTime` et manipulation :
```java
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class ExempleDateTime {
    public static void main(String[] args) {
        LocalDateTime dateTime = LocalDateTime.now();
        
        // Formater la date
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
        String dateStr = dateTime.format(formatter);
        
        System.out.println("Date et heure formatée : " + dateStr);
    }
}
```

#### Durées et périodes :
```java
import java.time.Duration;
import java.time.LocalDateTime;

public class ExempleDuree {
    public static void main(String[] args) {
        LocalDateTime debut = LocalDateTime.now();
        LocalDateTime fin = debut.plusHours(5).plusMinutes(30);
        
        Duration duree = Duration.between(debut, fin);
        System.out.println("Durée : " + duree.toHours() + " heures et " + duree.toMinutesPart() + " minutes.");
    }
}
```

### `java.io` : Lecture/écriture de fichiers
La bibliothèque `java.io` permet de gérer la lecture et l'écriture de fichiers (comme on a vu dans la section précédente).
- `FileReader` / `FileWriter` pour lire et écrire des fichiers texte.
- `BufferedReader` / `BufferedWriter` pour une lecture et écriture plus efficaces.
- `PrintWriter` pour une sortie formatée dans un fichier.

#### Exemple de lecture avec `BufferedReader` :
```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class LectureFichier {
    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new FileReader("monfichier.txt"))) {
            String ligne;
            while ((ligne = reader.readLine()) != null) {
                System.out.println(ligne);
            }
        } catch (IOException e) {
            System.out.println("Erreur de lecture : " + e.getMessage());
        }
    }
}
```

### `java.nio` : Fichiers et chemins modernes
Le package `java.nio` introduit des classes plus modernes pour la gestion des fichiers et des chemins. Cela inclut `Path`, `Files`, et des méthodes améliorées pour lire, écrire et manipuler les fichiers.

#### Exemple avec `Path` et `Files` :
```java
import java.nio.file.*;
import java.io.IOException;

public class ExempleNIO {
    public static void main(String[] args) {
        Path path = Paths.get("monfichier.txt");
        
        // Vérifier si le fichier existe
        if (Files.exists(path)) {
            System.out.println("Le fichier existe.");
        } else {
            System.out.println("Le fichier n'existe pas.");
        }
        
        // Lire tout le contenu du fichier
        try {
            String contenu = Files.readString(path);
            System.out.println("Contenu du fichier : " + contenu);
        } catch (IOException e) {
            System.out.println("Erreur de lecture avec NIO : " + e.getMessage());
        }
    }
}
```

#### Exemple avec `Files.copy()` :
```java
import java.nio.file.*;

public class CopierFichier {
    public static void main(String[] args) {
        Path source = Paths.get("source.txt");
        Path destination = Paths.get("destination.txt");
        
        try {
            Files.copy(source, destination, StandardCopyOption.REPLACE_EXISTING);
            System.out.println("Fichier copié avec succès !");
        } catch (IOException e) {
            System.out.println("Erreur de copie du fichier : " + e.getMessage());
        }
    }
}
```

### `java.net` : Programmation réseau
Le package `java.net` fournit des classes pour la communication réseau (TCP/IP, UDP, HTTP, etc.).

#### Exemple avec `Socket` pour la communication client-serveur :
- Client
```java
import java.net.*;
import java.io.*;

public class ClientSocket {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 12345)) {
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            out.println("Bonjour serveur !");
        } catch (IOException e) {
            System.out.println("Erreur du client : " + e.getMessage());
        }
    }
}
```

- Serveur
```java
import java.net.*;
import java.io.*;

public class ServeurSocket {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(12345)) {
            System.out.println("Serveur en attente de connexion...");
            Socket socket = serverSocket.accept();  // Attente d'une connexion

            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String message = in.readLine();
            System.out.println("Message reçu : " + message);
        } catch (IOException e) {
            System.out.println("Erreur du serveur : " + e.getMessage());
        }
    }
}
```
