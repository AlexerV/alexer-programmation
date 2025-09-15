use std::io;
use std::collections::HashMap;

#[tokio::main]
async fn main() {
    println!("=== Rust Cours Complet ===");

    // Variables et mutabilité
    let mut nom = String::new();
    println!("Entrez votre nom :");
    io::stdin().read_line(&mut nom).expect("Erreur lecture");
    let nom = nom.trim(); // supprimer le retour à la ligne

    let age: u32 = loop {
        let mut input = String::new();
        println!("Entrez votre âge :");
        io::stdin().read_line(&mut input).expect("Erreur lecture");
        match input.trim().parse() {
            Ok(num) => break num,
            Err(_) => println!("Veuillez entrer un nombre valide !"),
        }
    };

    println!("Bonjour {}, vous avez {} ans.", nom, age);

    // Conditions et opérateurs logiques
    if age >= 18 && age < 100 {
        println!("Vous êtes majeur !");
    } else if age >= 100 {
        println!("Vous êtes très âgé !");
    } else {
        println!("Vous êtes mineur !");
    }

    // Boucles
    println!("Boucle for de 1 à 5 :");
    for i in 1..=5 {
        println!("{}", i);
    }

    println!("Boucle while : compteur jusqu'à 3");
    let mut compteur = 0;
    while compteur < 3 {
        println!("Compteur = {}", compteur);
        compteur += 1;
    }

    println!("Boucle loop (interrompue après 2 tours) :");
    let mut compteur2 = 0;
    loop {
        println!("Compteur2 = {}", compteur2);
        compteur2 += 1;
        if compteur2 >= 2 { break; }
    }

    // Fonctions
    let resultat = addition(5, 7);
    println!("5 + 7 = {}", resultat);

    // Tableaux et vecteurs
    let fruits = ["Pomme", "Banane", "Cerise"];
    println!("Premier fruit : {}", fruits[0]);

    let mut nombres = vec![10, 20, 30];
    nombres.push(40);
    println!("Vecteur : {:?}", nombres);

    // HashMap
    let mut ages = HashMap::new();
    ages.insert("Alexer", 21);
    ages.insert("Bob", 30);
    println!("Age d'Alexer : {}", ages["Alexer"]);

    // Struct et Enum
    let pers = Personne { nom: String::from("Alexer"), age: 21 };
    println!("Personne : {} a {} ans", pers.nom, pers.age);

    let couleur = Couleur::Rouge;
    match couleur {
        Couleur::Rouge => println!("Rouge"),
        Couleur::Vert => println!("Vert"),
        Couleur::Bleu => println!("Bleu"),
    }

    // Gestion d'erreur simple
    let division = diviser(10.0, 2.0);
    match division {
        Ok(val) => println!("10 / 2 = {}", val),
        Err(e) => println!("Erreur : {}", e),
    }

    // Async simple
    mon_async().await;
}

fn addition(a: i32, b: i32) -> i32 {
    a + b
}

struct Personne {
    nom: String,
    age: u32,
}

enum Couleur {
    Rouge,
    Vert,
    Bleu,
}

fn diviser(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err(String::from("Division par zéro"))
    } else {
        Ok(a / b)
    }
}

// Exemple Async
async fn mon_async() {
    println!("Exécution d'une fonction async !");
}
