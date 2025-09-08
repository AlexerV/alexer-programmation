# Installation des compilateurs

## Linux

### Compilateur C

- vérifier que le compilateur est installé :
```bash
gcc --version
```
  - Si tu vois une version, comme gcc (Ubuntu 12.3.0) → c’est déjà installé.
  - Sinon, suis les étapes ci-dessous.

#### Installer GCC selon ta distribution
- Pour Ubuntu / Debian / Linux Mint :
```bash
sudo apt update
sudo apt install build-essential
```
Le paquet `build-essential` contient `gcc`, `g++`, `make`, et d'autres outils utiles pour le développement C/C++.

- Pour Arch Linux / Manjaro :
```bash
sudo pacman -S base-devel
```

- Pour Fedora / CentOS / RHEL :
```bash
sudo dnf groupinstall "Development Tools"
```

- Pour Fedora :
```bash
sudo dnf install gcc
```

#### Vérification après installation
Vérifie que le compilateur est bien installé :
```bash
gcc --version
```

#### Compilation
```bash
gcc hello.c -o hello
```
- `hello.c` = nom du programme à compiler
- `hello` = nom de sortie (nom d'exécution)

#### Exécution
```bash
./hello
```




## Windows
