import random

def guessing_game():
    # Affichage des messages d'introduction
    print("Bienvenue dans le jeu de devinettes !")
    print("Je pense à un nombre entre 1 et 100. Devine-le !")

    # Choisir un nombre aléatoire entre 1 et 100 que l'utilisateur doit deviner
    number_to_guess = random.randint(1, 100)
    
    # Variable pour compter le nombre de tentatives de l'utilisateur
    attempts = 0

    # Boucle principale du jeu
    while True:
        try:
            # Demander à l'utilisateur de deviner le nombre
            guess = int(input("Entrez votre devinette: "))
            
            # Incrémenter le nombre de tentatives à chaque essai
            attempts += 1
            
            # Vérification du nombre proposé par l'utilisateur
            if guess < number_to_guess:
                print("Trop bas !")  # Si le nombre deviné est trop petit
            elif guess > number_to_guess:
                print("Trop haut !")  # Si le nombre deviné est trop grand
            else:
                # Si l'utilisateur trouve la bonne réponse
                print(f"Félicitations ! Vous avez deviné le nombre en {attempts} tentatives.")
                break  # Terminer le jeu si le nombre est trouvé
        except ValueError:
            # Si l'utilisateur entre autre chose qu'un nombre, afficher un message d'erreur
            print("Veuillez entrer un nombre valide.")

# Appeler la fonction pour lancer le jeu
guessing_game()
