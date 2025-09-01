import cv2
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk

# Définir les caractères utilisés pour l'art ASCII
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65  # Ajustement du ratio pour l'affichage
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = np.array(image)
    ascii_str = ""
    for row in pixels:
        for pixel in row:
            ascii_str += ASCII_CHARS[pixel // 32]
        ascii_str += "\n"
    return ascii_str

def image_to_ascii(image, new_width=100):
    image = resize_image(image, new_width)
    image = grayscale_image(image)
    ascii_str = pixel_to_ascii(image)
    return ascii_str

def update_ascii_art():
    ret, frame = cap.read()
    if not ret:
        return

    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    ascii_art = image_to_ascii(image, new_width=100)

    # Mettre à jour le texte dans le widget Text
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, ascii_art)

    # Mettre à jour la fenêtre après 30 ms
    root.after(30, update_ascii_art)

# Initialisation de la capture de la caméra
cap = cv2.VideoCapture(0) # Ici le 0 correspond à l'entrée de caméra par défaut, si il y a plusieurs entrées de caméras, utiliser 1 ou 2.
if not cap.isOpened():
    print("Erreur : Impossible d'accéder à la caméra.")

# Création de la fenêtre principale tkinter
root = tk.Tk()
root.title("ASCII Art")

# Définir la taille initiale de la fenêtre
root.geometry("1200x800")

# Création d'un widget Text pour afficher l'art ASCII
text_widget = tk.Text(root, font=("Courier", 10), bg="black", fg="white")
text_widget.pack(expand=True, fill=tk.BOTH)

# Lancer la mise à jour de l'art ASCII
root.after(0, update_ascii_art)

# Lancer la boucle principale tkinter
root.mainloop()

# Libération de la caméra après la fermeture de la fenêtre
cap.release()
cv2.destroyAllWindows()
