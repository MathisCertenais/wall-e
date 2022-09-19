import numpy as np
import pandas as pd
import sys
# Librairie pour les fenêtres
import tkinter
from tkinter import *
# Librairie pour les images
from PIL import Image, ImageTk




# Création d'une fenêtre d'affichage
root=Tk()
# Personnalisation de la fenêtre
root.title("Manoir de Wall-E")
root.geometry("1080x720")
root.minsize(520, 400)

# Fonction qui permet de générer le manoir, avec comme paramètre le nombre de ligne et de colonne de la matrice, et la fenêtre d'affichage
def createMatrix(index, columns, root):

    # Initialisation des points de coordonnées
    i = 0
    j = 0
    # Création des lignes horizontales
    for x in range(index+1):
        verticale_line = Frame(root, bg='blue', height=1,width=columns*100)
        verticale_line.place(x=0, y=j)
        j += 100 

    # Création des lignes verticales
    for x in range(columns+1):
        verticale_line = Frame(root, bg='blue', height=index*100,width=1)
        verticale_line.place(x=i, y=0)
        i += 100 
    
    # Centrer la matrice

    return 

# Fonction qui permet d'inserer un element, c'est a dire un robot, une poussiere ou un bijoux dans le manoir, 
# avec comme paramètre l'objet qui correspond a l'élément à ajouter, et la fenêtre d'affichage
def insertElement(Object, root):

    # Creation d'un objet photo-image de l'image de l'élément concerné
    image = Image.open(Object.get_path())

    # Redimensionnement de l'image
    resized_image= image.resize((95,95), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    label = tkinter.Label(image=new_image)
    label.image = new_image
    # Position de l'image
    label.place(x=Object.get_position()[0], y=Object.get_position()[1])
    return

# Fonction qui permet d'aspirer un element, c'est a dire une poussiere ou un bijoux dans le manoir, 
# avec comme paramètre l'objet qui correspond a l'élément à ajouter, et la fenêtre d'affichage
def aspire(Object, root):
    return



