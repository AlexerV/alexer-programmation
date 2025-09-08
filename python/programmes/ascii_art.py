from PIL import Image  # Importation de la bibliothèque Pillow (PIL) pour manipuler les images

# Liste de caractères ASCII par ordre de luminosité
# Les caractères les plus sombres sont à gauche et les plus clairs à droite.
ASCII_CHARS = "@%#*+=-:. "  # Liste des caractères utilisés pour représenter l'intensité lumineuse des pixels

def scale_image(image, new_width=100):
    """Redimensionner l'image en fonction de la largeur donnée tout en conservant le ratio."""
    (original_width, original_height) = image.size  # Obtient les dimensions originales de l'image
    aspect_ratio = original_height / original_width  # Calcul du ratio de l'aspect pour garder les proportions
    new_height = int(aspect_ratio * new_width)  # Calcul de la nouvelle hauteur en fonction de la largeur
    new_image = image.resize((new_width, new_height))  # Redimensionne l'image avec la nouvelle largeur et hauteur
    return new_image  # Retourne l'image redimensionnée

def convert_to_grayscale(image):
    """Convertir l'image en niveaux de gris."""
    return image.convert("L")  # Convertit l'image en niveaux de gris avec le mode "L" (luminance)

def map_pixels_to_ascii(image, range_width=25):
    """Convertir les pixels en caractères ASCII."""
    pixels = image.getdata()  # Récupère tous les pixels de l'image sous forme d'une séquence
    ascii_str = ""  # Initialise une chaîne vide pour stocker l'art ASCII
    
    for pixel_value in pixels:  # Parcours de chaque pixel
        ascii_str += ASCII_CHARS[pixel_value // range_width]  # Mappe l'intensité du pixel à un caractère ASCII
        # Diviser la valeur du pixel par range_width permet de réduire l'échelle à la taille de la liste ASCII_CHARS
    
    return ascii_str  # Retourne la chaîne ASCII obtenue à partir des pixels

def convert_image_to_ascii(image, new_width=100):
    """Convertir une image en art ASCII."""
    image = scale_image(image, new_width)  # Redimensionner l'image pour qu'elle ait la largeur donnée
    image = convert_to_grayscale(image)  # Convertir l'image en niveaux de gris

    ascii_str = map_pixels_to_ascii(image)  # Convertir les pixels de l'image en art ASCII
    img_width = image.width  # Récupère la largeur de l'image (après redimensionnement)
    ascii_str_len = len(ascii_str)  # Calcule la longueur de la chaîne ASCII générée
    
    ascii_img = ""  # Initialise une chaîne vide pour l'art ASCII formaté
    for i in range(0, ascii_str_len, img_width):  # Parcours de la chaîne ASCII par lignes
        ascii_img += ascii_str[i:i+img_width] + "\n"  # Ajoute chaque ligne d'ASCII à l'art final
    
    return ascii_img  # Retourne l'art ASCII formaté

def main(image_path, new_width=100):
    """Charger l'image et la convertir en ASCII."""
    try:
        image = Image.open(image_path)  # Tente d'ouvrir l'image avec son chemin spécifié
    except Exception as e:  # Si une erreur survient lors de l'ouverture de l'image
        print(f"Impossible de charger l'image {image_path}: {e}")  # Affiche un message d'erreur
        return  # Arrête l'exécution de la fonction si l'image ne peut pas être ouverte
    
    ascii_art = convert_image_to_ascii(image, new_width)  # Convertit l'image en art ASCII
    print(ascii_art)  # Affiche l'art ASCII dans le terminal

    # Optionnel : Enregistrer l'ASCII art dans un fichier texte
    with open("ascii_art.txt", "w") as f:  # Ouvre un fichier en mode écriture
        f.write(ascii_art)  # Écrit l'art ASCII dans le fichier

if __name__ == "__main__":
    main("nom_photo.png", new_width=100)  # Exécute la fonction principale avec le chemin de l'image et la largeur souhaitée
