# JavaScript

## Extension et exécution
- Extension des fichiers : `.js`
- Exécution possible :
  - Dans un **navigateur** avec une balise `<script>`
  - Dans un **terminal** avec **Node.js** :  
    ```bash
    node fichier.js
    ```

---

## Les bases
- JavaScript est un langage **interprété** et **multi-paradigmes** (impératif, orienté objet, fonctionnel).
  - Interprété : le code est lu et exécuté directement, sans étape de compilation (contrairement à Java ou C).
  - Multi-paradigmes : tu peux programmer en style impératif (instructions), orienté objet (objets, classes), ou fonctionnel (fonctions comme valeurs).
- Afficher un message dans la console :
```js
console.log("Bonjour JavaScript !");
```

---

## Déclaration des variables
- Trois mots-clés principaux :
  - `let` : variable réassignable (recommandé)
  - `const` : constante (ne peut pas être réassignée)
  - `var` : ancienne syntaxe (éviter en général)
Exemple :
```js
let age = 21;
const nom = "Alexer";
var ancienneVariable = "à éviter";
```

---

## Types de données
- `number` : nombres (ex : `5`, `3.14`)
- `string` : chaînes de caractères (ex : `"Hello"`, `'World'`)
- `boolean` : vrai/faux (`true`, `false`)
- `null` : valeur vide
- `undefined` : variable déclarée mais non définie
- `object` : objets, tableaux, etc.
Exemple :
```js
let taille = 1.73;
let estConnecte = true;
let prenom = "Alexer";
```

---

## Opérations numériques
| Opération      | Symbole | Exemple  | Résultat |
| -------------- | ------- | -------- | -------- |
| Addition       | +       | `5 + 3`  | 8        |
| Soustraction   | -       | `5 - 3`  | 2        |
| Multiplication | \*      | `5 * 3`  | 15       |
| Division       | /       | `10 / 2` | 5        |
| Modulo         | %       | `10 % 3` | 1        |

---

## Saisir des informations
Dans un navigateur :
```js
let nom = prompt("Entrez votre nom : ");
alert("Bonjour " + nom);
```

En Node.js (via `readline-sync`) :
```js
const readline = require("readline-sync");

let nom = readline.question("Entrez votre nom : ");
console.log("Bonjour " + nom);
```

---

## Opérateurs de comparaison
| Opérateur | Signification               | Exemple             |
| --------- | --------------------------- | ------------------- |
| `==`      | égal (valeur)               | `5 == "5"` → true   |
| `===`     | égal strict (valeur + type) | `5 === "5"` → false |
| `!=`      | différent (valeur)          | `5 != "5"` → false  |
| `!==`     | différent strict            | `5 !== "5"` → true  |
| `<`       | inférieur à                 | `a < b`             |
| `>`       | supérieur à                 | `a > b`             |
| `<=`      | inférieur ou égal           | `a <= b`            |
| `>=`      | supérieur ou égal           | `a >= b`            |

---

## Conditions
### `If` / `Else`
```js
if (condition) {
    // instruction
} else {
    // instruction
}
```
```js
let note = 15;
if (note >= 10) {
    console.log("Admis");
} else {
    console.log("Échoué");
}
```

### `If` / `Else if` / `Else`
```js
if (condition) {
    // ...
} else if (autreCondition) {
    // ...
} else {
    // ...
}
```

---

## Opérateurs logiques
- `&&` : ET (vrai si toutes les conditions sont vraies)
- `||` : OU (vrai si au moins une est vraie)
- `!` : NON (inverse le résultat (NOT))
Exemple :
```js
if (age >= 18 && estConnecte) {
    console.log("Accès autorisé");
}
```

---

## Boucles
### Boucle `for`
```js
for (let i = 0; i < 5; i++) {
    console.log("i = " + i);
}
```

### Boucle `while`
```js
let i = 0;
while (i < 5) {
    console.log("i = " + i);
    i++;
}
```

### Boucle `do...while`
```js
let i = 0;
do {
    console.log("i = " + i);
    i++;
} while (i < 5);
```

### Boucle `for...of`
```js
let fruits = ["Pomme", "Banane", "Orange"];
for (let fruit of fruits) {
    console.log(fruit);
}
```

### Boucle `for...in`
```js
let personne = { nom: "Alexer", age: 21 };
for (let cle in personne) {
    console.log(cle + " : " + personne[cle]);
}
```

| Boucle       | Quand l’utiliser                                                          |
| ------------ | ------------------------------------------------------------------------- |
| `for`        | Quand tu connais le nombre d’itérations (ex : parcourir de 0 à 10)        |
| `while`      | Quand tu veux répéter **tant qu’une condition est vraie**                 |
| `do...while` | Quand tu veux exécuter **au moins une fois** avant de tester la condition |
| `for...of`   | Pour parcourir facilement les **éléments d’un tableau ou d’une chaîne**   |
| `for...in`   | Pour parcourir les **clés d’un objet**                                    |


---

## Fonctions
### Déclaration classique
```js
function addition(a, b) {
    return a + b;
}
console.log(addition(5, 3));
```

### Fonction fléchée
```js
const multiplication = (a, b) => a * b;
console.log(multiplication(4, 2));
```

- Les fonctions classiques sont adaptées pour déclarer des comportements réutilisables.
- Les fonctions fléchées sont plus courtes et pratiques dans les callbacks (ex: `map`, `filter`).
- Attention : elles n’ont pas leur propre `this`.

---

## Tableaux
```js
let fruits = ["Pomme", "Banane"];
fruits.push("Orange");
console.log(fruits[0]); // Pomme
```

On peux parcourir un tableau de plusieurs manières :
```js
let fruits = ["Pomme", "Banane", "Orange"];

// Boucle classique
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

// Boucle for...of
for (let fruit of fruits) {
    console.log(fruit);
}

// Méthode forEach
fruits.forEach(fruit => console.log(fruit));
```

---

## Objets
```js
let personne = {
    nom: "Alexer",
    age: 21
};
console.log(personne.nom);  // Alexer
```

- Un objet stocke des paires clé → valeur.
- On peut accéder aux valeurs soit avec `personne.nom`, soit avec `personne["nom"]`.
- Les objets sont la base de JavaScript (tout ou presque est un objet).

---

## Switch case
```js
switch (expression) {
    case valeur1:
        // instructions
        break;
    case valeur2:
        // instructions
        break;
    default:
        // si aucune condition ne correspond
}
```
Le `break` est **obligatoire** (sinon ça continue dans les autres `case`).
```js
let jour = 3;
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
```

---

## Manipulation du DOM (navigateur)
```html
<p id="demo">Texte initial</p>
<script>
  document.getElementById("demo").innerText = "Texte modifié avec JavaScript";
</script>
```

- Le DOM est la représentation de la page HTML en mémoire.
- Avec JavaScript, on peut modifier le contenu (`innerText`, `innerHTML`), les styles (`element.style.color`), et même ajouter/supprimer des éléments (`appendChild`, `remove`).
- C’est ce qui permet de rendre les pages interactives.

### DOM avec un fichier `.html` :
- Le JavaScript est directement intégré dans la page (via une balise `<script>`) ou lié avec un fichier externe. Le DOM correspond à la page en cours, et les changements sont visibles dans le navigateur.
Exemple :
```html
<script src="script.js"></script>
```
- Un exemple avec un fichier [HTML](https://github.com/AlexerV/alexer-programmation/tree/main/javascript/programmes/Exemple%20Manipulation%20DOM)

### DOM avec un fichier `.js` (Node.js + jsdom) :
- Le DOM est simulé en mémoire (grâce à `jsdom` ou une autre librairie). Ici, il n’y a pas de page affichée, mais tu peux manipuler du HTML comme si c’était une vraie page, puis afficher le résultat dans la console/terminal.
- Un exemple avec un fichier [Javascript](https://github.com/AlexerV/alexer-programmation/tree/main/javascript/programmes/Exemple%20Node%20%20DOM)

> Avec un fichier `.html`, le DOM correspond à la page affichée dans le navigateur. Avec un fichier `.js` exécuté par Node.js, on peut simuler un DOM (ex. avec *jsdom*) pour manipuler du HTML directement depuis le terminal.
