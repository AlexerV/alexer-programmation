from PIL import Image

# Liste de caractères ASCII par ordre de luminosité
ASCII_CHARS = "@%#*+=-:. "

def scale_image(image, new_width=100):
    """Redimensionner l'image en fonction de la largeur donnée tout en conservant le ratio."""
    (original_width, original_height) = image.size
    aspect_ratio = original_height / original_width
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    """Convertir l'image en niveaux de gris."""
    return image.convert("L")

def map_pixels_to_ascii(image, range_width=25):
    """Convertir les pixels en caractères ASCII."""
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // range_width]
    return ascii_str

def convert_image_to_ascii(image, new_width=100):
    """Convertir une image en art ASCII."""
    image = scale_image(image, new_width)
    image = convert_to_grayscale(image)

    ascii_str = map_pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    
    return ascii_img

def main(image_path, new_width=100):
    """Charger l'image et la convertir en ASCII."""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Impossible de charger l'image {image_path}: {e}")
        return
    
    ascii_art = convert_image_to_ascii(image, new_width)
    print(ascii_art)

    # Optionnel : Enregistrer l'ASCII art dans un fichier texte
    with open("ascii_art.txt", "w") as f:
        f.write(ascii_art)

if __name__ == "__main__":
    main("nom_photo.png", new_width=100)
