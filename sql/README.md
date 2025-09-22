# 🗄️ SQL - Cours

[![GitHub](https://img.shields.io/badge/GitHub-AlexerV-181717?logo=github)](https://github.com/AlexerV)<br>
![Discord](https://img.shields.io/badge/Discord-.alexer-5865F2?logo=discord&logoColor=white)

Bienvenue dans la section SQL du dépôt !  
Tu trouveras ici un cours progressif pour apprendre à manipuler des bases de données relationnelles, avec exemples, explications et bonnes pratiques.

---

## 📁 À propos de SQL
SQL (**Structured Query Language**) est un langage de requêtes utilisé pour interagir avec les bases de données.  
Il permet de :
- créer des tables (structure des données),
- insérer des données,
- lire et filtrer des données,
- mettre à jour ou supprimer des données,
- faire des jointures entre plusieurs tables,
- trier, regrouper et analyser les informations.

C’est la base de la plupart des systèmes de gestion de bases de données relationnelles (SGBD) : MySQL, PostgreSQL, SQLite, SQL Server, Oracle, etc.

---

## 🚀 Exécuter du SQL
### 🔹 Extension
Les fichiers se terminent par `.sql`.

### 🔹 Exécution d’un script
Selon le SGBD que tu utilises :
```bash
# MySQL
mysql -u utilisateur -p < fichier.sql

# PostgreSQL
psql -U utilisateur -f fichier.sql

# SQLite
sqlite3 ma_base.db < fichier.sql
```

---

## 📚 Ce que tu vas apprendre
- ✅ Créer une base de données et des tables
- ✅ Insérer des données (`INSERT`)
- ✅ Lire et filtrer des données (`SELECT`, `WHERE`)
- ✅ Modifier ou supprimer des données (`UPDATE`, `DELETE`)
- ✅ Utiliser les opérateurs logiques et de comparaison
- ✅ Fonctions utiles (`COUNT`, `AVG`, `MAX`, etc.)
- ✅ Tri (`ORDER BY`) et regroupement (`GROUP BY`)
- ✅ Jointures entre tables (`JOIN`)
- ✅ Exemple complet de script `.sql`

---

## 📌 Prérequis
- Avoir un SGBD installé (MySQL, PostgreSQL ou SQLite recommandés).
- Vérifier l’accès avec :
```bash
mysql --version
psql --version
sqlite3 --version
```
- Utiliser un éditeur de code ou client SQL (VS Code avec extension SQL, DBeaver, HeidiSQL, etc.).
