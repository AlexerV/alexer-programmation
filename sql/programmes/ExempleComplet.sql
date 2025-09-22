-- cours.sql
-- Exemple complet pour apprendre les bases du SQL

-- ================================
-- 1) Création d'une base de données (selon le SGBD)
-- ================================
-- (MySQL/PostgreSQL uniquement, pas nécessaire pour SQLite)
CREATE DATABASE entreprise;
USE entreprise;  -- MySQL
-- \c entreprise;  -- PostgreSQL

-- ================================
-- 2) Création d'une table
-- ================================
CREATE TABLE employes (
    id INT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    age INT,
    poste VARCHAR(50),
    salaire DECIMAL(10,2)
);

-- ================================
-- 3) Insertion de données
-- ================================
INSERT INTO employes (id, nom, age, poste, salaire) VALUES
(1, 'Alexer', 21, 'Développeur', 3500.00),
(2, 'Bob', 25, 'Designer', 2800.00),
(3, 'Charlie', 40, 'Manager', 5000.00),
(4, 'Diana', 28, 'Développeuse', 3700.00),
(5, 'AutreAlexer', 35, 'Analyste', 4000.00);

-- ================================
-- 4) Lecture de données
-- ================================
-- Tout afficher
SELECT * FROM employes;

-- Filtrer : employés de plus de 30 ans
SELECT nom, poste FROM employes WHERE age > 30;

-- ================================
-- 5) Mise à jour et suppression
-- ================================
-- Augmenter le salaire de Bob
UPDATE employes SET salaire = 3000 WHERE nom = 'Bob';

-- Supprimer un employé
DELETE FROM employes WHERE id = 5;

-- ================================
-- 6) Opérateurs
-- ================================
-- Employés développeurs OU ayant plus de 35 ans
SELECT * FROM employes WHERE poste = 'Développeur' OR age > 35;

-- ================================
-- 7) Fonctions utiles
-- ================================
-- Nombre d'employés
SELECT COUNT(*) AS total_employes FROM employes;

-- Salaire moyen
SELECT AVG(salaire) AS salaire_moyen FROM employes;

-- Âge maximum
SELECT MAX(age) AS age_max FROM employes;

-- ================================
-- 8) Tri et regroupement
-- ================================
-- Trier par salaire décroissant
SELECT nom, salaire FROM employes ORDER BY salaire DESC;

-- Salaire moyen par poste
SELECT poste, AVG(salaire) AS salaire_moyen
FROM employes
GROUP BY poste;

-- ================================
-- 9) Jointures (créons une 2ème table)
-- ================================
CREATE TABLE projets (
    id INT PRIMARY KEY,
    nom VARCHAR(50),
    employe_id INT,
    FOREIGN KEY (employe_id) REFERENCES employes(id)
);

INSERT INTO projets (id, nom, employe_id) VALUES
(1, 'Site Web', 1),
(2, 'Application Mobile', 2),
(3, 'Migration Base de Données', 3),
(4, 'Refonte UI', 4);

-- Jointure employes + projets
SELECT e.nom AS employe, e.poste, p.nom AS projet
FROM employes e
JOIN projets p ON e.id = p.employe_id;

-- ================================
-- Fin du script
-- ================================
