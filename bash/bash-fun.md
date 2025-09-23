# Bash / Shell - Commandes Drôles et Amusantes

En plus des bases du shell et des concepts avancés que nous avons vus jusqu'ici, nous allons explorer quelques commandes drôles et surprenantes. Ces commandes ne sont pas seulement amusantes, mais elles montrent aussi la flexibilité et l'ingéniosité de Bash.

---

## 1. `cowsay` - La vache qui parle
La commande `cowsay` génère un joli texte "parlé" par une vache (ou d’autres animaux selon l'option choisie).

### Installation
```bash
sudo apt install cowsay
```

### Exemple
```bash
cowsay "Bienvenue dans le monde de Bash !"
```

### Résultat
```markdown
 ___________________________________
< Bienvenue dans le monde de Bash ! >
 -----------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

---

## 2. `fortune` - Une citation au hasard
La commande `fortune` génère une citation, une phrase ou une blague aléatoire.

### Installation
```bash
sudo apt install fortune
```

### Exemple
```bash
fortune
```

---

## 3. `sl` - Le train
Quand tu tapes accidentellement `sl` au lieu de `ls`, un train (symbole de "Steam Locomotive") traverse l'écran.
### Installation
```bash
sudo apt install sl
```

### Exemple
```bash
sl
```

---

## 4. `yes` - Réponse automatique à tout
La commande `yes` répète indéfiniment une chaîne donnée, ce qui est utile pour répondre automatiquement à une question dans certains scripts.

### Exemple
```bash
yes "Je suis un génie du Bash !"
```
> Tu peux l'arrêter avec un `CTRL + C`

---

## 5. `toilet` - Texte en art ASCII
La commande `toilet` transforme un texte en art ASCII stylisé.

### Installation
```bash
sudo apt install toilet
```

### Exemple
```bash
toilet "Bonjour !"
```

### Options
```bash
-f term ou -f mono12      # choisir la police
-F border                 # ajouter une bordure
-F metal                  # une couleur "métalisée"

toilet -f mono12 -F border -F metal "Alexer"  # exemple complet
```

---

## 6. `figlet` - Texte en grandes lettres ASCII
Semblable à `toilet`, mais avec des styles différents. Il génère un texte en grandes lettres ASCII.

### Installation
```bash
sudo apt install figlet
```

### Exemple
```bash
figlet "Alexer"
```

### Options
```bash
-f slant                # écriture en italique

figlet -f slant "Alexer"  # exemple complet
```

---

## 7. `watch` - Surveillance en temps réel
La commande `watch` permet de répéter une commande à intervalle régulier, idéal pour surveiller un fichier ou une commande.

### Exemple
```bash
watch ls -l
```
> Cette commande affichera continuellement la sortie de `ls -l` toutes les 2 secondes.

---

## 8. `rev` - Inverser un texte
La commande `rev` inverse les caractères de chaque ligne d'un fichier ou d'un texte donné.

### Exemple
```bash
echo "Bonjour" | rev
```

---

## 9. `banner` - Texte géant en ASCII
Le programme `banner` génère du texte géant en ASCII, utile pour des messages d’accueil ou d’avertissement dans des scripts.

### Installation
```bash
sudo apt install sysvbanner
```

### Exemple
```bash
banner "Bienvenue dans Bash"
```

---

## 10. `lolcat` - Un texte arc-en-ciel
La commande `lolcat` permet d'ajouter un effet de couleur arc-en-ciel (effet "rainbow") à du texte dans ton terminal.

### Installation
```bash
sudo apt install lolcat
```

### Exemple
```bash
lolcat fichier.txt
```

---

## Mélanger des commandes

Le **pipe (`|`)** est un opérateur qui permet de chaîner plusieurs commandes ensemble, de manière à ce que la sortie d'une commande devienne l'entrée de la suivante.
Cela permet de combiner des outils de façon puissante et efficace sans avoir à enregistrer les résultats dans un fichier temporaire.

Syntaxe
```bash
commande1 | commande2 | commande3
```

- Commande1 produit une sortie (l'information à traiter).
- Cette sortie devient l'entrée de commande2.
- Et ainsi de suite pour les autres commandes.

### Une vache arc-en-ciel qui donne une citation
```bash
fortune | cowsay | lolcat
```

### Un train arc-en-ciel
```bash
sl | lolcat
```

### Une vache qui donne une citation toutes les 2 secondes
```bash
watch -n 2 "fortune | cowsay"
```

### Une bannière arc-en-ciel
```bash
toilet -f mono12 -F border "Alexer" | lolcat
```
