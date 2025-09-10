// dom-node.js
// Exemple d'utilisation de jsdom pour manipuler le DOM avec Node.js

// Installer la dépendance avant :
// npm install jsdom

const { JSDOM } = require("jsdom");

// ======================
// Créons une page HTML virtuelle
// ======================
const dom = new JSDOM(`
<!DOCTYPE html>
<html>
  <body>
    <h1 id="titre">Titre initial</h1>
    <div id="contenu"></div>
  </body>
</html>
`);

// On récupère le "document" comme dans un navigateur
const document = dom.window.document;

// ======================
// Manipulation du DOM
// ======================

// Modifier un texte
const titre = document.getElementById("titre");
titre.textContent = "Titre modifié avec jsdom 🎉";

// Ajouter un élément
const nouveauParagraphe = document.createElement("p");
nouveauParagraphe.textContent = "Paragraphe ajouté dynamiquement ✔️";
document.getElementById("contenu").appendChild(nouveauParagraphe);

// ======================
// Afficher le HTML final
// ======================
console.log(document.body.innerHTML);
