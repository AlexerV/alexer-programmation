import tkinter as tk  # Importation de Tkinter pour l'interface graphique
from tkinter import filedialog  # Importation pour la boîte de dialogue de sélection de fichiers
import pygame  # Importation de Pygame pour la gestion de la lecture de musique

class MusicPlayer:
    def __init__(self, root):
        """Initialisation de l'application du lecteur de musique."""
        self.root = root  # La fenêtre principale Tkinter
        self.root.title("Lecteur de Musique")  # Titre de la fenêtre
        self.root.geometry("400x150")  # Taille de la fenêtre principale (largeur x hauteur)

        self.current_song = None  # Variable pour stocker le chemin de la chanson actuellement sélectionnée

        pygame.mixer.init()  # Initialisation du module pygame.mixer pour gérer le son

        self.create_widgets()  # Crée les éléments graphiques de l'interface

    def create_widgets(self):
        """Crée les widgets (éléments de l'interface graphique)."""
        self.label = tk.Label(self.root, text="Aucune chanson sélectionnée", font=("Helvetica", 12))  # Étiquette pour afficher l'état
        self.label.pack(pady=20)  # Ajoute l'étiquette à la fenêtre avec un espacement vertical

        self.select_button = tk.Button(self.root, text="Sélectionner une chanson", command=self.select_song)  # Bouton pour sélectionner une chanson
        self.select_button.pack()  # Ajoute le bouton à la fenêtre

        self.play_button = tk.Button(self.root, text="Lecture", command=self.play_song, state=tk.DISABLED)  # Bouton de lecture
        self.play_button.pack()  # Ajoute le bouton à la fenêtre

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_song, state=tk.DISABLED)  # Bouton de pause
        self.pause_button.pack()  # Ajoute le bouton à la fenêtre

        self.stop_button = tk.Button(self.root, text="Arrêter", command=self.stop_song, state=tk.DISABLED)  # Bouton d'arrêt
        self.stop_button.pack()  # Ajoute le bouton à la fenêtre

    def select_song(self):
        """Ouvre une boîte de dialogue pour sélectionner un fichier MP3."""
        self.current_song = filedialog.askopenfilename(filetypes=[("Fichiers MP3", "*.mp3")])  # Demande à l'utilisateur de sélectionner un fichier MP3
        if self.current_song:  # Si une chanson est sélectionnée
            self.label.config(text=f"Chanson sélectionnée : {self.current_song}")  # Affiche le nom de la chanson
            self.play_button.config(state=tk.NORMAL)  # Active le bouton de lecture
            self.pause_button.config(state=tk.NORMAL)  # Active le bouton de pause
            self.stop_button.config(state=tk.NORMAL)  # Active le bouton d'arrêt

    def play_song(self):
        """Joue la chanson sélectionnée."""
        if self.current_song:  # Si une chanson a été sélectionnée
            pygame.mixer.music.load(self.current_song)  # Charge la chanson dans pygame
            pygame.mixer.music.play()  # Démarre la lecture de la chanson

    def pause_song(self):
        """Met la chanson en pause."""
        if pygame.mixer.music.get_busy():  # Si une chanson est en train de jouer
            pygame.mixer.music.pause()  # Met la musique en pause

    def stop_song(self):
        """Arrête la lecture de la chanson et réinitialise l'interface."""
        pygame.mixer.music.stop()  # Arrête la musique en cours de lecture
        self.label.config(text="Aucune chanson sélectionnée")  # Réinitialise le texte du label
        self.play_button.config(state=tk.DISABLED)  # Désactive le bouton de lecture
        self.pause_button.config(state=tk.DISABLED)  # Désactive le bouton de pause
        self.stop_button.config(state=tk.DISABLED)  # Désactive le bouton d'arrêt
        self.current_song = None  # Réinitialise la chanson sélectionnée

# Bloc principal
if __name__ == "__main__":
    root = tk.Tk()  # Crée une instance de la fenêtre principale Tkinter
    app = MusicPlayer(root)  # Crée une instance de MusicPlayer en passant la fenêtre Tkinter
    root.mainloop()  # Lance la boucle principale de Tkinter, affichant la fenêtre et gérant les événements
