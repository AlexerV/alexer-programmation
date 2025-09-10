# =============================
# Démo Python – Toutes notions
# =============================
print("=== 🚀 Démo Python ===\n")

# -----------------------------
# Variables et affichage
# -----------------------------
prenom = "Alexer"
age = 21
print(f"Bonjour {prenom}, tu as {age} ans\n")

# -----------------------------
# Saisie utilisateur
# -----------------------------
nom_utilisateur = input("Quel est ton nom ? ")
print(f"Enchanté, {nom_utilisateur} !\n")

# -----------------------------
# Opérations arithmétiques
# -----------------------------
a = 10
b = 3
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} % {b} = {a%b}")
print(f"{a} ** {b} = {a**b}")
print(f"{a} // {b} = {a//b}\n")

# -----------------------------
# Conditions
# -----------------------------
x = int(input("Entrez un nombre pour tester les conditions : "))
if x > 0:
    print(f"{x} est positif")
elif x < 0:
    print(f"{x} est négatif")
else:
    print(f"{x} est nul")

# Opérateurs logiques
y = int(input("Entrez un autre nombre : "))
if x > 0 and y > 0:
    print("Les deux nombres sont positifs")
if x > 0 or y > 0:
    print("Au moins un des nombres est positif")
if not (x > 0):
    print("x n'est pas positif")
print()

# -----------------------------
# Boucles
# -----------------------------
print("Boucle for sur range(3) :")
for i in range(3):
    print(i)

print("\nBoucle while :")
i = 0
while i < 3:
    print(i)
    i += 1
print()

# -----------------------------
# Fonctions
# -----------------------------
def dire_bonjour(nom):
    print(f"Bonjour {nom} !")

def addition(a, b):
    return a + b

dire_bonjour(nom_utilisateur)
print(f"2 + 3 = {addition(2,3)}\n")

# -----------------------------
# Listes
# -----------------------------
fruits = ["pomme", "banane", "cerise"]
print("Liste de fruits :", fruits)
for fruit in fruits:
    print(fruit)

# -----------------------------
# Dictionnaires
# -----------------------------
personne = {"nom": "Alexer", "age": 21}
print("\nDictionnaire personne :", personne)
print("Nom :", personne["nom"], "| Age :", personne["age"])
print()

# -----------------------------
# Match / Case (Python 3.10+)
# -----------------------------
lang = input("Quel langage veux-tu apprendre ? ")
match lang:
    case "Python":
        print("Tu peux devenir Data Scientist.")
    case "JavaScript":
        print("Tu peux devenir développeur web.")
    case "Java":
        print("Tu peux développer des applications mobiles.")
    case "PHP":
        print("Tu peux développer côté serveur.")
    case "Solidity":
        print("Tu peux développer pour la blockchain.")
    case _:
        print("Peu importe le langage, l'important c'est de coder !")
