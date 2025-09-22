# SQL

## Extension des fichiers SQL et comment exécuter un script
- Extention d'un fichier SQL : `.sql`  
Un fichier `.sql` contient une série de commandes SQL à exécuter sur une base de données.

## Lancer un script
Selon le SGBD utilisé (MySQL, PostgreSQL, SQLite...), la commande diffère :

### MySQL/MariaDB :
```bash
mysql -u utilisateur -p base_de_donnees < script.sql
```

### PostgreSQL :
```bash
psql -U utilisateur -d base_de_donnees -f script.sql
```

### SQLite :
```bash
sqlite3 ma_base.db < script.sql
```

### Exemple simple : `hello.sql`
```sql
SELECT 'Bonjour SQL !';
```
Puis exécuter :
```bash
sqlite3 test.db < hello.sql
```

---

## Les bases
- SQL (**Structured Query Language**) est un **langage déclaratif** servant à interagir avec les bases de données.
- On l’utilise pour :
  - créer des bases et des tables
  - insérer, modifier et supprimer des données
  - interroger et filtrer des données
  - gérer les droits d’accès

---

## Création de base et table
Exemple en SQL standard (MySQL/PostgreSQL) :
```sql
CREATE DATABASE entreprise;

USE entreprise;

CREATE TABLE employes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50) NOT NULL,
    age INT,
    poste VARCHAR(50)
);
```

Explications :
- `CREATE DATABASE` : crée une nouvelle base.
- `CREATE TABLE` : crée une table avec colonnes.
- `PRIMARY KEY` : clé unique.
- `AUTO_INCREMENT` : incrémente automatiquement l’ID.
- `NOT NULL` : valeur obligatoire.

---

## Insertion de données (INSERT)
L’instruction `INSERT INTO` permet d’ajouter des données dans une table.  
Il faut préciser dans quelle table on insère, les colonnes concernées, et les valeurs à insérer.
> 👉 Ici on ajoute un nouvel employé nommé Alexer dans la table employes.
```sql
INSERT INTO employes (nom, age, poste)
VALUES ('Alexer', 21, 'Développeur');
```

On peut aussi insérer plusieurs lignes en une seule requête :
```sql
INSERT INTO employes (nom, age, poste) VALUES
('Alexer', 21, 'Développeur'),
('Bob', 40, 'Manager'),
('Charlie', 25, 'Stagiaire');
```

---

## Lire les données (SELECT)
La commande `SELECT` est utilisée pour récupérer et afficher des informations d’une table.  
On peut afficher toutes les colonnes ou seulement certaines.
```sql
-- Récupérer toutes les colonnes
SELECT * FROM employes;

-- Récupérer seulement nom et âge
SELECT nom, age FROM employes;

-- Ajouter une condition avec WHERE
SELECT * FROM employes WHERE age > 30;
```
> 👉 `SELECT` est sûrement la commande la plus utilisée en SQL : elle permet de filtrer, trier et analyser les données.

---

## Mise à jour et suppression
### Update
Permet de changer des valeurs existantes dans une table.
```sql
UPDATE employes
SET age = 26
WHERE nom = 'Charlie';
```
> 👉 Ici, on met à jour l’âge de Charlie pour qu’il devienne 26.  
> ⚠️ Attention : sans `WHERE`, toutes les lignes de la table seront modifiées !

### Delete
Permet de retirer des lignes d’une table.
```sql
DELETE FROM employes WHERE nom = 'Bob';
```
> 👉 Ici, Bob est supprimé de la table.  
> ⚠️ Comme pour `UPDATE`, si tu oublies `WHERE`, toutes les données seront supprimées.

---

## Opérateurs de comparaison et logiques
Les opérateurs de comparaison et logiques permettent de poser des conditions dans WHERE.
```sql
-- Tous les employés de moins de 30 ans
SELECT * FROM employes WHERE age < 30;

-- Tous les employés qui sont développeurs OU managers
SELECT * FROM employes WHERE poste = 'Développeuse' OR poste = 'Manager';

-- Tous sauf les stagiaires
SELECT * FROM employes WHERE poste != 'Stagiaire';

-- Employés entre 25 et 35 ans
SELECT * FROM employes WHERE age >= 25 AND age <= 35;
```
> 👉 Ces opérateurs permettent de filtrer précisément les résultats.

| Opérateur      | Exemple                              | Signification |
| -------------- | ------------------------------------ | ------------- |
| `=`            | `age = 30`                           | égal à        |
| `<>` ou `!=`   | `poste <> 'Manager'`                 | différent de  |
| `<, >, <=, >=` | `age >= 18`                          | comparaisons  |
| `AND`          | `age > 20 AND age < 40`              | ET logique    |
| `OR`           | `poste = 'Dev' OR poste = 'Manager'` | OU logique    |
| `NOT`          | `NOT(age = 30)`                      | négation      |


---

## Fonctions utiles
SQL propose de nombreuses fonctions pour analyser les données.

- Moyenne :
```sql
SELECT AVG(age) FROM employes;
```
> 👉 Retourne l’âge moyen de tous les employés.

- Nombre d’éléments :
```sql
SELECT COUNT(*) FROM employes;
```
> 👉 Compte combien d’employés il y a.

- Valeurs extrêmes :
```sql
SELECT MAX(age), MIN(age) FROM employes;
```
> 👉 Donne l’âge le plus élevé et le plus petit.

- Chaînes de caractères :
```sql
SELECT UPPER(nom), LOWER(nom) FROM employes;
```
> 👉 Affiche les noms en majuscules et en minuscules.

---

## Tri et regroupement
### ORDER BY
On peut afficher les résultats dans un ordre précis :
```sql
SELECT * FROM employes ORDER BY age DESC;
```
> 👉 Classe les employés du plus âgé au plus jeune.

### GROUP BY
Permet de faire des statistiques par groupe.
```sql
SELECT poste, COUNT(*) AS nb_employes
FROM employes
GROUP BY poste;
```
> 👉 Ici on compte combien d’employés travaillent à chaque poste (Développeuse, Manager, etc.).

---

## Jointures
Une jointure relie plusieurs tables entre elles.  
Exemple : une table `employes` et une table `departements`.
```sql
-- Table départements
CREATE TABLE departements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT
);

-- Insérer des données
INSERT INTO departements (nom) VALUES ('Informatique'), ('RH');

-- Ajouter une colonne dans employes
ALTER TABLE employes ADD COLUMN departement_id INTEGER;

-- Exemple d’insertion avec relation
INSERT INTO employes (nom, age, poste, departement_id)
VALUES ('Alexer', 21, 'Développeur', 1),
       ('Bob', 40, 'DRH', 2);

-- Jointure entre employés et départements
SELECT e.nom AS employe, e.poste, d.nom AS departement
FROM employes e
JOIN departements d ON e.departement_id = d.id;
```

```sql
SELECT e.nom, d.nom AS departement
FROM employes e
JOIN departements d ON e.departement_id = d.id;
```
> 👉 Cette requête affiche le nom de chaque employé et le département auquel il appartient.  
Sans jointure, les données seraient séparées en deux tables.

---

## Contraintes
- `PRIMARY KEY` : identifiant unique
- `FOREIGN KEY` : clé étrangère reliant 2 tables
- `UNIQUE` : pas de doublons
- `CHECK` : condition à respecter
- `NOT NULL` : obligatoire

Exemple :
```sql
CREATE TABLE salaires (
    id INT PRIMARY KEY AUTO_INCREMENT,
    montant DECIMAL(10,2) CHECK (montant > 0),
    employe_id INT,
    FOREIGN KEY (employe_id) REFERENCES employes(id)
);
```

---

## Vues
Une vue est une requête enregistrée comme une table virtuelle.
```sql
CREATE VIEW vue_dev AS
SELECT nom, age FROM employes WHERE poste = 'Développeur';
```

---

## Transactions
Permettent d’assurer l’intégrité des données.
```sql
BEGIN;

UPDATE employes SET age = age + 1;
DELETE FROM employes WHERE nom = 'Erreur';

ROLLBACK; -- annule
COMMIT;   -- valide
```

---

## Index
Améliorent les performances des recherches.
```sql
CREATE INDEX idx_nom ON employes(nom);
```

---

## Sécurité et utilisateurs
### MySQL :
```sql
CREATE USER 'alex'@'localhost' IDENTIFIED BY 'motdepasse';
GRANT ALL PRIVILEGES ON entreprise.* TO 'alex'@'localhost';
```

---

## SQL avancé
- Procédures stockées : fonctions dans la base
- Triggers : actions automatiques sur événement
- CTE (Common Table Expressions) pour requêtes complexes

Exemple CTE :
```sql
WITH jeunes AS (
    SELECT * FROM employes WHERE age < 30
)
SELECT * FROM jeunes;
```
