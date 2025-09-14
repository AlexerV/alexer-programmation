<?php
// -------------------------
// Variables et constantes
// -------------------------
$nom = "Alexer";
$age = 21;
$taille = 1.73;
$estConnecte = true;

define("PI", 3.14159);

echo "Nom: $nom, Âge: $age, Taille: $taille m\n";
echo "Constante PI: " . PI . "\n\n";

// -------------------------
// Opérations numériques
// -------------------------
$a = 10;
$b = 3;
echo "a + b = " . ($a + $b) . "\n";
echo "a - b = " . ($a - $b) . "\n";
echo "a * b = " . ($a * $b) . "\n";
echo "a / b = " . ($a / $b) . "\n";
echo "a % b = " . ($a % $b) . "\n\n";

// -------------------------
// Entrées utilisateur (CLI)
// -------------------------
echo "Entrez votre prénom : ";
$prenom = trim(fgets(STDIN));
echo "Entrez votre âge : ";
$ageUser = (int)trim(fgets(STDIN));

echo "Bonjour $prenom, vous avez $ageUser ans.\n\n";

// -------------------------
// Conditions et opérateurs logiques
// -------------------------
if ($ageUser >= 18 && $ageUser < 100) {
    echo "Vous êtes majeur.\n";
} elseif ($ageUser >= 100) {
    echo "Vous êtes centenaire !\n";
} else {
    echo "Vous êtes mineur.\n";
}

// -------------------------
// Boucles
// -------------------------
echo "\nBoucle for : ";
for ($i = 1; $i <= 5; $i++) {
    echo "$i ";
}

echo "\nBoucle while : ";
$i = 1;
while ($i <= 3) {
    echo "$i ";
    $i++;
}

echo "\nBoucle do...while : ";
$j = 1;
do {
    echo "$j ";
    $j++;
} while ($j <= 2);

echo "\n\n";

// -------------------------
// Fonctions
// -------------------------
function addition($x, $y) {
    return $x + $y;
}
echo "5 + 7 = " . addition(5, 7) . "\n\n";

// -------------------------
// Tableaux
// -------------------------
$fruits = ["Pomme", "Banane", "Orange"];
echo "Tableau simple (for) : ";
for ($i = 0; $i < count($fruits); $i++) {
    echo $fruits[$i] . " ";
}

echo "\nTableau simple (foreach) : ";
foreach ($fruits as $fruit) {
    echo $fruit . " ";
}

echo "\n\n";

// Tableau associatif
$ages = ["Alexer" => 21, "Bob" => 30];
foreach ($ages as $personne => $ageP) {
    echo "$personne a $ageP ans\n";
}

// -------------------------
// Switch
// -------------------------
$jour = 3;
switch ($jour) {
    case 1: echo "Lundi\n"; break;
    case 2: echo "Mardi\n"; break;
    case 3: echo "Mercredi\n"; break;
    default: echo "Autre jour\n";
}
?>
