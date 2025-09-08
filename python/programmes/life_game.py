from random import choice
from turtle import *
from freegames import square

# Dictionnaire pour stocker l'état de chaque cellule
cells = {}

def initialize():
    """Initialisation des cellules de manière aléatoire."""
    # Remplissage du dictionnaire 'cells' avec toutes les cellules initialisées sur 'False'
    for x in range(-200, 200, 10):
        for y in range(-200, 200, 10):
            cells[x, y] = False  # Cellules mortes au départ

    # Initialisation d'une zone de cellules autour de l'origine avec des états aléatoires (vivantes ou mortes)
    for x in range(-50, 50, 10):
        for y in range(-50, 50, 10):
            cells[x, y] = choice([True, False])  # Choisit aléatoirement True (vivant) ou False (mort)


def step():
    """Effectue une étape dans le Jeu de la Vie."""
    neighbors = {}  # Dictionnaire pour stocker le nombre de voisins vivants pour chaque cellule

    # Parcours de toutes les cellules
    for x in range(-190, 190, 10):
        for y in range(-190, 190, 10):
            count = -cells[x, y]  # Compter la cellule elle-même, elle ne compte pas dans ses voisins
            # Vérification des voisins dans les huit directions autour de la cellule
            for h in [-10, 0, 10]:
                for v in [-10, 0, 10]:
                    count += cells[x + h, y + v]  # Compte le voisin si la cellule est vivante
            neighbors[x, y] = count  # Stocke le nombre de voisins vivants

    # Mise à jour de l'état de chaque cellule selon les règles du jeu
    for cell, count in neighbors.items():
        if cells[cell]:
            if count < 2 or count > 3:  # La cellule meurt si elle a moins de 2 ou plus de 3 voisins
                cells[cell] = False
        elif count == 3:  # La cellule devient vivante si elle a exactement 3 voisins
            cells[cell] = True


def draw():
    """Dessine tous les carrés."""
    step()  # Avance d'une étape du Jeu de la Vie
    clear()  # Efface le dessin précédent

    # Dessin de chaque cellule, vivante ou morte, en fonction de son état
    for (x, y), alive in cells.items():
        color = 'green' if alive else 'black'  # Vert pour une cellule vivante, noir pour une cellule morte
        square(x, y, 10, color)  # Dessine la cellule

    update()  # Met à jour l'affichage
    ontimer(draw, 100)  # Répète la fonction 'draw' toutes les 100 ms pour créer l'animation


# Initialisation de la fenêtre de jeu
setup(420, 420, 370, 0)
hideturtle()  # Cache le curseur de la tortue
tracer(False)  # Désactive l'animation de la tortue pour améliorer la performance
initialize()  # Initialise l'état des cellules
draw()  # Lance le processus de dessin
done()  # Finalise le programme turtle et attend la fermeture de la fenêtre
