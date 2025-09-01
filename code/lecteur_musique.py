import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Lecteur de Musique")
        self.root.geometry("400x150")

        self.current_song = None

        pygame.mixer.init()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Aucune chanson sélectionnée", font=("Helvetica", 12))
        self.label.pack(pady=20)

        self.select_button = tk.Button(self.root, text="Sélectionner une chanson", command=self.select_song)
        self.select_button.pack()

        self.play_button = tk.Button(self.root, text="Lecture", command=self.play_song, state=tk.DISABLED)
        self.play_button.pack()

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_song, state=tk.DISABLED)
        self.pause_button.pack()

        self.stop_button = tk.Button(self.root, text="Arrêter", command=self.stop_song, state=tk.DISABLED)
        self.stop_button.pack()

    def select_song(self):
        self.current_song = filedialog.askopenfilename(filetypes=[("Fichiers MP3", "*.mp3")])
        if self.current_song:
            self.label.config(text=f"Chanson sélectionnée : {self.current_song}")
            self.play_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)

    def play_song(self):
        if self.current_song:
            pygame.mixer.music.load(self.current_song)
            pygame.mixer.music.play()

    def pause_song(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop_song(self):
        pygame.mixer.music.stop()
        self.label.config(text="Aucune chanson sélectionnée")
        self.play_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)
        self.current_song = None

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
