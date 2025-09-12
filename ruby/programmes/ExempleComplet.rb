# cours_complet.rb
# Résumé des notions principales du cours Ruby

# ---------------------
# Variables et types
# ---------------------
nom = "Alexer"
age = 21
taille = 1.75
est_connecte = true

puts "Nom: #{nom}, Age: #{age}, Taille: #{taille}, Connecté: #{est_connecte}"

# ---------------------
# Opérations
# ---------------------
a, b = 10, 3
puts "Addition: #{a + b}"
puts "Soustraction: #{a - b}"
puts "Multiplication: #{a * b}"
puts "Division: #{a / b}"
puts "Modulo: #{a % b}"

# ---------------------
# Entrées utilisateur
# ---------------------
print "Entrez votre prénom : "
prenom = gets.chomp
print "Entrez votre âge : "
age_utilisateur = gets.chomp.to_i

puts "Bonjour #{prenom}, vous avez #{age_utilisateur} ans."

# ---------------------
# Conditions
# ---------------------
if age >= 18
  puts "Majeur"
else
  puts "Mineur"
end

# ---------------------
# Opérateurs logiques
# ---------------------
if age > 18 && est_connecte
  puts "Accès autorisé"
else
  puts "Accès refusé"
end

# ---------------------
# Boucles
# ---------------------
puts "Boucle for de 1 à 5 :"
for i in 1..5
  puts i
end

puts "Boucle while :"
i = 0
while i < 3
  puts "i = #{i}"
  i += 1
end

# ---------------------
# Méthodes
# ---------------------
def addition(x, y)
  x + y
end

puts "5 + 7 = #{addition(5, 7)}"

# ---------------------
# Tableaux
# ---------------------
fruits = ["Pomme", "Banane", "Orange"]
fruits.each do |fruit|
  puts "Fruit: #{fruit}"
end

# ---------------------
# Hash
# ---------------------
personne = { nom: "Alexer", age: 21, ville: "Paris" }
puts "Nom: #{personne[:nom]}, Âge: #{personne[:age]}"
