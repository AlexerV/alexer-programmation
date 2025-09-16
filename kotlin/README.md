# ☕ Kotlin – Cours

[![GitHub](https://img.shields.io/badge/GitHub-AlexerV-181717?logo=github)](https://github.com/AlexerV)<br>
![Discord](https://img.shields.io/badge/Discord-.alexer-5865F2?logo=discord&logoColor=white)

Bienvenue dans la section Kotlin du dépôt !  
Tu trouveras ici un cours progressif pour apprendre les bases du langage Kotlin, avec exemples, explications et bonnes pratiques.

---

## 📁 À propos de Kotlin
Kotlin est un langage moderne, concis et sécurisé, créé par JetBrains.  
Il est :
- le langage officiel recommandé pour Android par Google,
- totalement interopérable avec Java,
- utilisé aussi bien pour les applications mobiles, serveurs (Spring Boot, Ktor), desktop ou scripts.

---

## 🚀 Lancer un programme Kotlin
### 🔹 Extension
Les fichiers Kotlin se terminent par `.kt`.

### 🔹 Compilation et exécution
```bash
# Compilation
kotlinc Main.kt -include-runtime -d Main.jar

# Exécution
java -jar Main.jar
```

Ou plus simplement en script (sans compilation manuelle) :
```bash
kotlinc -script Main.kt
```

---

## 📚 Ce que tu vas apprendre
- ✅ Les bases de Kotlin
- ✅ Déclaration des variables (val / var)
- ✅ Types de données (Int, Double, String, Boolean…)
- ✅ Opérations numériques et logiques
- ✅ Saisie utilisateur (readLine)
- ✅ Conditions (if / else, when)
- ✅ Boucles (for, while, do..while)
- ✅ Fonctions (classiques, expressions, valeurs par défaut)
- ✅ Collections (List, MutableList, Map)
- ✅ Classes et objets (avec data class)
- ✅ Héritage et polymorphisme
- ✅ Null safety (?, ?:, safe calls)
- ✅ Coroutines (programmation asynchrone)
- ✅ Exemple complet de fichier .kt

---

## 📌 Prérequis
- Installer Kotlin
- Vérifier avec :
```bash
kotlinc -version
```
- Utiliser un éditeur moderne (VS Code avec extension Kotlin, IntelliJ IDEA, Android Studio).
