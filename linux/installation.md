# 🐧 Installer une distribution Linux sur Windows avec WSL

> ⚠️ Ce guide permet d’installer **uniquement un terminal Linux** (ligne de commande) sous Windows.  
> Il **n'inclut pas d'interface graphique** (comme GNOME, KDE, etc.).

---

## 🔧 Étapes d'installation

### 1. Ouvrir l'invite de commande Windows
- Appuyez sur `Win + R`, tapez `cmd`, puis validez.

### 2. Installer WSL
Dans l'invite de commande, entrez la commande suivante pour installer WSL :
```bash
wsl --install
```
Cela va installer WSL ainsi que la distribution Linux par défaut (généralement **Ubuntu**). Si tu veux une autre distribution, tu peux la choisir à l'étape suivante.
> 💡 Astuce : Si tu veux vérifier la version de WSL installée, tu peux utiliser cette commande : `wsl --list --verbose` pour afficher les versions de WSL et les distributions installées.

### 3. Lister les distributions disponibles
Pour voir toutes les distributions Linux disponibles à l’installation, utilise la commande suivante :
```bash
wsl --list --online
```
Cela te donnera une liste de distributions que tu peux installer, comme Ubuntu, Debian, Kali Linux, Fedora, etc.

### 4. Installer une distribution spécifique
Remplacez `[distribution]` par le nom de la distribution souhaitée :
```bash
wsl --install -d [distribution]
```

Exemple avec Ubuntu :
```bash
wsl --install -d Ubuntu
```

### 5. Redémarrer l'ordinateur
Une fois l’installation terminée, il est nécessaire de redémarrer ton ordinateur pour finaliser l'installation de WSL.

### 6. Lancer la distribution Linux
Après redémarrage :
1. Ouvrez le menu Démarrer

2. Recherchez le nom de la distribution installée (ex : Ubuntu)

![Menu Démarrer Linux](./images/Capture_decran_2024-02-09_183937.png)

3. Cliquez dessus pour lancer votre terminal Linux

![Terminal Linux lancé](./images/Capture_decran_2024-02-09_183859.png)


### Et après ?

Pour commencer à utiliser ton terminal Linux efficacement, consulte la section sur les [commandes Linux essentielles](./commandes.md).
> 💡 Conseil supplémentaire : Tu peux aussi configurer ton environnement WSL pour l’utiliser avec des outils de développement comme Docker, Python, ou même un serveur web local pour tester tes projets !
