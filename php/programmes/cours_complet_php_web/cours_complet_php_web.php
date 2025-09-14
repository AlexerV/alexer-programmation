<?php
// Traitement du formulaire
$resultat = "";
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $prenom = $_POST["prenom"] ?? "Inconnu";
    $age = (int)($_POST["age"] ?? 0);

    if ($age >= 18) {
        $resultat = "Bonjour $prenom, vous êtes majeur.";
    } else {
        $resultat = "Bonjour $prenom, vous êtes mineur.";
    }
}
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Cours Complet PHP</title>
</head>
<body>
    <h1>Bienvenue dans le cours complet PHP</h1>

    <!-- Variables et constantes -->
    <h2>Variables et constantes</h2>
    <?php
    $nom = "Alexer";
    define("PI", 3.14);
    echo "Nom : $nom<br>";
    echo "Constante PI : " . PI . "<br>";
    ?>

    <!-- Formulaire (entrées utilisateur POST) -->
    <h2>Formulaire</h2>
    <form method="post">
        Prénom: <input type="text" name="prenom"><br>
        Âge: <input type="number" name="age"><br>
        <input type="submit" value="Envoyer">
    </form>
    <p><?php echo $resultat; ?></p>

    <!-- Boucles -->
    <h2>Boucles</h2>
    <?php
    echo "Boucle for : ";
    for ($i = 1; $i <= 5; $i++) {
        echo "$i ";
    }
    ?>

    <!-- Tableaux -->
    <h2>Tableaux</h2>
    <?php
    $fruits = ["Pomme", "Banane", "Orange"];
    echo "Tableau simple : ";
    foreach ($fruits as $fruit) {
        echo "$fruit ";
    }
    ?>

    <!-- Switch -->
    <h2>Switch</h2>
    <?php
    $jour = 2;
    switch ($jour) {
        case 1: echo "Lundi"; break;
        case 2: echo "Mardi"; break;
        case 3: echo "Mercredi"; break;
        default: echo "Autre jour";
    }
    ?>
</body>
</html>
