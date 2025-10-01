# Conversion Binaire/Décimal/Hexadécimal

## Tableau récapitulatif
| **Binaire** | **Décimal** | **Hexadécimal** |
| ----------- | ----------- | --------------- |
| 0000        | 0           | 0               |
| 0001        | 1           | 1               |
| 0010        | 2           | 2               |
| 0011        | 3           | 3               |
| 0100        | 4           | 4               |
| 0101        | 5           | 5               |
| 0110        | 6           | 6               |
| 0111        | 7           | 7               |
| 1000        | 8           | 8               |
| 1001        | 9           | 9               |
| 1010        | 10          | A               |
| 1011        | 11          | B               |
| 1100        | 12          | C               |
| 1101        | 13          | D               |
| 1110        | 14          | E               |
| 1111        | 15          | F               |


## Conversion de binaire à décimal :
- Principe : Le système binaire est une base 2, ce qui signifie que chaque bit a une valeur de 2ⁿ, où n est la position du bit (en commençant par 0 de droite à gauche).
- Étapes :
  - Prenez chaque bit binaire (0 ou 1) et multipliez-le par 2 élevé à la puissance de sa position, en commençant par la position 0 (à droite).
  - Additionnez les résultats.

Exemple :

Convertir 1011 (binaire) en décimal :

1×2<sup>3</sup>+0×2<sup>2</sup>+1×2<sup>1</sup>+1×2<sup>0</sup>=8+0+2+1=11

Donc, 1011 (binaire) = 11 (décimal).

## Conversion de décimal à binaire :
- Principe : Le système décimal est en base 10, et pour le convertir en binaire (base 2), on divise le nombre décimal par 2, en conservant le reste à chaque division, et on lit les restes dans l'ordre inverse.
- Étapes :
  - Divisez le nombre décimal par 2.
  - Conservez le reste (0 ou 1).
  - Répétez l'opération jusqu'à ce que le quotient soit 0.
  - Lisez les restes dans l'ordre inverse pour obtenir le nombre binaire.

Exemple :

Convertir 13 (décimal) en binaire :

- 13 ÷ 2 = 6, reste = 1
- 6 ÷ 2 = 3, reste = 0
- 3 ÷ 2 = 1, reste = 1
- 1 ÷ 2 = 0, reste = 1

Les restes, lus de bas en haut, donnent 1101.

Donc, 13 (décimal) = 1101 (binaire).

## Conversion de binaire à hexadécimal :
- Principe : Chaque groupe de 4 bits (un "nibble") en binaire correspond à un chiffre hexadécimal. Le binaire est une base 2 et l'hexadécimal une base 16.
- Étapes :
  - Divisez le nombre binaire en groupes de 4 bits, en partant de la droite.
  - Si le dernier groupe contient moins de 4 bits, ajoutez des zéros à gauche.
  - Convertissez chaque groupe de 4 bits en un chiffre hexadécimal en utilisant le tableau suivant :
    - 0000 = 0, 0001 = 1, 0010 = 2, 0011 = 3, 0100 = 4, 0101 = 5, 0110 = 6, 0111 = 7
    - 1000 = 8, 1001 = 9, 1010 = A, 1011 = B, 1100 = C, 1101 = D, 1110 = E, 1111 = F

Exemple :

Convertir 11011011 (binaire) en hexadécimal :

- Divisez le binaire en deux groupes de 4 bits : 1101 et 1011.
- 1101 = D et 1011 = B.

Donc, 11011011 (binaire) = DB (hexadécimal).

## Conversion d'hexadécimal à binaire :
- Principe : Chaque chiffre hexadécimal peut être converti directement en 4 bits binaires.
- Étapes :
  - Prenez chaque caractère hexadécimal.
  - Convertissez chaque caractère en un groupe de 4 bits binaire en utilisant le tableau de correspondance.

| Hexadécimal | Binaire |
| ----------- | ------- |
| 0           | 0000    |
| 1           | 0001    |
| 2           | 0010    |
| 3           | 0011    |
| 4           | 0100    |
| 5           | 0101    |
| 6           | 0110    |
| 7           | 0111    |
| 8           | 1000    |
| 9           | 1001    |
| A           | 1010    |
| B           | 1011    |
| C           | 1100    |
| D           | 1101    |
| E           | 1110    |
| F           | 1111    |

Exemple :

Convertir 3F (hexadécimal) en binaire :

- 3 = 0011 et F = 1111.

Donc, 3F (hexadécimal) = 00111111 (binaire).

## Conversion de décimal à hexadécimal :
- Principe : Le système décimal est en base 10, et pour le convertir en hexadécimal (base 16), on divise le nombre décimal par 16 et on garde le reste.
- Étapes :
  - Divisez le nombre décimal par 16.
  - Conservez le reste (0 à 15), qui correspond à un chiffre hexadécimal.
  - Répétez jusqu'à ce que le quotient soit 0.
  - Lisez les restes dans l'ordre inverse pour obtenir le nombre hexadécimal.

Exemple :

Convertir 255 (décimal) en hexadécimal :

- 255 ÷ 16 = 15, reste = 15 → F
- 15 ÷ 16 = 0, reste = 15 → F

Les restes, lus de bas en haut, donnent FF.

Donc, 255 (décimal) = FF (hexadécimal).

## Conversion d'hexadécimal à décimal :
- Principe : L'hexadécimal est en base 16. Pour convertir un nombre hexadécimal en décimal, chaque chiffre hexadécimal est multiplié par 16 élevé à la puissance de sa position (en partant de 0 de droite à gauche).
- Étapes :
  - Prenez chaque chiffre hexadécimal.
  - Multipliez chaque chiffre par 16 élevé à la puissance de sa position.
  - Additionnez les résultats.

Exemple :

Convertir A3 (hexadécimal) en décimal :

- A = 10 et 3 = 3.
- A3 = (10 × 16¹) + (3 × 16⁰) = 160 + 3 = 163.

Donc, A3 (hexadécimal) = 163 (décimal).
