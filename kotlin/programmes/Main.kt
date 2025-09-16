// Main.kt
// Exemple complet qui reprend les bases de Kotlin

// Déclaration d'une classe simple
open class Personne(val nom: String, val age: Int) {
    open fun sePresenter() {
        println("Bonjour, je m'appelle $nom et j'ai $age ans.")
    }
}

// Héritage avec "Student" qui hérite de "Personne"
class Etudiant(nom: String, age: Int, val filiere: String) : Personne(nom, age) {
    override fun sePresenter() {
        println("Salut ! Je suis $nom, j'ai $age ans et j'étudie $filiere.")
    }
}

// Une "data class" génère automatiquement toString, equals, hashCode...
data class Livre(val titre: String, val auteur: String)

fun addition(a: Int, b: Int): Int {
    return a + b
}

// Fonction avec valeur par défaut
fun multiplier(a: Int, b: Int = 2) = a * b

// Fonction qui peut renvoyer null
fun division(a: Int, b: Int): Int? {
    return if (b == 0) null else a / b
}

// Programme principal
fun main() {
    println("=== Variables et types ===")
    val immutable = 10       // val = variable immuable
    var mutable = 20         // var = variable modifiable
    mutable += 5
    println("val = $immutable, var = $mutable")

    val pi: Double = 3.14
    val actif: Boolean = true
    val lettre: Char = 'K'
    val nom: String = "Kotlin"
    println("Pi=$pi, actif=$actif, lettre=$lettre, nom=$nom")

    println("\n=== Saisie utilisateur ===")
    print("Entrez votre prénom : ")
    val prenom = readLine()
    println("Bonjour $prenom !")

    println("\n=== Opérations numériques ===")
    val a = 10
    val b = 3
    println("a+b=${a+b}, a-b=${a-b}, a*b=${a*b}, a/b=${a/b}, a%b=${a%b}")

    println("\n=== Conditions ===")
    val note = 15
    if (note >= 18) {
        println("Excellent !")
    } else if (note >= 10) {
        println("Admis")
    } else {
        println("Échec")
    }

    println("\n=== When (switch) ===")
    val jour = 3
    when (jour) {
        1 -> println("Lundi")
        2 -> println("Mardi")
        3 -> println("Mercredi")
        else -> println("Jour inconnu")
    }

    println("\n=== Boucles ===")
    for (i in 1..5) println("for i=$i")

    var i = 0
    while (i < 3) {
        println("while i=$i")
        i++
    }

    var j = 0
    do {
        println("do..while j=$j")
        j++
    } while (j < 2)

    println("\n=== Fonctions ===")
    println("Addition: 5+3=${addition(5,3)}")
    println("Multiplication avec valeur par défaut: 4*2=${multiplier(4)}")
    println("Multiplication 4*3=${multiplier(4,3)}")

    val res = division(10, 0) ?: "Division impossible"
    println("Division: $res")

    println("\n=== Collections ===")
    val fruits = mutableListOf("Pomme", "Banane")
    fruits.add("Orange")
    println("Fruits: $fruits")

    val ages = mapOf("Alexer" to 21, "Bob" to 30)
    println("Âge de Bob: ${ages["Bob"]}")

    println("\n=== Classes et héritage ===")
    val p = Personne("Jean", 40)
    val e = Etudiant("Alexer", 21, "Informatique")
    p.sePresenter()
    e.sePresenter()

    println("\n=== Data class ===")
    val livre = Livre("Kotlin en action", "JetBrains")
    println(livre)

    println("\n=== Null safety ===")
    val texte: String? = null
    println("Taille du texte: ${texte?.length ?: "inconnue"}")
}
