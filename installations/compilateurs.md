# 🛠️ Installation des compilateurs sur Linux

Ce document te guide pour installer les compilateurs/interpréteurs nécessaires pour différents langages de programmation sur une distribution Linux (ex : Ubuntu/Debian).
> 💡 Utilise `sudo` si tu n’es pas root.

---

## 📚 Sommaire

- [🔵 C](#-c)
- [🔵 C++](#-c-1)
- [☕ Java](#-java)
- [🌐 JavaScript (Node.js)](#-javascript-nodejs)
- [🐍 Python](#-python)

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
