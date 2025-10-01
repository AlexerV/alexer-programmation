# La commande `tar`
La commande `tar` (pour Tape ARchive) est utilisée principalement pour l'archivage et la compression de fichiers ou de répertoires sous Linux. Elle permet de combiner plusieurs fichiers ou répertoires en un seul fichier d'archive (tarball) et peut également être utilisée pour compresser cet archive à l'aide de différents outils comme `gzip`, `bzip2`, ou `xz`.

**Remarque importante :**
- `gzip` est plus rapide à compresser, mais le xz a le meilleur taux de compression.
- `bzip2` se situe entre les deux en termes de vitesse et de taux de compression.

## Créer une archive et la compresser
Pour archiver un dossier ou un fichier entier et le compresser, la commande `tar` s'utilise comme suit :
```bash
tar -cvzf monArchive.tar.gz /chemin/vers/dossier
```
Voici ce que chaque option signifie :
- `-c` : Créer une nouvelle archive.
- `-v` : Mode verbeux (affiche la progression et les fichiers traités).
- `-z` : Compresser l'archive avec `gzip` (si vous souhaitez utiliser `xz`, remplacez-le par `-J` et pour `bzip2`, remplacez par `-j`).
- `-f` : Spécifie le nom de l'archive à créer (ici, `monArchive.tar.gz`).

Cela créera une archive compressée avec `gzip` appelée `monDossier.tar.gz`. Tous les fichiers et sous-dossiers du répertoire seront inclus dans l'archive.

## Formats de compression
- `gzip` : Compression rapide mais moins efficace.
- `bzip2` : Meilleur taux de compression, mais plus lent que `gzip`.
- `xz` : Meilleur taux de compression, plus lent encore, mais extrêmement efficace pour les très gros fichiers.

Les options pour utiliser ces outils de compression sont les suivantes :
- `-z` : Compression avec `gzip`.
- `-j` : Compression avec `bzip2`.
- `-J` : Compression avec `xz`.

**Exemples :**
- Avec `gzip` :
```bash
tar -cvzf archive.tar.gz /chemin/vers/fichier-ou-dossier
```

- Avec `bzip2` :
```bash
tar -cvjf archive.tar.bz2 /chemin/vers/fichier-ou-dossier
```

- Avec `xz` :
```bash
tar -cvJf archive.tar.xz /chemin/vers/fichier-ou-dossier
```

## Extraire une archive et la décompresser
Une fois l'archive créée, vous pouvez facilement la décompresser et l'extraire avec la commande `tar` :
```bash
tar -xzvf monArchive.tar.gz
```

Voici ce que signifient les options :
- `-x` : Extraire (décompresser) l'archive.
- `-z` : Utiliser gzip pour décompresser (si l'archive est compressée avec `xz`, remplacez-le par `-J` et pour `bzip2`, remplacez par `-j`).
- `-v` : Mode verbeux (affiche les fichiers extraits).
- `-f` : Spécifie le fichier à traiter (ici, `monArchive.tar.gz`).

Cela extrait tout le contenu de l'archive `monArchive.tar.gz` dans le répertoire courant.

## Extraire une archive dans un répertoire spécifique
Il est également possible de spécifier un répertoire cible pour l'extraction des fichiers :
```bash
tar -xzvf monArchive.tar.gz -C /chemin/vers/repertoire
```
Cela extraira l'archive dans le répertoire `/chemin/vers/repertoire`.

## Vérification de l'archive
Si vous souhaitez simplement vérifier le contenu d'une archive sans l'extraire, vous pouvez utiliser l'option `-t` :
```bash
tar -tvf monArchive.tar.gz
```

Cela affiche la liste des fichiers contenus dans l'archive.

## Ajouter des fichiers à une archive existante
Il est aussi possible d'ajouter des fichiers à une archive tar existante en utilisant l'option `-r` (concatenate files to an archive) :
```bash
tar -rvf monArchive.tar fichier1 fichier2
```

Cette commande ajoute `fichier1` et `fichier2` à l'archive `monArchive.tar`.

## Suppression d'un fichier d'une archive
Pour supprimer un fichier d'une archive existante, vous pouvez utiliser l'option `--delete` :
```bash
tar --delete -f monArchive.tar fichierASupprimer
```

Note : Cette opération est assez coûteuse, car elle doit recréer l'archive sans le fichier supprimé.
