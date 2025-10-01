# Les bases de données
Une **base de données** est un ensemble structuré et organisé d'informations ou de données, généralement stockées électroniquement dans un système informatique. Les bases de données permettent de stocker, organiser, récupérer, mettre à jour, et manipuler de grandes quantités d'informations de manière efficace.

Les bases de données sont utilisées dans divers domaines, allant de la gestion de données commerciales à la gestion des informations personnelles. Voici quelques exemples de bases de données populaires :
- **PostgreSQL** : Système de gestion de base de données relationnelle open-source.
- **Oracle** : Base de données relationnelle propriétaire de Oracle Corporation.
- **Microsoft Access** : Base de données relationnelle qui fait partie de la suite Microsoft Office.
- **MariaDB** : Un fork de MySQL, utilisé pour des applications web.
- **MySQL** : Base de données relationnelle open-source très utilisée pour les applications web.
- **IBM DB2** : Base de données relationnelle développée par IBM.

## Les catégories de commandes SQL
### DDL (Data Definition Language) :
- La DDL est utilisée pour définir et structurer la base de données. Elle inclut des commandes pour la création, modification, et suppression des objets de la base de données comme les tables, index, etc.
- Commandes principales :
  - `CREATE` : Créer une base de données, une table, un index, etc.
  - `ALTER` : Modifier une table ou une base de données existante.
  - `DROP` : Supprimer une base de données ou une table.

### DCL (Data Control Language) :
- La DCL est utilisée pour gérer les droits d'accès aux objets de la base de données, en permettant à l'administrateur de la base de données de contrôler qui peut accéder ou modifier les données.
- Commandes principales :
  - `GRANT` : Accorder des privilèges d'accès.
  - `REVOKE` : Retirer des privilèges d'accès.

### DML (Data Manipulation Language) :
- La DML est utilisée pour manipuler les données dans les tables de la base de données. Elle inclut des commandes pour lire, insérer, mettre à jour, et supprimer des données.
- Commandes principales :
  - `SELECT` : Récupérer des données.
  - `INSERT` : Ajouter des données.
  - `UPDATE` : Modifier des données existantes.
  - `DELETE` : Supprimer des données.

## Les clés dans une base de données
Les clés sont des éléments essentiels dans la conception de bases de données relationnelles. Elles permettent d'identifier de manière unique les enregistrements et de lier les tables entre elles.

- Clé naturelle : Une clé naturelle est un attribut ou un ensemble d'attributs qui existe naturellement dans les données pour identifier de manière unique chaque enregistrement. Par exemple, une combinaison de "nom" et "prénom" peut constituer une clé naturelle si ces valeurs sont uniques dans une table.

- Clé technique : Lorsqu'il n'y a pas de clé naturelle, une clé technique est ajoutée sous la forme d'un identifiant unique (souvent appelé id ou code), généré par le système. Cela garantit que chaque enregistrement peut être identifié de manière unique.

- Clé primaire : La clé primaire est une clé qui permet d'identifier de manière unique chaque enregistrement d'une table. Une table ne peut avoir qu'une seule clé primaire, et elle ne peut contenir de valeurs nulles.

Exemple :
```sql
CREATE TABLE employes (
    id INT PRIMARY KEY,
    nom VARCHAR(50),
    prenom VARCHAR(50),
    age INT
);
```
Ici, la colonne `id` est la clé primaire.

- Clé étrangère : Une clé étrangère est une clé dans une table qui pointe vers la clé primaire d'une autre table. Elle permet de définir des relations entre les tables.

Exemple :
```sql
CREATE TABLE services (
    id INT PRIMARY KEY,
    nom_service VARCHAR(50)
);

CREATE TABLE employes (
    id INT PRIMARY KEY,
    nom VARCHAR(50),
    prenom VARCHAR(50),
    id_service INT,
    FOREIGN KEY (id_service) REFERENCES services(id)
);
```

Dans cet exemple, `id_service` dans la table `employes` est une clé étrangère qui fait référence à `id` dans la table `services`.

## La normalisation des bases de données
La normalisation est un processus de conception des bases de données qui permet d'éviter les redondances de données et d'assurer la cohérence et l'intégrité des informations. Elle est réalisée par le biais de plusieurs formes normales.
- Première forme normale (1NF) :
  - Une table est en 1NF si elle respecte les critères suivants :
    - Elle possède une clé primaire.
    - Chaque colonne contient des valeurs atomiques (c'est-à-dire que chaque valeur est indivisible). Par exemple, une colonne "nomPrenom" n'est pas atomique car elle contient deux informations.
    - Aucune colonne ne contient des collections de valeurs (pas de listes dans une seule colonne).

Exemple (non conforme à la 1NF) :
```sql
CREATE TABLE contacts (
    id INT PRIMARY KEY,
    nom VARCHAR(50),
    prenoms VARCHAR(100)  -- Liste de prénoms : "Jean, Pierre"
);
```

Ce n'est pas une bonne pratique car la colonne `prenoms` contient plusieurs valeurs (non atomiques).

- Deuxième forme normale (2NF) :
  - Une table est en 2NF si elle est en 1NF et que tous les attributs non-clé dépendent entièrement de la clé primaire (pas de dépendances partielles).
  - Pour la mettre en 2NF, on doit :
    - Regrouper dans une nouvelle table les attributs dépendants d'une partie de la clé (si la clé primaire est composite) et faire de cette partie de la clé la clé primaire de la nouvelle table.
    - Regrouper dans une autre table les attributs qui dépendent de la totalité de la clé.

Exemple :
Si une table `employes` a une clé composite (`id_employe`, `id_service`), et que l'attribut `nom_service` dépend uniquement de `id_service` et non de l'ensemble de la clé, il faut séparer les informations en deux tables.

Table `employes` (en 2NF) :
```sql
CREATE TABLE employes (
    id_employe INT,
    id_service INT,
    nom VARCHAR(50),
    PRIMARY KEY (id_employe, id_service)
);
```

Table `services` (en 2NF) :
```sql
CREATE TABLE services (
    id_service INT PRIMARY KEY,
    nom_service VARCHAR(50)
);
```

La table `employes` ne contient plus `nom_service`, qui est déplacé dans la table `services`.
