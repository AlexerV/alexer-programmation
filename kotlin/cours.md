# Kotlin

## Extension des fichiers et exécution
- Extension des fichiers Kotlin : `.kt`
- Kotlin peut être utilisé pour écrire :
  - des applications Android (le plus courant),
  - des applications desktop,
  - du backend (avec Spring Boot, Ktor),
  - ou des scripts simples.
> 👉 Kotlin est entièrement interopérable avec Java, c’est-à-dire que tu peux utiliser des bibliothèques Java dans un projet Kotlin.

- Compilation et exécution
```bash
kotlinc Main.kt -include-runtime -d main.jar
java -jar main.jar
```

- Exemple simple `Main.kt`:
```kotlin
fun main() {
    println("Bonjour Kotlin !")
}
```

---

## Les bases
- Kotlin est **typé statiquement**, mais avec une inférence de type.
- Les blocs de code sont délimités par `{ ... }`.
- Point d’entrée : fonction `main`.
```kotlin
fun main() {
    val nom = "Alexer"   // immuable
    var age = 21         // mutable
    println("Nom: $nom, Age: $age")
}
```

---

## Variables et types
- `val` : immuable (équivalent `final` en Java).
- `var` : variable mutable.  
Kotlin infère automatiquement le type :
```kotlin
val nom = "Alexer"   // String (constant)
var age = 21         // Int (modifiable)
```
> 👉 On recommande d’utiliser val par défaut, car un code immuable est plus sûr et plus simple à maintenir.

### Types courants
| Type      | Exemple         | Description                                 |
| --------- | --------------- | ------------------------------------------- |
| `Int`     | `42`            | Entier 32 bits                              |
| `Long`    | `42L`           | Entier long 64 bits                         |
| `Double`  | `3.14`          | Nombre décimal (64 bits)                    |
| `Float`   | `3.14f`         | Nombre décimal simple précision             |
| `Boolean` | `true`, `false` | Booléen                                     |
| `Char`    | `'A'`           | Caractère unique                            |
| `String`  | `"Bonjour"`     | Chaîne de caractères (mutable via méthodes) |

---

## Opérations arithmétiques et logiques
Kotlin reprend les opérateurs classiques :
```kotlin
val a = 10
val b = 3
println(a + b)  // 13
println(a % b)  // 1 (modulo)
```

> ⚡ Particularité : beaucoup d’opérateurs sont en réalité des fonctions.

Exemple :
```kotlin
val c = a.plus(b)   // équivalent à a + b
```

Exemple complet :
```kotlin
fun main() {
    val a = 10
    val b = 3
    println("Somme = ${a + b}")
    println("Modulo = ${a % b}")

    if (a > 0 && b > 0) {
        println("Les deux sont positifs !")
    }
}
```

---

## Entrées utilisateur
```kotlin
fun main() {
    print("Entrez votre nom : ")
    val nom = readLine()
    println("Bonjour $nom")
}
```
- `readLine()` retourne une chaîne nullable (`String?`), car la saisie peut échouer.

- On peut convertir en nombre :
```kotlin
val age = readLine()?.toInt() ?: 0
```
> 👉 Ici `?:` est **l’opérateur Elvis** : si la valeur est nulle, on met `0`.

---

## Conditions
### `if` / `else if` / `else`
Syntaxe :
```kotlin
if (condition) {
    code...
} else if (autre condition) {
    code...
} else {
    code...
}
```

Exemple :
```kotlin
fun main() {
    val note = 15
    if (note >= 18) {
        println("Excellent !")
    } else if (note >= 10) {
        println("Admis")
    } else {
        println("Échec")
    }
}
```

### when (équivalent switch/case)
```kotlin
fun main() {
    val jour = 3
    when (jour) {
        1 -> println("Lundi")
        2 -> println("Mardi")
        3 -> println("Mercredi")
        else -> println("Jour inconnu")
    }
}
```

> 👉 `when` peut aussi être utilisé comme expression :

```kotlin
val message = when (jour) {
    1 -> "Lundi"
    2 -> "Mardi"
    else -> "Autre jour"
}
```

---

## Boucles
### Boucle `for`
```kotlin
for (i in 1..5) {
    println(i) // 1 à 5 inclus
}
```
> 👉 `..` crée une range.

Pour exclure la borne supérieure, utilise `until` :
```kotlin
for (i in 1 until 5) println(i) // 1,2,3,4
```

### Boucle `while`
```kotlin
var i = 0
while (i < 5) {
    println("i = $i")
    i++
}
```

### Boucle `do...while`
```kotlin
var i = 0
do {
    println("i = $i")
    i++
} while (i < 5)
```

---

## Fonctions
### Délcaration :
```kotlin
fun addition(a: Int, b: Int): Int {
    return a + b
}
```

### Utilisation :
```kotlin
fun main() {
    println("Résultat = ${addition(5, 3)}")
}
```

### Fonction simple (expression unique) :
```kotlin
fun carre(x: Int) = x * x
```

### Paramètres avec valeur par défaut :
```kotlin
fun saluer(nom: String = "inconnu") {
    println("Bonjour $nom")
}
```

---

## Collections
### List (immuable)
```kotlin
val fruits = listOf("Pomme", "Banane", "Orange")
println(fruits[0])
```

### MutableList
```kotlin
val fruits = mutableListOf("Pomme", "Banane")
fruits.add("Orange")
println(fruits)
```

### Map
```kotlin
val notes = mapOf("Alexer" to 15, "Bob" to 12)
println(notes["Alexer"])
```

> 👉 Les collections en Kotlin sont riches et compatibles avec la **programmation fonctionnelle** :

```kotlin
val pairs = listOf(1,2,3,4,5).filter { it % 2 == 0 }
println(pairs) // [2,4]
```

---

## Classes et objets
```kotlin
class Personne(val nom: String, var age: Int)

fun main() {
    val p = Personne("Alexer", 21)
    println("${p.nom} a ${p.age} ans")
}
```
- `val nom` → propriété en lecture seule
- `var age` → propriété modifiable

---

## Data classes
Très utiles pour représenter des objets "données" :
```kotlin
data class Utilisateur(val nom: String, val age: Int)

fun main() {
    val u = Utilisateur("Alexer", 21)
    println(u)
}
```
> Kotlin génère automatiquement : `toString()`, `equals()`, `hashCode()`, `copy()`.

---

## Héritage et interfaces
```kotlin
open class Animal {
    open fun parler() {
        println("Je suis un animal")
    }
}

class Chien: Animal() {
    override fun parler() {
        println("Ouaf !")
    }
}

fun main() {
    val c = Chien()
    c.parler()
}
```

En Kotlin, les classes et méthodes sont `final` par défaut.  
Il faut utiliser `open` pour autoriser l’héritage.

---

## Null Safety
- En Kotlin, par défaut une variable ne peut pas être `null`. Cela évite de nombreuses erreurs (`NullPointerException`).
- Pour autoriser `null`, il faut utiliser `?`.
```kotlin
fun main() {
    var nom: String? = null
    println(nom?.length) // safe call
}
```
- `?` = appel sûr (si null → ne plante pas)
- `?:` = valeur par défaut
```kotlin
val longueur = nom?.length ?: 0
```

---

## Programmation fonctionnelle
Kotlin supporte les **lambdas** et les **fonctions d’ordre supérieur**.
```kotlin
fun main() {
    val nombres = listOf(1, 2, 3, 4, 5)
    val pairs = nombres.filter { it % 2 == 0 }
    println(pairs)
}
```

---

## Coroutines (Async/Await en Kotlin)
Les coroutines permettent d’écrire du code concurrent lisible.

### Exemple
Ajoute la dépendance (si projet Gradle) :
```gradle
implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.6.4")
```

Puis :
```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    launch {
        delay(1000L)
        println("Bonjour depuis une coroutine !")
    }
    println("Programme principal")
}
```
