#!/bin/bash
# Script démonstratif Bash

echo "=== 🚀 Démo Bash / Shell ==="

# ----------------------------
# Variables
# ----------------------------
var1="Alexer"
var2=42
echo "Bonjour, $var1 !"
echo "Le nombre magique est $var2"

# ----------------------------
# Lecture utilisateur
# ----------------------------
echo -n "Quel est ton prénom ? "
read prenom
echo "Enchanté, $prenom 👋"

# ----------------------------
# Opérations arithmétiques
# ----------------------------
a=5
b=3
somme=$(expr $a + $b)
echo "$a + $b = $somme"

# ----------------------------
# Conditions
# ----------------------------
echo -n "Quel âge as-tu ? "
read age
if [ "$age" -ge 18 ]; then
    echo "Tu es majeur ✅"
else
    echo "Tu es mineur ❌"
fi

# ----------------------------
# Boucles
# ----------------------------
echo "Compteur avec for :"
for i in {1..5}; do
    echo "Itération $i"
done

echo "Compteur avec while :"
i=1
while [ $i -le 3 ]; do
    echo "Tour $i"
    i=$(expr $i + 1)
done

# ----------------------------
# Sélecteur case
# ----------------------------
echo "Choisis ton langage préféré :"
echo "1- Bash  2- Python  3- JavaScript"
read choix
case $choix in
    1) echo "🔥 Tu aimes le Shell !" ;;
    2) echo "🐍 Tu aimes Python !" ;;
    3) echo "✨ Tu aimes JavaScript !" ;;
    *) echo "Langage inconnu 🤷" ;;
esac

# ----------------------------
# Fonctions
# ----------------------------
multiplier() {
    resultat=$(expr $1 \* $2)
    echo "$1 x $2 = $resultat"
}
echo "Exemple de fonction :"
multiplier 6 7

# ----------------------------
# Tests fichiers
# ----------------------------
echo "Vérification d'un fichier fictif..."
if [ -f "demo.sh" ]; then
    echo "demo.sh existe ✔️"
else
    echo "demo.sh est introuvable ❌"
fi

# ----------------------------
# Redirections
# ----------------------------
echo "Hello fichier !" > sortie.txt
echo "Un texte ajouté" >> sortie.txt
echo "Contenu du fichier sortie.txt :"
cat sortie.txt

# ----------------------------
# Donner les droits d'exécution au fichier : sudo chmod +x demo.sh
# Exécuter le fichier : ./demo.sh
# ----------------------------
