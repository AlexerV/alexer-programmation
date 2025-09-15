# 🦀 Rust – Cours

[![GitHub](https://img.shields.io/badge/GitHub-AlexerV-181717?logo=github)](https://github.com/AlexerV)<br>
![Discord](https://img.shields.io/badge/Discord-.alexer-5865F2?logo=discord&logoColor=white)

Bienvenue dans la section **Rust** du dépôt !  
Tu trouveras ici un cours progressif pour apprendre les bases du langage Rust, avec exemples, explications et bonnes pratiques.

---

## 📁 À propos de Rust

Rust est un **langage de programmation compilé, moderne et sécurisé en mémoire**.  
Il est conçu pour éviter les erreurs courantes (segfaults, data races) tout en offrant des performances comparables au C/C++.  
Il est très utilisé pour :  
- le développement système  
- les applications WebAssembly  
- les serveurs hautes performances  
- les projets embarqués  

---

## 🚀 Lancer un programme Rust

### 🔹 Extension
Les fichiers Rust se terminent par `.rs`.

### 🔹 Compilation et exécution avec `rustc`

#### Windows / Linux / macOS :

```bash
# Compilation
rustc main.rs

# Exécution
./main   # ou main.exe sur Windows
```

### 🔹 Compilation et exécution avec Cargo (recommandé)
Cargo est le **gestionnaire de projet et de dépendances** de Rust.

```bash
# Créer un projet
cargo new mon_projet
cd mon_projet

# Compiler
cargo build

# Exécuter
cargo run
```
> ⚠️ Utilise toujours Cargo dès que tu travailles avec plusieurs fichiers ou des dépendances externes (ex : Tokio, Serde).

---

## 📚 Ce que tu vas apprendre
- ✅ Les bases de Rust
- ✅ Déclaration des variables et mutabilité
- ✅ Types de base (entiers, flottants, booléens, chaînes, etc.)
- ✅ Opérations numériques
- ✅ Entrées utilisateur (`std::io`)
- ✅ Opérateurs de comparaison
- ✅ Conditions (`if` / `else`)
- ✅ Opérateurs logiques
- ✅ Boucles (`for` / `while` / `loop`)
- ✅ Fonctions
- ✅ Tableaux, Vecteurs et HashMap
- ✅ Structures (`struct`) et Enums
- ✅ Gestion des erreurs (`Result`, `Option`, `match`)
- ✅ Emprunts et ownership
- ✅ Modules et organisation du code
- ✅ Programmation asynchrone (`async`/`await` avec Tokio ou `async-std`)
- ✅ Exemple complet de projet Rust avec Cargo

---

## 📌 Prérequis
- Avoir Rust et Cargo installés
- Vérifier avec :
```bash
rustc --version
cargo --version
```
- Utiliser un éditeur adapté avec support de Rust (ex : VS Code avec l’extension rust-analyzer)
