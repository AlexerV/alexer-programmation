// main.js
// Exemple global pour réviser les bases de JavaScript

// ======================
// Variables et types
// ======================
let age = 21;
const nom = "Alexer";
let estConnecte = true;
let taille = 1.75;

console.log("Nom :", nom);
console.log("Âge :", age);
console.log("Connecté ?", estConnecte);
console.log("Taille :", taille);

// ======================
// Opérations numériques
// ======================
let a = 10;
let b = 3;
console.log("Addition :", a + b);
console.log("Soustraction :", a - b);
console.log("Multiplication :", a * b);
console.log("Division :", a / b);
console.log("Modulo :", a % b);

// ======================
// Conditions et opérateurs logiques
// ======================
if (age >= 18 && estConnecte) {
    console.log("Accès autorisé");
} else if (age >= 18 && !estConnecte) {
    console.log("Tu dois être connecté !");
} else {
    console.log("Accès refusé, tu es mineur.");
}

// ======================
// Boucles
// ======================
// Boucle for
for (let i = 0; i < 3; i++) {
    console.log("for → i =", i);
}

// Boucle while
let i = 0;
while (i < 3) {
    console.log("while → i =", i);
    i++;
}

// Boucle do...while
let j = 0;
do {
    console.log("do...while → j =", j);
    j++;
} while (j < 3);

// ======================
// Tableaux
// ======================
let fruits = ["Pomme", "Banane", "Orange"];
console.log("Premier fruit :", fruits[0]);

// Parcourir avec for...of
for (let fruit of fruits) {
    console.log("for...of →", fruit);
}

// forEach
fruits.forEach(fruit => console.log("forEach →", fruit));

// ======================
// Objets
// ======================
let personne = {
    nom: "Alexer",
    age: 21,
    estAdmin: false
};
console.log("Objet :", personne);
console.log("Nom :", personne.nom);
console.log("Âge :", personne["age"]);

// Boucle for...in
for (let cle in personne) {
    console.log(cle, ":", personne[cle]);
}

// ======================
// Fonctions
// ======================
// Fonction classique
function addition(x, y) {
    return x + y;
}
console.log("Addition (fonction) :", addition(5, 7));

// Fonction fléchée
const multiplication = (x, y) => x * y;
console.log("Multiplication (fléchée) :", multiplication(4, 6));

// ======================
// Switch case
// ======================
let jour = 2;
switch (jour) {
    case 1:
        console.log("Lundi");
        break;
    case 2:
        console.log("Mardi");
        break;
    case 3:
        console.log("Mercredi");
        break;
    default:
        console.log("Jour inconnu");
}

// ======================
// Manipulation de chaîne
// ======================
let message = "Bonjour " + nom + " !";
console.log(message);
console.log("Longueur du message :", message.length);
console.log("En majuscules :", message.toUpperCase());
