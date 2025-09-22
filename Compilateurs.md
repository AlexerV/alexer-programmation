# 🛠️ Installation des compilateurs sur Linux

[![GitHub](https://img.shields.io/badge/GitHub-AlexerV-181717?logo=github)](https://github.com/AlexerV)
![Discord](https://img.shields.io/badge/Discord-.alexer-5865F2?logo=discord&logoColor=white)

Ce document te guide pour installer les compilateurs/interpréteurs nécessaires pour différents langages de programmation sur une distribution Linux (ex : Ubuntu/Debian).
> 💡 Utilise `sudo` si tu n’es pas root.

💡 Si tu es sur **Windows** mais que tu veux compiler comme sur **Linux**, tu peux installer un terminal Linux minimal grâce à **WSL (Windows Subsystem for Linux)**.  
👉 Consulte [ce guide pour installer WSL](../linux/installation.md) si ce n'est pas déjà fait.  
👉 Tu peux aussi jeter un œil à [ce fichier pour les commandes Linux de base](../linux/commandes.md) afin de te familiariser avec le terminal.

---

## 📚 Sommaire

- [🔵 C](#-c)
- [🔵 C++](#-c-1)
- [☕ Java](#-java)
- [🌐 JavaScript (Node.js)](#-javascript-nodejs)
- [🐍 Python](#-python)
- [💎 Ruby](#-ruby)
- [🐘 PHP](#-php)
- [🦀 Rust](#-rust)
- [🐹 Kotlin](#-kotlin)
- [🗄️ SQL](#%EF%B8%8F-sql)

---

## 🔵 C
### Installation
```bash
sudo apt update
sudo apt install gcc
```

### Exemple `hello.c`
```c
#include <stdio.h>

int main() {
    printf("Hello, world!\n");
    return 0;
}
```

### Compilation et exécution
```bash
gcc hello.c -o hello
./hello
```

---

## 🔵 C++
### Installation
```bash
sudo apt update
sudo apt install g++
```

### Exemple `hello.cpp`
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, world!" << endl;
    return 0;
}
```

### Compilation et exécution
```bash
g++ hello.cpp -o hello
./hello
```

---

## ☕ Java
### Installation
```bash
sudo apt update
sudo apt install default-jdk
```

### Exemple `Hello.java`
```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
```

### Compilation et exécution
```bash
javac Hello.java
java Hello
```
> ⚠️ Le nom du fichier doit correspondre au nom de la classe `public`.

---

## 🌐 JavaScript (Node.js)
### Installation
```bash
sudo apt update
sudo apt install nodejs npm
```
> Vérifie que `node` est bien installé :
```bash
node -v
```

### Exemple `hello.js`
```javascript
console.log("Hello, world!");
```

### Exécution
```bash
node hello.js
```

---

## 🐍 Python
### Installation
```bash
sudo apt update
sudo apt install python3
```

### Exemple `hello.py`
```python
print("Hello, world!")
```

### Exécution
```bash
python3 hello.py
```

---

## 💎 Ruby
### Installation
```bash
sudo apt update
sudo apt install ruby-full
```

> Vérifie que Ruby est bien installé :
```bash
ruby -v
```

### Exemple `hello.rb`
```rb
puts "Hello, world!"
```

### Exécution
```bash
ruby hello.rb
```

---

## 🐘 PHP
### Installation
```bash
sudo apt update
sudo apt install php
```

> Vérifie que PHP est bien installé :
```bash
php -v
```

### Exemple `hello.php`
```php
<?php
echo "Hello, world!";
?>
```

### Exécution en ligne de commande
```bash
php hello.php
```

### Exécution en mode serveur local
PHP intègre un petit serveur web pratique pour les tests :
```bash
php -S localhost:8000
```
Puis ouvre ton navigateur à l’adresse 👉 [http://localhost:8000/hello.php](http://localhost:8000/hello.php)

---

## 🦀 Rust
### Installation
```bash
sudo apt update
sudo apt install rustup       # Installe rustup (gestionnaire Rust)
sudo apt install rustc        # Installe le compilateur Rust
rustup default stable         # Définit la version stable par défaut
```

> Vérifie que Rust est bien installé :
```bash
rustc --version
cargo --version
```

### Exemple `hello.rs`
```rust
fn main() {
    println!("Hello, world!");
}
```

### Compilation et exécution avec rustc
```bash
# Compiler
rustc hello.rs

# Exécuter
./hello
```

### Compilation et exécution avec Cargo (recommandé)
```bash
# Créer un projet
cargo new mon_projet
cd mon_projet

# Compiler le projet
cargo build

# Exécuter le projet
cargo run
```
> Pourquoi privilégier Cargo ?
> - `rustc` compile un seul fichier, il ne gère pas les dépendances ni le fichier `Cargo.toml`.
> - Cargo compile l’intégralité du projet, télécharge les dépendances et applique les bonnes pratiques (édition 2021 par défaut, optimisation, etc.).

---

## 🐹 Kotlin
### Installation
```bash
sudo apt update
sudo apt install default-jdk      # Kotlin a besoin de la JVM
sudo snap install --classic kotlin
```
> Vérifie que Kotlin est bien installé :
```bash
kotlin -version
```

### Exemple `Main.kt`
```kotlin
fun main() {
    println("Hello, world!")
}
```

### Compilation et exécution
```bash
# Compilation
kotlinc Main.kt -include-runtime -d Main.jar

# Exécution
java -jar Main.jar
```

> ⚡ Contrairement à Java, Kotlin génère un `.jar` directement exécutable avec la JVM.

Tu peux aussi utiliser un REPL interactif avec :
```bash
kotlin
```

---

## 🗄️ SQL
### Installation
#### SQLite (léger, rapide pour débuter)
```bash
sudo apt update
sudo apt install sqlite3
```
> Vérifie que SQLite est bien installé :
```bash
sqlite3 --version
```

#### MySQL (serveur complet)
```bash
sudo apt update
sudo apt install mysql-server
```
> Vérifie que MySQL est installé et démarré :
```bash
mysql --version
sudo systemctl status mysql
```

#### PostgreSQL
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```
> Vérifie PostgreSQL :
```bash
psql --version
sudo systemctl status postgresql
```

### Exemple `hello.sql`
```sql
SELECT 'Bonjour SQL !';
```

### Exécution
#### SQLite
```bash
sqlite3 hello.db
sqlite> .read hello.sql
```

#### MySQL
```bash
mysql -u root -p
mysql> source hello.sql;
```

#### PostgreSQL
```bash
psql -U postgres
postgres=# \i hello.sql
```
> ⚡ SQL n’est pas un langage compilé : il s’exécute directement dans le moteur de base de données.
