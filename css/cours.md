# CSS – Feuilles de style en cascade

## Qu’est-ce que le CSS ?
**CSS** signifie *Cascading Style Sheets* (feuilles de style en cascade). Il permet de **gérer la présentation** des pages HTML (couleurs, polices, mise en page…).

HTML structure le contenu, **CSS le met en forme**.

---

## Syntaxe de base CSS

```css
sélecteur {
  propriété: valeur;
}
```

Exemple :
```css
p {
  color: blue;
  font-size: 16px;
}
```

---

## Liaison HTML & CSS
### 1. CSS en ligne (dans les balises HTML)
```html
<p style="color:red;">Texte rouge</p>
```

### 2. CSS interne (dans le `<head>`)
```html
<head>
  <style>
    p { color: blue; }
  </style>
</head>
```

### 3. CSS externe (fichier .css)
```html
<link rel="stylesheet" href="style.css">
```

---

## Sélecteurs CSS
### Sélecteurs de base
| Sélecteur   | Cible                              |
| ----------- | ---------------------------------- |
| `*`         | Tous les éléments                  |
| `p`         | Tous les `<p>`                     |
| `.maClasse` | Élément avec la classe             |
| `#monId`    | Élément avec l’ID                  |
| `div p`     | `<p>` à l’intérieur d’un `<div>`   |
| `ul > li`   | `<li>` enfants directs d’un `<ul>` |

### Groupes
```css
h1, h2, h3 {
  color: darkblue;
}
```

---

## Sélecteurs avancés
### Sélecteurs d’attributs
```css
input[type="text"] {
  border: 1px solid gray;
}
```
> Permet de cibler les éléments selon leurs attributs (type, name, etc.).

### Sélecteurs de pseudo-classes avancés
```css
li:first-child { font-weight: bold; }
li:last-child { color: red; }
li:nth-child(2n) { background-color: #f0f0f0; }  /* tous les éléments pairs */
```

### Combinateurs
- `E F` : descendant
- `E > F` : enfant direct
- `E + F` : frère immédiat
- `E ~ F` : frère général

---

## Couleurs et unités
### Unités CSS utiles
- `px` : pixels (fixe)
- `%` : pourcentage de l’élément parent
- `em` : relatif à la taille de police de l’élément
- `rem` : relatif à la taille de police de l’élément racine (`html`)
- `vh`, `vw` : pourcentage de la hauteur/largeur de la fenêtre
> Exemple : `font-size: 2rem;` → 2 fois la taille de police racine.

### Dégradés
```css
background: linear-gradient(to right, red, yellow);
background: radial-gradient(circle, blue, lightblue);
```

---

## Texte avancé
### Casser les mots :
```css
word-wrap: break-word;
overflow-wrap: break-word;
```

### Ombrage du texte :
```css
text-shadow: 2px 2px 5px gray;
```

### Police personnalisée :
```css
@font-face {
  font-family: 'MaPolice';
  src: url('maPolice.ttf');
}
p { font-family: 'MaPolice', sans-serif; }
```

---

## Box model et display
### Boîte flexible
```css
box-sizing: border-box;
```
> Inclut padding et border dans la largeur totale, pratique pour les layouts modernes.

### Display
- `inline` : ne prend que l’espace nécessaire
- `block` : prend toute la largeur disponible
- `inline-block` : inline mais avec hauteur/largeur personnalisables
- `none` : cache l’élément

---

## Positionnement avancé
### Z-index : contrôle l’empilement
```css
div { position: absolute; z-index: 10; }
```

### Sticky : position collante
```css
header { position: sticky; top: 0; }
```
> L’élément reste visible jusqu’à ce que son conteneur soit hors de la vue.

---

## Flexbox complémentaire
### Alignement
```css
flex-wrap: wrap;             /* retour à la ligne si nécessaire */
align-content: space-between; /* alignement multi-lignes */
```

### Ordre
```css
.item1 { order: 2; }
.item2 { order: 1; }
```
> Permet de réorganiser les éléments sans changer le HTML.

---

## Grid complémentaire
### Zones nommées
```css
.grid-container {
  display: grid;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
}
.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.footer { grid-area: footer; }
```

### Répartition flexible
```css
grid-template-columns: repeat(3, 1fr); /* 3 colonnes égales */
grid-template-rows: auto 200px auto;
```

---

## Transitions et animations avancées
### Transitions multiples
```css
button {
  transition: background-color 0.3s ease, transform 0.3s ease;
}
```

### Animation infinie
```css
@keyframes rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
.logo { animation: rotate 2s linear infinite; }
```

---

## Responsive design avancé
### Media Queries pour orientation
```css
@media (orientation: portrait) {
  body { background-color: lightpink; }
}
```

### Breakpoints courants
```css
/* smartphone */
@media (max-width: 480px) { ... }
/* tablette */
@media (max-width: 768px) { ... }
/* desktop */
@media (min-width: 1024px) { ... }
```

### Unités relatives
```css
width: 80vw;   /* 80% de la largeur de la fenêtre */
font-size: 2rem;
```

---

## Propriétés de base
### Couleurs
```css
color: red;
background-color: lightgray;
```

- Couleurs nommées : `red`, `blue`, `black`

- Hexadécimal : `#ff0000`

- RGB : `rgb(255, 0, 0)`

- RGBA : `rgba(255, 0, 0, 0.5)` (avec transparence)

### Qu’est-ce que RGB ?
RGB signifie **Red**, **Green**, **Blue** (Rouge, Vert, Bleu).
C’est un modèle de couleur **additif**, utilisé pour afficher des couleurs sur les écrans (moniteurs, téléphones, télévisions, etc.).
- Chaque couleur est définie par 3 valeurs numériques : `rgb(R, G, B)` où :
  - **R** (Red) : intensité du rouge (entre 0 et 255)
  - **G** (Green) : intensité du vert (entre 0 et 255)
  - **B** (Blue) : intensité du bleu (entre 0 et 255)

Exemple :
```css
color: rgb(255, 0, 0);   /* Rouge pur */
color: rgb(0, 255, 0);   /* Vert pur */
color: rgb(0, 0, 255);   /* Bleu pur */
color: rgb(128, 128, 128); /* Gris moyen */
```

### Qu’est-ce que RGBA ?
**RGBA** est une extension de **RGB**, qui ajoute un **canal alpha** (transparence).
- Syntaxe : `rgba(R, G, B, A)`

- A = alpha = opacité :
  - `1` = complètement opaque
  - `0` = complètement transparent
  - Valeur intermédiaire = semi-transparent (ex: `0.5` pour 50%)

Exemple :
```css
background-color: rgba(255, 0, 0, 0.5); /* Rouge semi-transparent */
```

### Tableau récapitulatif des couleurs CSS
| Couleur        | Nom CSS     | Code HEX  | Code RGB             | Définition rapide                                             |
| -------------- | ----------- | --------- | -------------------- | ------------------------------------------------------------- |
| 🔴             | `red`       | `#FF0000` | `rgb(255, 0, 0)`     | Rouge vif, couleur forte, utilisée pour attirer l’attention   |
| 🟠             | `orange`    | `#FFA500` | `rgb(255, 165, 0)`   | Couleur chaude, souvent associée à l’énergie et la créativité |
| 🟡             | `yellow`    | `#FFFF00` | `rgb(255, 255, 0)`   | Jaune pur, synonyme de lumière, chaleur et alerte             |
| 🟢             | `green`     | `#008000` | `rgb(0, 128, 0)`     | Vert classique, associé à la nature, la croissance            |
| 🔵             | `blue`      | `#0000FF` | `rgb(0, 0, 255)`     | Bleu intense, souvent utilisé pour la confiance et le calme   |
| 🟣             | `purple`    | `#800080` | `rgb(128, 0, 128)`   | Couleur royale, mystique ou créative                          |
| ⚫              | `black`     | `#000000` | `rgb(0, 0, 0)`       | Noir absolu, pour contrastes, textes ou fonds                 |
| ⚪              | `white`     | `#FFFFFF` | `rgb(255, 255, 255)` | Blanc pur, utilisé pour les fonds et le minimalisme           |
| ⚪ (gris clair) | `lightgray` | `#D3D3D3` | `rgb(211, 211, 211)` | Gris doux, utilisé comme couleur d’arrière-plan ou neutre     |
| ⚫ (gris foncé) | `darkgray`  | `#A9A9A9` | `rgb(169, 169, 169)` | Gris foncé, pour contraste plus marqué                        |
| 🟥             | `crimson`   | `#DC143C` | `rgb(220, 20, 60)`   | Rouge profond avec une touche de rose, élégant et moderne     |
| 🟩             | `lime`      | `#00FF00` | `rgb(0, 255, 0)`     | Vert fluo, utilisé pour des effets flashy                     |
| 🟦             | `skyblue`   | `#87CEEB` | `rgb(135, 206, 235)` | Bleu clair, très agréable pour des designs doux ou aérés      |
| 🟪             | `violet`    | `#EE82EE` | `rgb(238, 130, 238)` | Violet clair, frais, utilisé dans les interfaces modernes     |
| 🧡             | `coral`     | `#FF7F50` | `rgb(255, 127, 80)`  | Orange rosé, doux et chaleureux                               |
| 🌸             | `pink`      | `#FFC0CB` | `rgb(255, 192, 203)` | Rose clair, souvent utilisé dans des designs doux ou féminins |
| 🌌             | `navy`      | `#000080` | `rgb(0, 0, 128)`     | Bleu marine, profond et sérieux                               |
| 🧊             | `aqua`      | `#00FFFF` | `rgb(0, 255, 255)`   | Cyan, frais et moderne                                        |
| 🌿             | `olive`     | `#808000` | `rgb(128, 128, 0)`   | Vert terne, naturel et discret                                |
| 🌫️            | `silver`    | `#C0C0C0` | `rgb(192, 192, 192)` | Gris métallique, pour des effets sobres                       |



### Texte
```css
font-family: Arial, sans-serif;
font-size: 16px;
font-weight: bold;
text-align: center;
text-decoration: underline;
line-height: 1.5;
```

### Bordures
```css
border: 2px solid black;
border-radius: 10px;
```

### Marges et padding
```css
margin: 20px;       /* marge extérieure */
padding: 10px;      /* marge intérieure */
```
Raccourcis :
```css
margin: 10px 20px;  /* haut/bas, gauche/droite */
```

### Dimensions
```css
width: 200px;
height: 100px;
max-width: 100%;
```

---

## Le modèle de boîte (Box Model)
- `content` : contenu

- `padding` : espace intérieur

- `border` : bordure

- `margin` : espace extérieur

---

## Classes, ID et héritage
### Classe (réutilisable)
```css
.important {
  color: red;
}
```

### ID (unique)
```css
#en-tete {
  font-size: 24px;
}
```

### Héritage
Certaines propriétés comme `color` ou `font` sont héritées par les enfants.

---

## Positionnement
### Position statique (par défaut)
```css
position: static;
```

### Relative
```css
position: relative;
top: 10px;
left: 20px;
```

### Absolute
```css
position: absolute;
top: 0;
left: 0;
```

### Fixed
```css
position: fixed;
bottom: 10px;
right: 10px;
```

---

## Flexbox
Pour des mises en page flexibles et modernes.

### Conteneur :
```css
display: flex;
flex-direction: row;      /* ou column */
justify-content: center;  /* centrage horizontal */
align-items: center;      /* centrage vertical */
gap: 10px;
```

### Éléments enfants :
```css
flex: 1;
```

---

## Grid (Grille CSS)
Permet de créer des mises en page en colonnes/lignes.
```display: grid;
grid-template-columns: 1fr 1fr 1fr;
gap: 20px;
```

---

## Images et arrière-plans
```css
background-image: url("image.jpg");
background-size: cover;
background-repeat: no-repeat;
background-position: center;
```

---

## Pseudo-classes
```css
a:hover {
  color: red;
}
input:focus {
  border-color: blue;
}
```

---

## Pseudo-éléments
```css
p::first-line {
  font-weight: bold;
}
div::before {
  content: "💡 ";
}
```

## Animation et transitions
### Transition :
```css
button {
  transition: background-color 0.3s ease;
}
button:hover {
  background-color: green;
}
```

### Animation :
```css
@keyframes slidein {
  from { transform: translateX(-100px); }
  to   { transform: translateX(0); }
}

.element {
  animation: slidein 1s forwards;
}
```

---

## Responsive Design (design adaptatif)
### Media Queries
```css
@media screen and (max-width: 768px) {
  body {
    background-color: lightblue;
  }
}
```

---

## Organisation des fichiers CSS
### Exemple de structure :
```bash
/css
  ├─ reset.css
  ├─ base.css
  ├─ layout.css
  ├─ components.css
  └─ style.css
```

---

## Bonnes pratiques CSS
- Utilise des **classes** plutôt que des **IDs** pour le style

- Ne mélange pas HTML et CSS (évite les `style=""`)

- Préfère les **fichiers CSS externes**

- Organise tes styles avec des commentaires

- Utilise un reset CSS pour un rendu cohérent
