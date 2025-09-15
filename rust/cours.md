# Rust

## Extension des fichiers et comment lancer un programme
- Extension des fichiers Rust : `.rs`
Chaque fichier source Rust se termine par `.rs`.
Un projet peut être lancé de deux façons :
- **Programme simple** avec `rustc` (compilation directe)
- **Projet structuré** avec `cargo` (outil officiel de gestion)

### Compilation et exécution simples
```bash
rustc main.rs   # compile le fichier en binaire
./main          # exécute le binaire
```

### Avec Cargo (recommandé)
```bash
cargo new mon_projet   # crée un projet
cd mon_projet
cargo run              # compile et exécute
```

Exemple `main.rs` :
```rust
fn main() {
    println!("Bonjour Rust !");
}
```

---

## Les bases
- Rust est un **langage compilé**, moderne, orienté sur la sécurité et la performance.
- Le point d’entrée est toujours la fonction `main` :
```rust
fn main() {
    // code ici
}
```
- Chaque instruction se termine par `;`.
- Les blocs sont délimités par `{ ... }`.

---

## Déclaration des variables
- Par défaut, les variables sont **immutables** (`let`).
- On peut rendre une variable **mutable** avec `mut`.

Exemple :
```rust
let age = 21;             // immuable
let mut taille = 1.73;    // mutable
let nom = "Alexer";       // chaîne de caractères
let actif: bool = true;   // booléen
```

Types courants :
- `i32` : entier signé
- `f64` : flottant
- `bool` : vrai/faux
- `char` : caractère
- `&str` : chaîne statique
- `String` : chaîne modifiable

---

## Opérations numériques et logiques

| Opération      | Symbole | Exemple          | Résultat |         |      |
| -------------- | ------- | ---------------- | -------- | ------- | ---- |
| Addition       | +       | `5 + 3`          | 8        |         |      |
| Soustraction   | -       | `5 - 3`          | 2        |         |      |
| Multiplication | \*      | `5 * 3`          | 15       |         |      |
| Division       | /       | `10 / 2`         | 5        |         |      |
| Modulo         | %       | `10 % 3`         | 1        |         |      |
| ET logique     | &&      | `a > 0 && b > 0` | true     |         |      |
| OU logique     | \|\|    | \`a > 0          |          | b > 0\` | true |
| NON logique    | !       | `!(a == b)`      | inverse  |         |      |

Exemple :
```rust
fn main(){
  let a = 10;
  let b = 3;

  println!("Somme: {}", a + b);
  println!("Modulo: {}", a % b);

  if a > 0 && b > 0 {
      println!("Les deux sont positifs !");
  }
}
```

---

## Entrées utilisateur
On utilise `std::io` pour lire dans le terminal.

```rust
use std::io;

fn main() {
    let mut nom = String::new();
    println!("Entrez votre nom :");
    io::stdin().read_line(&mut nom).expect("Erreur de lecture");

    println!("Bonjour, {}", nom.trim());
}
```

---

## Conditions
Syntaxe :
```rust
if condition {
    // bloc exécuté
} else if autre_condition {
    // bloc alternatif
} else {
    // sinon
}
```

Exemple :
```rust
fn main() {
    let note = 15;

    if note >= 18 {
        println!("Excellent !");
    } else if note >= 10 {
        println!("Admis");
    } else {
        println!("Échec");
    }
}
```

---

## Boucles
Rust propose plusieurs types de boucles.

### Boucle `for` (sur une plage ou une collection)
```rust
fn main() {
    for i in 0..5 {
        println!("i = {}", i);
    }
}
```

### Boucle `while`
```rust
fn main() {
    let mut i = 0;
    while i < 5 {
        println!("i = {}", i);
        i += 1;
    }
}
```

### Boucle `loop` (boucle infinie avec possibilité de `break`)
```rust
fn main() {
    let mut i = 0;
    loop {
        if i == 3 {
            break;
        }
        println!("i = {}", i);
        i += 1;
    }
}
```

| Boucle  | Quand l’utiliser                                          |
| ------- | --------------------------------------------------------- |
| `for`   | Parcourir une plage ou une collection (tableau, vecteur). |
| `while` | Répéter tant qu’une condition est vraie.                  |
| `loop`  | Répéter indéfiniment jusqu’à un `break`.                  |

### Parcourir un tableau
```rust
fn main() {
    let nombres = [1, 2, 3, 4, 5];
    for n in nombres.iter() {
        println!("{}", n);
    }
}
```

---

## Fonctions
### Déclaration :
```rust
fn addition(a: i32, b: i32) -> i32 {
    a + b
}
```

### Utilisation :
```rust
fn main() {
    let resultat = addition(5, 3);
    println!("Résultat = {}", resultat);
}
```

### Exemple complet :
```rust
fn addition(a: i32, b: i32) -> i32 {
    a + b
}

fn main() {
    let resultat = addition(5, 3);
    println!("Résultat = {}", resultat);
}
```

---

## Ownership et Borrowing (Propriété et emprunt)
Rust gère la mémoire grâce à un système unique appelé **ownership** (propriété).  
Chaque valeur a un "propriétaire", et une seule variable peut posséder une valeur à la fois.

Exemple :
```rust
fn main() {
    let s1 = String::from("Bonjour");
    let s2 = s1; // ownership transféré
    // println!("{}", s1); // ❌ Erreur : s1 n'est plus valide

    let s3 = String::from("Rust");
    let s4 = &s3; // emprunt (référence)
    println!("{} et {}", s3, s4); // ✅ utilisables tous les deux
}
```

### Règles principales
- Une valeur ne peut avoir qu’un seul propriétaire.
- On peut emprunter une valeur avec `&` (référence immuable).
- On peut emprunter en mutable avec `&mut`, mais un seul emprunt mutable à la fois est autorisé.
```rust
fn main() {
    let mut x = 5;
    let r1 = &mut x; // emprunt mutable
    *r1 += 1;
    println!("{}", r1);
}
```

---

## Lifetimes (durée de vie des références)
Les *lifetimes* indiquent combien de temps une référence reste valide.  
Rust les vérifie à la compilation pour éviter les références invalides.

Exemple :
```rust
fn plus_long<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

fn main() {
    let a = "Rust";
    let b = "Programmation";
    println!("Le plus long est : {}", plus_long(a, b));
}
```
Ici `'a` indique que le résultat aura une durée de vie au moins égale aux paramètres reçus.

---

## Structures de données
### Tableaux
```rust
fn main() {
    let nombres = [10, 20, 30];
    println!("Premier élément: {}", nombres[0]);
}
```

### Vecteurs (dynamiques)
```rust
fn main() {
    let mut fruits = Vec::new();
    fruits.push("Pomme");
    fruits.push("Banane");
    println!("{:?}", fruits);
}
```

### HashMap
```rust
fn main() {
    use std::collections::HashMap;

    let mut notes = HashMap::new();
    notes.insert("Alexer", 15);
    notes.insert("Bob", 12);

    println!("Note de Alexer: {:?}", notes.get("Alexer"));
}
```

---

## Structures et implémentations
Rust permet de définir des structures personnalisées avec `struct`, puis d’implémenter des méthodes avec `impl`.

Exemple :
```rust
struct Rectangle {
    largeur: u32,
    hauteur: u32,
}

impl Rectangle {
    fn aire(&self) -> u32 {
        self.largeur * self.hauteur
    }
}

fn main() {
    let rect = Rectangle { largeur: 30, hauteur: 10 };
    println!("Aire = {}", rect.aire());
}
```

---

## Enums (Énumérations)
Un `enum` permet de définir plusieurs variantes possibles pour une même donnée.

Exemple :
```rust
enum Direction {
    Nord,
    Sud,
    Est,
    Ouest,
}

fn main() {
    let d = Direction::Nord; // ici changer "Nord" par une autre direction (Sud, Est, Ouest)

    match d {
        Direction::Nord => println!("On va vers le Nord"),
        Direction::Sud => println!("On va vers le Sud"),
        _ => println!("Autre direction"),
    }
}
```

---

## Traits
Les `traits` définissent des comportements (semblables aux interfaces).

Exemple :
```rust
trait Decrire {
    fn decrire(&self) -> String;
}

struct Personne {
    nom: String,
}

impl Decrire for Personne {
    fn decrire(&self) -> String {
        format!("Je m'appelle {}", self.nom)
    }
}

fn main() {
    let p = Personne { nom: String::from("Alexer") };
    println!("{}", p.decrire());
}
```

---

## Pointeurs intelligents
Rust propose plusieurs pointeurs intelligents pour gérer la mémoire.

### `Box<T>`
Alloue une valeur sur le tas.
```rust
fn main() {
    let x = Box::new(10);
    println!("x = {}", x);
}
```

### `Rc<T>`
Compteur de références (plusieurs propriétaires possibles).
```rust
use std::rc::Rc;

fn main() {
    let a = Rc::new(5);
    let b = Rc::clone(&a);
    println!("a = {}, b = {}", a, b);
}
```

---

## Slices et Strings
### Slice
Permet de référencer une partie d’un tableau ou d’une chaîne.
```rust
fn main() {
    let tableau = [1, 2, 3, 4, 5];
    let tranche = &tableau[1..3]; // éléments 1 et 2
    println!("{:?}", tranche);
}
```

### String vs `&str`
- `&str` : chaîne statique (litérale).
- `String` : chaîne dynamique modifiable.

```rust
fn main() {
    let s1: &str = "Bonjour";
    let mut s2: String = String::from("Rust");
    s2.push_str(" !");
    println!("{} {}", s1, s2);
}
```

---

## Modules et organisation avec Cargo
Rust organise le code avec des modules (`mod`) et des imports (`use`).

Exemple :
```rust
mod outils {
    pub fn carre(x: i32) -> i32 {
        x * x
    }
}

fn main() {
    println!("4^2 = {}", outils::carre(4));
}
```
Avec `cargo`, un projet est structuré ainsi :
```css
src/
 └── main.rs
 └── lib.rs
```

---

## Macros
Les macros permettent de générer du code.  
Exemple classique : `println!`.

Exemple de macro personnalisée :
```rust
macro_rules! carre {
    ($x:expr) => {
        $x * $x
    };
}

fn main() {
    println!("5^2 = {}", carre!(5));
}
```

---

## Match (équivalent du switch/case)
```rust
fn main() {
    let jour = 3;
    match jour {
        1 => println!("Lundi"),
        2 => println!("Mardi"),
        3 => println!("Mercredi"),
        _ => println!("Jour inconnu"),
    }
}
```

---

## Gestion des erreurs avec Option et Result
Rust ne dispose pas d’`exceptions`. À la place, il utilise les types `Option` et `Result`.

### Option
Permet de représenter une valeur qui peut exister ou non :
```rust
fn division(a: i32, b: i32) -> Option<i32> {
    if b == 0 {
        None
    } else {
        Some(a / b)
    }
}

fn main() {
    match division(10, 2) { // remplacer le "2" par "0"
        Some(r) => println!("Résultat = {}", r),
        None => println!("Division par zéro interdite"),
    }
}
```

### Result
Utilisé pour représenter succès (`Ok`) ou erreur (`Err`) :
```rust
use std::fs::File;

fn main() {
    match File::open("inexistant.txt") {
        Ok(_) => println!("Fichier ouvert"),
        Err(e) => println!("Erreur : {}", e),
    }
}
```

---

## Concurrence et Async
Rust propose plusieurs façons de gérer le parallélisme.

### Threads
```rust
use std::thread;

fn main() {
    let handle = thread::spawn(|| {
        println!("Bonjour depuis un thread !");
    });

    handle.join().unwrap();
}
```

### Async / Await (avec Tokio ou async-std)
Rust permet d’écrire du code **asynchrone** grâce au mot-clé `async` et à l’opérateur `await`.  
Cependant, pour exécuter ce type de code, il faut utiliser un *runtime asynchrone* comme **Tokio** ou **async-std**.

### Exemple avec Tokio

1. Créer un projet :
```bash
cargo new mon_projet
cd mon_projet
```

2. Ajouter la dépendance dans `Cargo.toml` :
```toml
[dependencies]
tokio = { version = "1", features = ["full"] }
```

3. Code dans `src/main.rs` :
```rust
#[tokio::main]
async fn main() {
    println!("Début du programme async...");

    ma_fonction().await;
}

async fn ma_fonction() {
    println!("Cette fonction est exécutée en mode async !");
}
```

4. Compiler et exécuter avec Cargo :
```bash
cargo run
```

### Pourquoi pas `rustc main.rs` ?
- `rustc` compile seulement un fichier source, il ne lit pas le fichier `Cargo.toml`.
- Sans `Cargo`, les dépendances comme **Tokio** ou **async-std** ne seront pas téléchargées.
- Par défaut, `rustc` compile en édition 2015, ce qui peut poser problème avec du code moderne (`async/await` vient avec l’édition 2018+).
> 👉 Donc pour tout projet qui utilise des **librairies externes**, passe toujours par Cargo.
