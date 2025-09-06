import tkinter as tk
import random
import string
import pyperclip

# Fonction pour générer le mot de passe
def generate_password():
    # Récupérer les choix de l'utilisateur depuis l'interface
    length = int(entry_length.get())
    use_upper = var_upper.get()
    use_lower = var_lower.get()
    use_digits = var_digits.get()
    use_special = var_special.get()

    # Construction des caractères autorisés
    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    # Générer le mot de passe
    if chars:  # S'assurer qu'il y a des caractères valides
        password = ''.join(random.choice(chars) for _ in range(length))
        label_result.config(text=f"Mot de passe généré : {password}")
    else:
        label_result.config(text="Erreur : Aucune option sélectionnée!")

# Fonction pour copier le mot de passe dans le presse-papiers
def copy_to_clipboard():
    password = label_result.cget("text").replace("Mot de passe généré : ", "")
    if password:
        pyperclip.copy(password)  # Copier le mot de passe dans le presse-papiers
        label_copy_status.config(text="Mot de passe copié !")
    else:
        label_copy_status.config(text="Aucun mot de passe à copier.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Générateur de Mot de Passe")

# Label pour la longueur du mot de passe
label_length = tk.Label(root, text="Longueur du mot de passe:")
label_length.grid(row=0, column=0, padx=10, pady=10)

# Entrée pour la longueur du mot de passe
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)
entry_length.insert(0, "12")  # Valeur par défaut

# Cases à cocher pour les types de caractères à inclure
var_upper = tk.IntVar()
var_lower = tk.IntVar()
var_digits = tk.IntVar()
var_special = tk.IntVar()

check_upper = tk.Checkbutton(root, text="Majuscules", variable=var_upper)
check_upper.grid(row=1, column=0, padx=10, pady=5)

check_lower = tk.Checkbutton(root, text="Minuscules", variable=var_lower)
check_lower.grid(row=1, column=1, padx=10, pady=5)

check_digits = tk.Checkbutton(root, text="Chiffres", variable=var_digits)
check_digits.grid(row=2, column=0, padx=10, pady=5)

check_special = tk.Checkbutton(root, text="Caractères spéciaux", variable=var_special)
check_special.grid(row=2, column=1, padx=10, pady=5)

# Bouton pour générer le mot de passe
button_generate = tk.Button(root, text="Générer", command=generate_password)
button_generate.grid(row=3, column=0, columnspan=2, pady=10)

# Label pour afficher le résultat
label_result = tk.Label(root, text="Mot de passe généré : ", font=("Helvetica", 12))
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Bouton pour copier le mot de passe dans le presse-papiers
button_copy = tk.Button(root, text="Copier", command=copy_to_clipboard)
button_copy.grid(row=5, column=0, columnspan=2, pady=10)

# Label pour afficher l'état de copie
label_copy_status = tk.Label(root, text="", font=("Helvetica", 10))
label_copy_status.grid(row=6, column=0, columnspan=2, pady=5)

# Démarrer l'interface graphique
root.mainloop()
