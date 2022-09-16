# Librairie pour les fenêtres
from tkinter import *

# Création d'une fenêtre
window = Tk()
# Personnalisation
window.title("Manoir de Wall-E")
window.geometry("1080x720")
window.minsize(520, 400)
# Génération du titre
window_label = Label(window, text="Affichage en temps réel du manoir, \ndu robot, des poussières et des bijoux.", font=("Courrier", 25))
# Placement en haut
window_label.pack(expand=NO)

# Affichage de la fenêtre
window.mainloop()