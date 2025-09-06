import cv2

# Charger le classificateur Haar Cascade pour la détection des visages
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Ouvrir la webcam (0 signifie la webcam par défaut)
cap = cv2.VideoCapture(1)

while True:
		# Lire une image à partir de la webcam
		ret, frame = cap.read()
		
		# Si la capture a échoué, arrêter la boucle
		if not ret:
				print("Échec de la capture vidéo.")
				break
		
		# Convertir l'image en niveaux de gris
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Détecter les visages dans l'image
		faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

		# Dessiner des rectangles autour des visages détectés
		for (x, y, w, h) in faces:
				cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

		# Afficher l'image avec les visages détectés
		cv2.imshow('Webcam Face Detection', frame)

		# Quitter avec la touche 'q'
		if cv2.waitKey(1) & 0xFF == ord('q'):
				break

# Libérer la caméra et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()
