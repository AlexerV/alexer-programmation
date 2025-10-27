# Go (Golang)

## Extension des fichiers et exécution

- Extension des fichiers Go : `.go`

### Exécution et compilation

```bash
# Exécuter directement sans compiler
go run main.go

# Compiler et créer un exécutable
go build main.go
./main           # Linux/macOS
main.exe         # Windows

# Compiler avec un nom personnalisé
go build -o monprogramme main.go
```

### Exemple simple
```go
// main.go
package main

import "fmt"

func main() {
    fmt.Println("Hello, Go!")
}
```
> 💡 Point important : Tout programme Go exécutable doit avoir un package `main` et une fonction `main()`.

---

## Les bases
- Go est un langage compilé et statiquement typé.
- Le point d'entrée est toujours la fonction `main` dans le package `main`.
- Les accolades `{ }` délimitent les blocs de code.
- Go utilise l'indentation automatique via `gofmt`.
- Pas besoin de point-virgule `;` à la fin des instructions (ajouté automatiquement).
- Les variables non utilisées génèrent une erreur de compilation.
- La casse est importante (`maVariable` ≠ `mavariable`).

### Organisation d'un fichier Go
```go
package main              // Déclaration du package

import "fmt"              // Import des packages

func main() {             // Fonction principale
    fmt.Println("Go!")
}
```

---

## Déclaration des variables
### Types de base
| Type      | Description                | Exemple               |
| --------- | -------------------------- | --------------------- |
| `int`     | Entier (32 ou 64 bits)     | `42`                  |
| `int8`    | Entier 8 bits              | `127`                 |
| `int16`   | Entier 16 bits             | `32767`               |
| `int32`   | Entier 32 bits             | `2147483647`          |
| `int64`   | Entier 64 bits             | `9223372036854775807` |
| `uint`    | Entier non signé           |  `42`                 |
| `float32` | Nombre décimal 32 bits     |  `3.14`               |
| `float64` | Nombre décimal 64 bits     |  `3.14159265359`      |
| `bool`    | Booléen                    |  `true` / `false`     |
| `string`  | Chaîne de caractères       |  `"Hello"`            |
| `byte`    | Alias pour uint8           |  `'A'`                |
| `rune`    | Alias pour int32 (Unicode) |  `'€'`                |

### Déclaration de variables
```go
// Déclaration explicite avec type
var age int = 21
var nom string = "Alexer"

// Inférence de type
var taille = 1.73        // float64 par défaut
var estConnecte = true   // bool

// Déclaration courte (uniquement dans les fonctions)
prenom := "Alex"
compteur := 10

// Déclaration multiple
var x, y int = 10, 20
a, b := 5, "texte"

// Valeur zéro par défaut
var n int        // n = 0
var s string     // s = ""
var isValid bool // isValid = false
```

### Constantes
```go
const Pi = 3.14159
const (
    Lundi = 1
    Mardi = 2
    Mercredi = 3
)
```

---

## Opérations numériques
Go supporte les opérations classiques :
| Opération      | Symbole | Exemple  | Résultat |
| -------------- | ------- | -------- | -------- |
| Addition       | +       | `5 + 3`  | 8        |
| Soustraction   | -       | `5 - 3`  | 2        |
| Multiplication | \*      | `5 * 3`  | 15       |
| Division       | /       | `10 / 2` | 5        |
| Modulo         | %       | `10 % 3` | 1        |

```go
a := 10
b := 3
somme := a + b        // 13
reste := a % b        // 1
division := a / b     // 3 (division entière)
divFloat := float64(a) / float64(b)  // 3.333...
```

### Opérateurs d'incrémentation
```go
compteur := 0
compteur++    // compteur = 1
compteur--    // compteur = 0
compteur += 5 // compteur = 5
compteur *= 2 // compteur = 10
```

---

## Saisir des informations
Pour lire des entrées utilisateur, on utilise le package `fmt` :
```go
package main

import "fmt"

func main() {
    var nom string
    var age int

    fmt.Print("Entrez votre nom : ")
    fmt.Scan(&nom)

    fmt.Print("Entrez votre âge : ")
    fmt.Scan(&age)

    fmt.Printf("Bonjour %s, vous avez %d ans.\n", nom, age)
}
```

### Lecture d'une ligne complète
```go
import (
    "bufio"
    "fmt"
    "os"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("Entrez votre nom complet : ")
    nom, _ := reader.ReadString('\n')
    fmt.Println("Bonjour", nom)
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

```go
if a == b {
    fmt.Println("a est égal à b")
}
```

---

## Structures conditionnelles
### `If` / `Else`
```go
age := 18

if age >= 18 {
    fmt.Println("Majeur")
} else {
    fmt.Println("Mineur")
}
```

### `If` avec initialisation
```go
if age := 20; age >= 18 {
    fmt.Println("Majeur")
}
// age n'est plus accessible ici
```

### `Else if`
```go
note := 15

if note >= 16 {
    fmt.Println("Très bien")
} else if note >= 14 {
    fmt.Println("Bien")
} else if note >= 10 {
    fmt.Println("Passable")
} else {
    fmt.Println("Insuffisant")
}
```

---

## Opérateurs logiques
- `&&` : ET logique (`a > 0 && b < 10`)
- `||` : OU logique (`a < 0 || b > 10`)
- `!` : NON logique (`!(a == b)`)

```go
age := 25
estConnecte := true

if age >= 18 && estConnecte {
    fmt.Println("Accès autorisé")
}

if age < 18 || !estConnecte {
    fmt.Println("Accès refusé")
}
```

---

## Boucles
> 💡 Particularité de Go : Il n'existe qu'un seul type de boucle : `for`. Mais elle peut être utilisée de plusieurs façons !

### Boucle `for` classique
```go
for i := 0; i < 5; i++ {
    fmt.Println("i =", i)
}
```

### Boucle `while` (équivalent)
```go
i := 0
for i < 5 {
    fmt.Println("i =", i)
    i++
}
```

### Boucle infinie
```go
for {
    fmt.Println("Boucle infinie")
    break  // Sortie de la boucle
}
```

### Boucle sur un tableau/slice
```go
nombres := []int{10, 20, 30, 40}

// Avec index et valeur
for index, valeur := range nombres {
    fmt.Printf("Index %d : %d\n", index, valeur)
}

// Seulement la valeur (ignorer l'index avec _)
for _, valeur := range nombres {
    fmt.Println(valeur)
}
```

### `Break` et `Continue`
```go
for i := 0; i < 10; i++ {
    if i == 3 {
        continue  // Passe à l'itération suivante
    }
    if i == 7 {
        break     // Sort de la boucle
    }
    fmt.Println(i)
}
```

---

## Fonctions
### Déclaration de base
```go
func addition(a int, b int) int {
    return a + b
}

// Types identiques raccourcis
func soustraction(a, b int) int {
    return a - b
}
```

### Fonction sans retour
```go
func direBonjour(nom string) {
    fmt.Println("Bonjour", nom)
}
```

### Valeurs de retour multiples
```go
package main

import "fmt"

func division(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division par zéro")
    }
    return a / b, nil
}

func main() {
    resultat, err := division(10, 2)
    if err != nil {
        fmt.Println("Erreur:", err)
    } else {
        fmt.Println("Résultat:", resultat)
    }
}
```

### Retours nommés
```go
func calculer(a, b int) (somme int, produit int) {
    somme = a + b
    produit = a * b
    return  // Retourne automatiquement somme et produit
}
```

### Fonctions variadiques
```go
func somme(nombres ...int) int {
    total := 0
    for _, n := range nombres {
        total += n
    }
    return total
}

resultat := somme(1, 2, 3, 4, 5)  // 15
```

### Fonctions anonymes et closures
```go
// Fonction anonyme
multiplier := func(a, b int) int {
    return a * b
}
fmt.Println(multiplier(3, 4))  // 12

// Closure
func compteur() func() int {
    n := 0
    return func() int {
        n++
        return n
    }
}

c := compteur()
fmt.Println(c())  // 1
fmt.Println(c())  // 2
```

---

## Tableaux et Slices
### Tableaux (taille fixe)
```go
// Déclaration avec taille fixe
var nombres [5]int
nombres[0] = 10
nombres[1] = 20

// Initialisation
nombres := [5]int{10, 20, 30, 40, 50}

// Taille automatique
nombres := [...]int{10, 20, 30}

fmt.Println(len(nombres))  // 3
```

### Slices (taille dynamique)
```go
// Déclaration
var fruits []string

// Initialisation
fruits = []string{"Pomme", "Banane", "Orange"}

// Ajout d'éléments
fruits = append(fruits, "Fraise")

// Accès
fmt.Println(fruits[0])  // Pomme

// Longueur et capacité
fmt.Println(len(fruits))  // 4
fmt.Println(cap(fruits))  // capacité
```

### Création avec make
```go
// Slice avec longueur et capacité
nombres := make([]int, 5)      // longueur 5, capacité 5
nombres := make([]int, 5, 10)  // longueur 5, capacité 10
```

### Découpage de slices
```go
nombres := []int{0, 1, 2, 3, 4, 5}

slice1 := nombres[1:4]   // [1, 2, 3]
slice2 := nombres[:3]    // [0, 1, 2]
slice3 := nombres[3:]    // [3, 4, 5]
slice4 := nombres[:]     // copie complète
```

---

## Maps (dictionnaires)
```go
// Déclaration
var ages map[string]int

// Initialisation avec make
ages = make(map[string]int)

// Ajout d'éléments
ages["Alexer"] = 21
ages["Bob"] = 30

// Initialisation directe
ages := map[string]int{
    "Alexer": 21,
    "Bob":   30,
    "Eve":   28,
}

// Accès
fmt.Println(ages["Alexer"])  // 21

// Vérifier l'existence d'une clé
age, existe := ages["Charlie"]
if existe {
    fmt.Println("Charlie a", age, "ans")
} else {
    fmt.Println("Charlie n'existe pas")
}

// Suppression
delete(ages, "Bob")

// Parcourir une map
for nom, age := range ages {
    fmt.Printf("%s a %d ans\n", nom, age)
}
```

---

## Switch case
```go
jour := 3

switch jour {
case 1:
    fmt.Println("Lundi")
case 2:
    fmt.Println("Mardi")
case 3:
    fmt.Println("Mercredi")
case 4, 5:  // Plusieurs valeurs
    fmt.Println("Jeudi ou Vendredi")
default:
    fmt.Println("Weekend")
}
```

### Switch sans condition (comme if/else)
```go
heure := 14

switch {
case heure < 12:
    fmt.Println("Matin")
case heure < 18:
    fmt.Println("Après-midi")
default:
    fmt.Println("Soir")
}
```

### Switch avec initialisation
```go
switch age := 25; {
case age < 18:
    fmt.Println("Mineur")
case age < 65:
    fmt.Println("Adulte")
default:
    fmt.Println("Senior")
}
```

---

## Structures (struct)
```go
// Déclaration d'une structure
type Personne struct {
    Nom    string
    Age    int
    Ville  string
}

// Création d'une instance
p1 := Personne{
    Nom:   "Alexer",
    Age:   21,
    Ville: "Paris",
}

// Création avec ordre des champs
p2 := Personne{"Bob", 30, "Lyon"}

// Accès aux champs
fmt.Println(p1.Nom)    // Alexer
p1.Age = 26

// Structures anonymes
coord := struct {
    X int
    Y int
}{10, 20}
```

### Structures imbriquées
```go
type Adresse struct {
    Rue   string
    Ville string
}

type Personne struct {
    Nom     string
    Adresse Adresse
}

p := Personne{
    Nom: "Charlie",
    Adresse: Adresse{
        Rue:   "123 Main St",
        Ville: "Paris",
    },
}

fmt.Println(p.Adresse.Ville)  // Paris
```

---

## Pointeurs
```go
// Déclaration d'une variable
x := 42

// Pointeur vers x
ptr := &x

// Accès à la valeur via le pointeur
fmt.Println(*ptr)  // 42

// Modification via le pointeur
*ptr = 100
fmt.Println(x)  // 100

// Pointeur nil
var p *int
if p == nil {
    fmt.Println("Pointeur nil")
}
```

### Pointeurs avec fonctions
```go
func modifier(x *int) {
    *x = *x * 2
}

nombre := 10
modifier(&nombre)
fmt.Println(nombre)  // 20
```

### Pointeurs avec structures
```go
type Personne struct {
    Nom string
    Age int
}

func anniversaire(p *Personne) {
    p.Age++  // Go dé-référence automatiquement
}

personne := Personne{"Alexer", 21}
anniversaire(&personne)
fmt.Println(personne.Age)  // 26
```

---

## Méthodes
Les méthodes sont des fonctions associées à un type :
```go
type Rectangle struct {
    Largeur  float64
    Hauteur  float64
}

// Méthode avec récepteur par valeur
func (r Rectangle) Aire() float64 {
    return r.Largeur * r.Hauteur
}

// Méthode avec récepteur par pointeur
func (r *Rectangle) Doubler() {
    r.Largeur *= 2
    r.Hauteur *= 2
}

// Utilisation
rect := Rectangle{10, 5}
fmt.Println(rect.Aire())  // 50

rect.Doubler()
fmt.Println(rect.Aire())  // 200
```

---

## Interfaces
Les interfaces définissent un ensemble de méthodes :
```go
// Définition d'une interface
type Forme interface {
    Aire() float64
    Perimetre() float64
}

// Rectangle implémente Forme
type Rectangle struct {
    Largeur, Hauteur float64
}

func (r Rectangle) Aire() float64 {
    return r.Largeur * r.Hauteur
}

func (r Rectangle) Perimetre() float64 {
    return 2 * (r.Largeur + r.Hauteur)
}

// Cercle implémente Forme
type Cercle struct {
    Rayon float64
}

func (c Cercle) Aire() float64 {
    return 3.14 * c.Rayon * c.Rayon
}

func (c Cercle) Perimetre() float64 {
    return 2 * 3.14 * c.Rayon
}

// Fonction utilisant l'interface
func afficherInfos(f Forme) {
    fmt.Printf("Aire: %.2f, Périmètre: %.2f\n", f.Aire(), f.Perimetre())
}

// Utilisation
rect := Rectangle{10, 5}
cercle := Cercle{7}

afficherInfos(rect)
afficherInfos(cercle)
```

### Interface vide
```go
// Interface vide - peut contenir n'importe quel type
var x interface{}

x = 42
x = "texte"
x = true

// Type assertion
valeur, ok := x.(int)
if ok {
    fmt.Println("C'est un entier:", valeur)
}
```

---

## Gestion d'erreurs
Go utilise des valeurs de retour explicites pour gérer les erreurs :
```go
import (
    "errors"
    "fmt"
)

func division(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division par zéro impossible")
    }
    return a / b, nil
}

// Utilisation
resultat, err := division(10, 0)
if err != nil {
    fmt.Println("Erreur:", err)
} else {
    fmt.Println("Résultat:", resultat)
}
```

### Créer des erreurs personnalisées
```go
import "fmt"

type ErreurDivision struct {
    Dividende float64
    Diviseur  float64
}

func (e *ErreurDivision) Error() string {
    return fmt.Sprintf("impossible de diviser %.2f par %.2f", e.Dividende, e.Diviseur)
}

func division(a, b float64) (float64, error) {
    if b == 0 {
        return 0, &ErreurDivision{a, b}
    }
    return a / b, nil
}
```

---

## Goroutines et Concurrence
Les goroutines permettent d'exécuter du code en parallèle :
```go
import (
    "fmt"
    "time"
)

func afficher(texte string) {
    for i := 0; i < 5; i++ {
        fmt.Println(texte, i)
        time.Sleep(100 * time.Millisecond)
    }
}

func main() {
    // Exécution synchrone
    afficher("Sync")

    // Exécution asynchrone avec goroutine
    go afficher("Async 1")
    go afficher("Async 2")

    // Attendre pour que les goroutines se terminent
    time.Sleep(1 * time.Second)
}
```

### WaitGroup pour synchroniser
```go
import (
    "fmt"
    "sync"
)

func travail(id int, wg *sync.WaitGroup) {
    defer wg.Done()  // Signale la fin
    fmt.Printf("Travail %d commence\n", id)
    time.Sleep(time.Second)
    fmt.Printf("Travail %d terminé\n", id)
}

func main() {
    var wg sync.WaitGroup

    for i := 1; i <= 3; i++ {
        wg.Add(1)
        go travail(i, &wg)
    }

    wg.Wait()  // Attend que toutes les goroutines se terminent
    fmt.Println("Tous les travaux sont terminés")
}
```

---

## Channels
Les channels permettent la communication entre goroutines :
```go
// Créer un channel
messages := make(chan string)

// Envoyer dans un channel (dans une goroutine)
go func() {
    messages <- "Hello"
}()

// Recevoir depuis un channel
msg := <-messages
fmt.Println(msg)
```

### Channel avec buffer
```go
// Channel avec buffer de taille 2
messages := make(chan string, 2)

messages <- "premier"
messages <- "deuxième"

fmt.Println(<-messages)
fmt.Println(<-messages)
```

### Fermer un channel
```go
jobs := make(chan int, 5)

// Envoyer des valeurs
for i := 1; i <= 5; i++ {
    jobs <- i
}
close(jobs)  // Fermer le channel

// Recevoir jusqu'à la fermeture
for job := range jobs {
    fmt.Println("Job:", job)
}
```

### Select pour plusieurs channels
```go
c1 := make(chan string)
c2 := make(chan string)

go func() {
    time.Sleep(1 * time.Second)
    c1 <- "un"
}()

go func() {
    time.Sleep(2 * time.Second)
    c2 <- "deux"
}()

for i := 0; i < 2; i++ {
    select {
    case msg1 := <-c1:
        fmt.Println("Reçu", msg1)
    case msg2 := <-c2:
        fmt.Println("Reçu", msg2)
    }
}
```

---

## Defer, Panic et Recover
### Defer (exécution différée)
```go
func main() {
    defer fmt.Println("Fin")  // S'exécute à la fin
    fmt.Println("Début")
    fmt.Println("Milieu")
}
// Affiche: Début, Milieu, Fin
```

### Panic (erreur fatale)
```go
func risque() {
    panic("Quelque chose s'est mal passé!")
}

func main() {
    risque()
    fmt.Println("Ceci ne sera jamais affiché")
}
```

### Recover (récupération après panic)
```go
func risque() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Récupéré de:", r)
        }
    }()
    panic("Erreur!")
    fmt.Println("Jamais exécuté")
}

func main() {
    risque()
    fmt.Println("Programme continue")
}
```

---

## Fichiers et entrées/sorties
### Écrire dans un fichier
```go
import (
    "fmt"
    "os"
)

func main() {
    // Créer/ouvrir un fichier
    fichier, err := os.Create("monfichier.txt")
    if err != nil {
        fmt.Println("Erreur:", err)
        return
    }
    defer fichier.Close()

    // Écrire dans le fichier
    fichier.WriteString("Bonjour Go!\n")
    fichier.WriteString("Ligne 2\n")

    fmt.Println("Fichier créé avec succès")
}
```

### Lire un fichier
```go
import (
    "fmt"
    "os"
)

func main() {
    // Lire tout le contenu
    contenu, err := os.ReadFile("monfichier.txt")
    if err != nil {
        fmt.Println("Erreur:", err)
        return
    }
    fmt.Println(string(contenu))
}
```

### Lire ligne par ligne
```go
import (
    "bufio"
    "fmt"
    "os"
)

func main() {
    fichier, err := os.Open("monfichier.txt")
    if err != nil {
        fmt.Println("Erreur:", err)
        return
    }
    defer fichier.Close()

    scanner := bufio.NewScanner(fichier)
    for scanner.Scan() {
        fmt.Println(scanner.Text())
    }

    if err := scanner.Err(); err != nil {
        fmt.Println("Erreur de lecture:", err)
    }
}
```

### Ajouter du contenu à un fichier
```go
fichier, err := os.OpenFile("monfichier.txt", os.O_APPEND|os.O_WRONLY, 0644)
if err != nil {
    fmt.Println("Erreur:", err)
    return
}
defer fichier.Close()

fichier.WriteString("Nouvelle ligne ajoutée\n")
```

---

## Packages et Modules
### Structure d'un projet
```
monprojet/
├── go.mod
├── main.go
└── utils/
    └── helpers.go
```

### Initialiser un module
```bash
go mod init github.com/username/monprojet
```

### Créer un package
```go
// utils/helpers.go
package utils

import "fmt"

// Fonction exportée (commence par une majuscule)
func Saluer(nom string) {
    fmt.Println("Bonjour", nom)
}

// Fonction non exportée (commence par une minuscule)
func calculerInterne() int {
    return 42
}
```

### Utiliser un package
```go
// main.go
package main

import (
    "github.com/username/monprojet/utils"
)

func main() {
    utils.Saluer("Alexer")
}
```

### Installer des dépendances
```bash
# Installer un package externe
go get github.com/gorilla/mux

# Nettoyer les dépendances
go mod tidy
```

---

## Bibliothèques utiles
### `fmt` : Formatage et affichage
```go
import "fmt"

// Affichage
fmt.Println("Hello")           // Avec retour à la ligne
fmt.Print("Hello")              // Sans retour à la ligne
fmt.Printf("Age: %d\n", 21)     // Formaté

// Formatage dans une string
s := fmt.Sprintf("Nom: %s, Age: %d", "Alexer", 21)
```

### Verbes de formatage courants :
| Verbe | Description         | Exemple |
| ------| ------------------- | ------- |
| `%v`  | Valeur par défaut   | `%v`    |
| `%+v` | Avec noms de champs | `%+v`   |
| `%#v` | Représentation Go   | `%#v`   |
| `%T`  | Type de la variable | `%T`    |
| `%d`  | Entier décimal      | `%d`    |
| `%f`  | Nombre décimal      | `%.2f`  |
| `%s`  | String              | `%s`    |
| `%t`  | Boolean             | `%t`    |
| `%p`  | Pointeur            | `%p`    |

### `strings` : Manipulation de chaînes
```go
import "strings"

s := "Hello World"

// Vérifications
strings.Contains(s, "World")      // true
strings.HasPrefix(s, "Hello")     // true
strings.HasSuffix(s, "World")     // true

// Transformations
strings.ToUpper(s)                // "HELLO WORLD"
strings.ToLower(s)                // "hello world"
strings.Replace(s, "World", "Go", 1)  // "Hello Go"
strings.ReplaceAll(s, "l", "L")   // "HeLLo WorLd"

// Découpage et jointure
parts := strings.Split("a,b,c", ",")  // ["a", "b", "c"]
joined := strings.Join(parts, "-")     // "a-b-c"

// Suppression d'espaces
strings.TrimSpace("  hello  ")    // "hello"
```

### `strconv` : Conversions de types
```go
import "strconv"

// String vers int
i, err := strconv.Atoi("42")
if err != nil {
    fmt.Println("Erreur de conversion")
}

// Int vers string
s := strconv.Itoa(42)

// String vers float
f, err := strconv.ParseFloat("3.14", 64)

// Float vers string
s := strconv.FormatFloat(3.14159, 'f', 2, 64)  // "3.14"

// String vers bool
b, err := strconv.ParseBool("true")
```

### `time` : Gestion du temps
```go
import "time"

// Temps actuel
maintenant := time.Now()
fmt.Println(maintenant)

// Date spécifique
date := time.Date(2025, 12, 25, 10, 30, 0, 0, time.UTC)

// Formatage (référence: Mon Jan 2 15:04:05 MST 2006)
dateStr := maintenant.Format("02/01/2006 15:04:05")
dateStr := maintenant.Format("2006-01-02")

// Parsing
t, err := time.Parse("2006-01-02", "2025-10-27")

// Opérations
dans1heure := maintenant.Add(1 * time.Hour)
hier := maintenant.Add(-24 * time.Hour)

// Durées
duree := time.Since(maintenant)  // Temps écoulé
time.Sleep(2 * time.Second)      // Pause
```

### `math` : Opérations mathématiques
```go
import "math"

// Puissances et racines
math.Pow(2, 3)        // 8
math.Sqrt(16)         // 4
math.Cbrt(27)         // 3

// Arrondis
math.Ceil(3.14)       // 4
math.Floor(3.14)      // 3
math.Round(3.5)       // 4

// Valeurs absolues
math.Abs(-5)          // 5

// Trigonométrie
math.Sin(math.Pi / 2) // 1
math.Cos(0)           // 1

// Constantes
math.Pi               // 3.141592653589793
math.E                // 2.718281828459045
```

### `math/rand` : Nombres aléatoires
```go
import (
    "math/rand"
    "time"
)

// Initialiser le générateur (optionnel en Go 1.20+)
rand.Seed(time.Now().UnixNano())

// Nombres aléatoires
n := rand.Intn(100)           // Entre 0 et 99
f := rand.Float64()           // Entre 0.0 et 1.0
n := rand.Intn(10) + 1        // Entre 1 et 10
```

### `os` : Système d'exploitation
```go
import "os"

// Variables d'environnement
home := os.Getenv("HOME")
os.Setenv("MA_VAR", "valeur")

// Arguments de ligne de commande
args := os.Args  // os.Args[0] est le nom du programme

// Répertoire de travail
dir, _ := os.Getwd()
os.Chdir("/tmp")

// Informations sur fichiers
info, err := os.Stat("fichier.txt")
if err == nil {
    fmt.Println(info.Size())      // Taille
    fmt.Println(info.ModTime())   // Date de modification
    fmt.Println(info.IsDir())     // Est un répertoire?
}

// Créer/supprimer répertoires
os.Mkdir("mondir", 0755)
os.MkdirAll("dir/subdir/subsubdir", 0755)
os.Remove("fichier.txt")
os.RemoveAll("mondir")
```

### `io` : Entrées/sorties
```go
import "io"

// Copier un fichier
source, _ := os.Open("source.txt")
defer source.Close()

destination, _ := os.Create("dest.txt")
defer destination.Close()

io.Copy(destination, source)
```

### `encoding/json` : JSON
```go
import "encoding/json"

type Personne struct {
    Nom string `json:"nom"`
    Age int    `json:"age"`
}

// Encoder (Go vers JSON)
p := Personne{"Alexer", 21}
jsonData, err := json.Marshal(p)
fmt.Println(string(jsonData))  // {"nom":"Alexer","age":21}

// Encoder avec indentation
jsonData, err := json.MarshalIndent(p, "", "  ")

// Décoder (JSON vers Go)
jsonStr := `{"nom":"Bob","age":30}`
var p2 Personne
err := json.Unmarshal([]byte(jsonStr), &p2)
```

### `net/http` : Serveur et client HTTP
```go
import "net/http"

// Serveur HTTP simple
func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, %s!", r.URL.Path[1:])
}

func main() {
    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}

// Client HTTP
resp, err := http.Get("https://api.example.com/data")
if err != nil {
    fmt.Println("Erreur:", err)
    return
}
defer resp.Body.Close()

body, _ := io.ReadAll(resp.Body)
fmt.Println(string(body))
```

### `regexp` : Expressions régulières
```go
import "regexp"

// Vérifier une correspondance
matched, _ := regexp.MatchString(`\d+`, "abc123")  // true

// Compiler un pattern
re := regexp.MustCompile(`[a-z]+`)

// Trouver
result := re.FindString("abc123def")  // "abc"

// Trouver tous
results := re.FindAllString("abc 123 def", -1)  // ["abc", "def"]

// Remplacer
result := re.ReplaceAllString("abc123def", "X")  // "X123X"
```

---

## Bonnes pratiques
### Conventions de nommage
- Variables et fonctions : `camelCase` (`monNombre`, `calculerSomme`)
- Fonctions/types exportés : `PascalCase` (`Calculer`, `TypePersonne`)
- Constantes : `PascalCase` ou `MAJUSCULES` (`Pi`, `MAX_SIZE`)
- Packages : minuscules, un seul mot (`fmt`, `http`, `json`)

### Gestion des erreurs
```go
// ✅ Bon
if err != nil {
    return fmt.Errorf("échec de l'opération: %w", err)
}

// ❌ Mauvais
if err != nil {
    panic(err)  // À éviter sauf cas exceptionnel
}
```

### Commentaires pour documentation
```go
// Calculer additionne deux nombres et retourne le résultat.
// Cette fonction ne gère pas les débordements.
func Calculer(a, b int) int {
    return a + b
}
```

### Tests unitaires
```go
// calculator_test.go
package main

import "testing"

func TestAddition(t *testing.T) {
    resultat := addition(2, 3)
    if resultat != 5 {
        t.Errorf("Attendu 5, obtenu %d", resultat)
    }
}

// Exécuter les tests
// go test
```
