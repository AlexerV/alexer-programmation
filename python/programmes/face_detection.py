import cv2  # Importation de la bibliothèque OpenCV pour la capture vidéo et le traitement d'image

# Charger le classificateur Haar Cascade pour la détection des visages
# Haar Cascade est un modèle pré-entraîné utilisé pour la détection d'objets (ici les visages)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(1)  # Ouvrir la webcam (0 signifie la webcam par défaut, 1 pour une autre caméra si disponible)

while True:
    # Lire une image à partir de la webcam
    ret, frame = cap.read()  # capture d'une image de la webcam
    if not ret:  # Si la capture échoue (par exemple si la caméra n'est pas accessible)
        print("Échec de la capture vidéo.")  # Afficher un message d'erreur
        break  # Quitte la boucle si l'image n'a pas pu être lue
    
    # Convertir l'image en niveaux de gris (la détection de visages fonctionne mieux sur des images en niveaux de gris)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Conversion de l'image de BGR à Gris

    # Détecter les visages dans l'image (le classificateur Haar Cascade renvoie une liste de coordonnées de visages)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # scaleFactor: Paramètre pour la mise à l'échelle de l'image (utile pour les visages à différentes tailles)
    # minNeighbors: Paramètre pour la qualité de la détection (plus élevé = plus de visages détectés, mais moins de faux positifs)
    # minSize: Taille minimale des visages à détecter (par défaut, un visage trop petit ne sera pas détecté)

    # Dessiner des rectangles autour des visages détectés
    for (x, y, w, h) in faces:  # Parcours de chaque visage détecté
        # Dessine un rectangle autour du visage sur l'image (x, y) est le coin supérieur gauche, (x + w, y + h) le coin inférieur droit
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Rouge: (255, 0, 0), épaisseur du rectangle: 2

    # Afficher l'image avec les visages détectés dans une fenêtre nommée 'Webcam Face Detection'
    cv2.imshow('Webcam Face Detection', frame)

    # Vérifier si l'utilisateur appuie sur la touche 'q' pour quitter la boucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # Si 'q' est pressé, sortir de la boucle

# Libérer la caméra et fermer toutes les fenêtres ouvertes
cap.release()  # Libère la caméra pour la rendre disponible pour d'autres applications
cv2.destroyAllWindows()  # Ferme toutes les fenêtres OpenCV ouvertes
