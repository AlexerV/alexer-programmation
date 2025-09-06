import cv2  # Importation de la bibliothèque OpenCV pour capturer des vidéos et traiter les images
import numpy as np  # Importation de NumPy pour la manipulation de tableaux d'images
from PIL import Image, ImageTk  # Importation de Pillow (PIL) pour manipuler les images et ImageTk pour l'intégration avec Tkinter
import tkinter as tk  # Importation de Tkinter pour créer une interface graphique

# Définir les caractères utilisés pour l'art ASCII
# La liste de caractères représente différents niveaux de luminosité, du plus sombre (@) au plus clair (espace)
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    """Redimensionne l'image pour l'adapter à la largeur donnée tout en conservant les proportions."""
    width, height = image.size  # Récupère les dimensions de l'image originale
    ratio = height / width / 1.65  # Ajuste le ratio pour compenser la différence d'aspect des pixels (effet de 'compression' vertical)
    new_height = int(new_width * ratio)  # Calcule la nouvelle hauteur selon le ratio ajusté
    resized_image = image.resize((new_width, new_height))  # Redimensionne l'image
    return resized_image  # Retourne l'image redimensionnée

def grayscale_image(image):
    """Convertit l'image en niveaux de gris."""
    return image.convert("L")  # Utilise le mode 'L' (luminance) pour convertir l'image en niveaux de gris

def pixel_to_ascii(image):
    """Convertit chaque pixel de l'image en un caractère ASCII."""
    pixels = np.array(image)  # Convertit l'image en un tableau NumPy pour faciliter l'accès aux pixels
    ascii_str = ""  # Chaîne vide pour stocker l'art ASCII
    
    for row in pixels:  # Parcours chaque ligne de pixels de l'image
        for pixel in row:  # Parcours chaque pixel dans la ligne
            ascii_str += ASCII_CHARS[pixel // 32]  # Mappe la valeur du pixel à un caractère ASCII en fonction de sa luminosité
        ascii_str += "\n"  # Ajoute une nouvelle ligne après chaque ligne de pixels
    return ascii_str  # Retourne la chaîne ASCII complète

def image_to_ascii(image, new_width=100):
    """Convertit une image en art ASCII en redimensionnant et en la convertissant en niveaux de gris."""
    image = resize_image(image, new_width)  # Redimensionne l'image
    image = grayscale_image(image)  # Convertit l'image en niveaux de gris
    ascii_str = pixel_to_ascii(image)  # Convertit l'image en art ASCII
    return ascii_str  # Retourne l'art ASCII

def update_ascii_art():
    """Capture une image de la caméra, la convertit en ASCII, et met à jour l'affichage."""
    ret, frame = cap.read()  # Capture une image de la caméra
    if not ret:  # Si la capture échoue (pas d'image disponible)
        return  # Quitte la fonction
    
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))  # Convertit l'image OpenCV (BGR) en image Pillow (RGB)
    ascii_art = image_to_ascii(image, new_width=100)  # Convertit l'image en art ASCII
    
    # Met à jour le texte dans le widget Text avec l'art ASCII généré
    text_widget.delete("1.0", tk.END)  # Supprime le texte existant dans le widget Text
    text_widget.insert(tk.END, ascii_art)  # Insère le nouvel art ASCII à la fin du widget

    # Met à jour la fenêtre après 30 millisecondes pour afficher la nouvelle image
    root.after(30, update_ascii_art)  # Appelle cette fonction à nouveau après 30ms (mise à jour continue)

# Initialisation de la capture vidéo à partir de la caméra
cap = cv2.VideoCapture(0)  # Ouvre le flux vidéo de la caméra par défaut (0 pour la première caméra, 1 pour la seconde, etc.)
if not cap.isOpened():  # Si la caméra n'a pas pu être ouverte
    print("Erreur : Impossible d'accéder à la caméra.")  # Affiche un message d'erreur

# Création de la fenêtre principale Tkinter
root = tk.Tk()  # Crée une fenêtre Tkinter
root.title("ASCII Art")  # Définit le titre de la fenêtre

# Définir la taille initiale de la fenêtre (largeur x hauteur)
root.geometry("1200x800")  # Largeur de 1200px et hauteur de 800px

# Création d'un widget Text pour afficher l'art ASCII
text_widget = tk.Text(root, font=("Courier", 10), bg="black", fg="white")  # Widget Text avec fond noir et texte blanc
text_widget.pack(expand=True, fill=tk.BOTH)  # Pack le widget pour qu'il occupe toute la fenêtre

# Lancer la mise à jour de l'art ASCII immédiatement
root.after(0, update_ascii_art)  # Appelle la fonction update_ascii_art dès que la fenêtre est affichée

# Lancer la boucle principale de Tkinter (pour l'interface graphique)
root.mainloop()  # Cette boucle permet à Tkinter de gérer les événements (clics, mises à jour, etc.)

# Libération de la caméra et fermeture des fenêtres OpenCV après la fermeture de la fenêtre Tkinter
cap.release()  # Libère la caméra pour qu'elle puisse être utilisée par d'autres programmes
cv2.destroyAllWindows()  # Ferme toutes les fenêtres ouvertes par OpenCV
