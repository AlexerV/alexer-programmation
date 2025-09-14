# PHP

## Extension des fichiers et exécution
- Les fichiers PHP se terminent par `.php`.
- PHP est un langage interprété côté serveur, principalement utilisé pour le développement web.

Pour exécuter un script PHP :
1. Installe [PHP](https://www.php.net/downloads) sur ton système.
2. Vérifie l’installation avec :
```bash
php -v
```
3. Crée un fichier `index.php` :
```php
<?php
echo "Bonjour PHP !";
?>
```
4. Exécute-le dans le terminal :
```bash
php index.php
```
⚡ Tu peux aussi lancer un petit serveur local (pratique pour tester du code web) :
```bash
php -S localhost:8000
```
Puis ouvre [http://localhost:8000](http://localhost:8000/) dans ton navigateur.

---

## Les bases
- Chaque instruction se termine par `;`.
- Le code PHP est écrit entre balises :
```php
<?php
// code ici
?>
```
Exemple minimal :
```php
<?php
echo "Hello World!";
?>
```

---

## Variables et types
En PHP, toutes les variables commencent par `$`.  
Types courants :
- `int` → entier
- `float` → nombre décimal
- `string` → chaîne de caractères
- `bool` → booléen (`true`/`false`)
- `array` → tableau
- `object` → objet
Exemple :
```php
<?php
$nom = "Alexer";
$age = 21;
$taille = 1.73;
$estConnecte = true;

echo "Nom: $nom, Age: $age, Taille: $taille, Connecté: $estConnecte";
?>
```

---

## Constantes
Une constante est une valeur qui ne change pas durant l’exécution.

### Déclaration
```php
<?php
define("PI", 3.14);
const SITE_NAME = "Alexer Programmation";

echo PI;          // 3.14
echo SITE_NAME;   // Alexer Programmation
?>
```
> ⚠️ Par convention, les constantes s’écrivent en MAJUSCULES.

---

## Opérations
| Opération      | Symbole | Exemple   |
| -------------- | ------- | --------- |
| Addition       | +       | `$a + $b` |
| Soustraction   | -       | `$a - $b` |
| Multiplication | \*      | `$a * $b` |
| Division       | /       | `$a / $b` |
| Modulo         | %       | `$a % $b` |

---

## Chaînes de caractères (String)

En PHP, on peut manipuler des chaînes avec différents opérateurs et fonctions.

### Concaténation
On utilise le `.` pour coller des chaînes :  
```php
<?php
$prenom = "Alexer";
$nom = "Dev";
echo $prenom . " " . $nom;  // Alexer Dev
?>
```

### Interpolation
Avec des guillemets doubles (`"`), on peut insérer des variables directement :
```php
<?php
$age = 21;
echo "J'ai $age ans";  // J'ai 21 ans
?>
```

### Fonctions utiles
```php
<?php
$texte = "Bonjour";
echo strlen($texte);     // Longueur = 7
echo strtolower($texte); // "bonjour"
echo strtoupper($texte); // "BONJOUR"
echo substr($texte, 0, 3); // "Bon"
?>
```

---

## Entrées utilisateur
### Depuis le terminal
```php
<?php
echo "Entrez votre nom : ";
$nom = trim(fgets(STDIN));

echo "Bonjour $nom !";
?>
```
> ⚠️ Dans un contexte web, les entrées viennent des formulaires (`$_GET`, `$_POST`).

### Entrées via formulaire web
Exemple avec $_GET (URL : index.php?nom=Alexer)
```php
<?php
if (isset($_GET["nom"])) {
    $nom = $_GET["nom"];
    echo "Bonjour $nom (via GET)";
}
?>
```

Exemple avec $_POST (formulaire HTML)
```php
<form method="POST" action="">
    <input type="text" name="nom" placeholder="Votre nom">
    <button type="submit">Envoyer</button>
</form>

<?php
if (isset($_POST["nom"])) {
    $nom = $_POST["nom"];
    echo "Bonjour $nom (via POST)";
}
?>
```

---

## Conditions
### Syntaxe générale
```php
if (condition) {
    // instructions
} elseif (autre_condition) {
    // instructions si autre_condition vraie
} else {
    // instructions sinon
}
```
Exemple :
```php
<?php
$note = 15;

if ($note >= 16) {
    echo "Très bien";
} elseif ($note >= 10) {
    echo "Admis";
} else {
    echo "Échoué";
}
?>
```

---

## Opérateurs logiques
- `&&` → ET
- `||` → OU
- `!` → NO

### Exemple combiné
```php
<?php
$a = 5;
$b = 10;

if ($a > 0 && $b > 0) {
    echo "Les deux nombres sont positifs\n";
}

if ($a < 0 || $b < 0) {
    echo "Au moins un nombre est négatif\n";
}

if (!($a == $b)) {
    echo "$a est différent de $b\n";
}
?>
```

---

## Boucles
### Boucle `for`
```php
for ($i = 0; $i < 5; $i++) {
    echo "i = $i\n";
}
```

### Boucle `while`
```php
$i = 0;
while ($i < 5) {
    echo "i = $i\n";
    $i++;
}
```

### Boucle `do...while`
```php
$i = 0;
do {
    echo "i = $i\n";
    $i++;
} while ($i < 5);
```

### Quand utiliser quelle boucle en PHP
| Type de boucle | Quand l’utiliser                                                                                   | Exemple                                    |
|----------------|----------------------------------------------------------------------------------------------------|--------------------------------------------|
| `for`          | Quand on connaît le nombre exact d’itérations                                                      | Afficher les nombres de 1 à 10             |
| `while`        | Quand on répète tant qu’une condition est vraie (sans connaître le nombre d’itérations à l’avance) | Lire un mot de passe jusqu’à ce qu’il soit bon |
| `do...while`   | Quand on veut exécuter le bloc **au moins une fois**, puis répéter tant qu’une condition est vraie | Afficher un menu au moins une fois         |
| `foreach`      | Quand on veut parcourir facilement un tableau ou un tableau associatif                             | Lire tous les éléments d’un tableau        |


---

## Fonctions
```php
<?php
function addition($a, $b) {
    return $a + $b;
}

echo addition(5, 3); // 8
?>
```

---

## Inclusion de fichiers
PHP permet de séparer le code en plusieurs fichiers.

### `Include` et `Require`
```php
<?php
include "header.php";   // inclut le fichier mais continue si erreur
require "config.php";   // inclut le fichier et arrête si erreur
?>
```

### Variante avec `_once`
```php
<?php
include_once "header.php";  // inclut une seule fois
require_once "config.php";
?>
```
> 💡 Très utile dans les projets web pour séparer l’affichage (HTML) de la logique (PHP).

---

## Tableaux
### Numériques
```php
$fruits = ["Pomme", "Banane", "Orange"];
echo $fruits[0]; // Pomme
```

### Associatifs
```php
$personne = [
    "nom" => "Alexer",
    "age" => 21,
    "ville" => "Paris"
];
echo $personne["nom"]; // Alexer
```

### Parcourir un tableau
```php
<?php
$fruits = ["Pomme", "Banane", "Orange"];

# Avec for
for ($i = 0; $i < count($fruits); $i++) {
    echo $fruits[$i] . "\n";
}

# Avec foreach (plus simple)
foreach ($fruits as $fruit) {
    echo $fruit . "\n";
}

# Avec clés + valeurs
foreach ($fruits as $index => $fruit) {
    echo "Index $index : $fruit\n";
}
?>
```

---

## Switch
```php
$jour = 3;
switch ($jour) {
    case 1:
        echo "Lundi";
        break;
    case 2:
        echo "Mardi";
        break;
    case 3:
        echo "Mercredi";
        break;
    default:
        echo "Jour inconnu";
}
```

---

## Bonnes pratiques PHP
- Toujours fermer les ressources ouvertes (fichiers, connexions).  
- Indiquer l’encodage si vous générez du HTML :  
  ```php
  header("Content-Type: text/html; charset=UTF-8");
  ```
- Utiliser `===` plutôt que `==` pour éviter les comparaisons imprécises (égalité stricte).
- Organiser son code en plusieurs fichiers (`include`, `require`).
- Commenter son code (`//` ou `/* ... */`) pour améliorer la lisibilité.
