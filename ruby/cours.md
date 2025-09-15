# Ruby

---

## Extension des fichiers Ruby et comment lancer un programme
- Extension des fichiers Ruby : `.rb`

Chaque fichier source Ruby se termine par `.rb`.

- Exécution :

Sur Windows / Linux / macOS, une fois Ruby installé, tu peux lancer un programme directement via le terminal :
```bash
ruby mon_programme.rb
```

- Exemple :
```ruby
# mon_programme.rb
puts "Bonjour Ruby !"
```

- Puis lancer :
```bash
ruby mon_programme.rb
```

Contrairement à Java, Ruby est un langage interprété : il n’a pas besoin de compilation préalable.  
Le code est exécuté directement.

---

## Les bases
- Ruby est un langage interprété et orienté objet.
- L’exécution d’un script démarre du haut vers le bas du fichier.
- Les blocs de code sont délimités par `end`.
- Pas de point-virgule obligatoire à la fin des lignes.
- La casse est importante (`maVariable` ≠ `mavariable`).

---

## Particularités de Ruby
- **Interpolation de chaînes** :  
```ruby
nom = "Alexer"
puts "Bonjour #{nom}"  # Bonjour Alexer
```

- **Symbols** : objets légers souvent utilisés comme clés dans les Hash.
```ruby
personne = { nom: "Alexer", age: 21 }
puts personne[:nom]  # Alexer
```

- Ranges (plages) :
```ruby
for i in 1..5
  puts i
end
```

- Tout est objet :
```ruby
puts 5.even?  # true
puts "Ruby".upcase  # RUBY
```

---

## Déclaration des variables
En Ruby, il n’y a pas de typage explicite. Les variables prennent le type du contenu.

Exemple :
```ruby
age = 21
taille = 1.73
est_connecte = true
initiale = 'J'
nom = "Alexer"
```

---

## Opérations numériques
Ruby supporte les opérations classiques :
| Opération      | Symbole | Exemple  | Résultat |
| -------------- | ------- | -------- | -------- |
| Addition       | +       | `5 + 3`  | 8        |
| Soustraction   | -       | `5 - 3`  | 2        |
| Multiplication | \*      | `5 * 3`  | 15       |
| Division       | /       | `10 / 2` | 5        |
| Modulo         | %       | `10 % 3` | 1        |

Exemple :
```ruby
a = 10
b = 3
reste = a % b  # reste = 1
```

---

## Saisir des informations
Pour lire une entrée utilisateur, on utilise `gets.chomp` :
```ruby
print "Entrez votre nom : "
nom = gets.chomp

print "Entrez votre âge : "
age = gets.chomp.to_i

puts "Bonjour #{nom}, vous avez #{age} ans."
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
```ruby
if a == b
  puts "a est égal à b"
end
```

---

## Structures conditionnelles
Structure de base :
```ruby
if condition
  # bloc exécuté si vrai
elsif autre_condition
  # autre bloc
else
  # bloc sinon
end
```

Exemple :
```ruby
note = 15
if note >= 10
  puts "Admis"
else
  puts "Échoué"
end
```

---

## Opérateurs logiques
- `&&` : ET logique (`a > 0 && b < 10`)
- `||` : OU logique (`a < 0 || b > 10`)
- `!` : NON logique (`!(a == b)`)

Exemple :
```ruby
if age >= 18 && est_connecte
  puts "Accès autorisé"
end
```

---

## Boucles
### Boucle `for`
```ruby
for i in 0..4
  puts "i = #{i}"
end
```

### Boucle `while`
```ruby
i = 0
while i < 5
  puts "i = #{i}"
  i += 1
end
```

### Boucle `until` (équivalent de do...while)
```ruby
i = 0
until i >= 5
  puts "i = #{i}"
  i += 1
end
```

### Quand utiliser quelle boucle en Ruby
| Type de boucle | Quand l’utiliser                                                                                                    | Exemple de situation                          |
| -------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| `for`          | Quand **le nombre d’itérations est connu à l’avance**                                                               | Afficher les nombres de 1 à 10                |
| `while`        | Quand **on ne connaît pas à l’avance le nombre d’itérations**, mais on veut répéter tant qu’une condition est vraie | Lire un mot de passe tant qu’il est incorrect |
| `until`        | Quand on veut **répéter tant qu’une condition est fausse**                                                          | Répéter jusqu’à atteindre un nombre limite    |

---

## Fonctions (méthodes)
Déclaration d’une méthode simple :
```ruby
def addition(a, b)
  return a + b
end
```

Utilisation :
```ruby
resultat = addition(5, 3)  # resultat = 8
puts resultat
```

---

## Bonnes pratiques Ruby
- Utiliser **snake_case** pour les variables et méthodes : `ma_variable`, `ma_methode`.  
- Utiliser **CamelCase** pour les noms de classes et modules : `MaClasse`.  
- Préférer `#{variable}` (interpolation) plutôt que la concaténation (`"Bonjour " + nom`).  
- Indenter avec **2 espaces** (pas de tabulation).  
- Écrire du code clair et lisible : Ruby favorise la simplicité et l’élégance.  

---

## Structures de base de données
### Tableaux (Array) :
```ruby
fruits = ["Pomme", "Banane"]
puts fruits[0]  # Pomme
fruits << "Orange"
```

### Hash (dictionnaire) :
```ruby
ages = { "Alexer" => 21, "Bob" => 30 }
puts ages["Alexer"]  # 21
```

---

## Case / When (équivalent switch)
```ruby
jour = 3
case jour
when 1
  puts "Lundi"
when 2
  puts "Mardi"
when 3
  puts "Mercredi"
else
  puts "Jour inconnu"
end
```

---

- Types avancés
  - Symbols : objets légers utilisés comme clés dans les Hash
  - Ranges (plages)
  - Nil et Boolean
- Méthodes avancées
  - Paramètres par défaut
  - Arguments variables
  - Retour multiple
- Blocs, Procs et Lambdas
  - Bloc simple
  - Proc
  - Lambda
- Classes et POO
  - Héritage
- Exceptions
- Fichiers
- Modules et namespaces
  - Définition d’un module
  - Inclusion dans une classe
