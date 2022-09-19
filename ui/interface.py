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

# Classe du tableau 3d qui contiendra les Objets
class My3DArray():
    # Initilialisation
    def __init__(self):
        self = []
    # Mise a jour de la taille du tableau
    def update(self, index, columns):
        self = [[ ['0' for col in range(1)] for col in range(index)] for row in range(columns)]

# Initialisation du tableau 3d
array3D = My3DArray()

# Fonction qui permet de générer le manoir, avec comme paramètre le nombre de ligne et de colonne de la matrice, et la fenêtre d'affichage
def createMatrix(index, columns, root):
    

    # Edition de la taille du tableau 3d
    array3D.update(index,columns)

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
    
    # Deplacement de l'objet s'il s'agit d'un robot
    if Object.get_name() == 'aspirateur':
        # Suppression de l'image du robot sur l'interface
        # Suppression de l'objet robot dans le tableau 3d
        # Ajout de l'objet robot au nouvel emplacement dans le tableau 3d
        array3D.update(Object.get_position()[0], Object.get_position()[1])


    # Ajout de l'objet s'il s'agit d'une poussiere ou d'un bijoux
    else:
        array3D.update(Object.get_position()[0], Object.get_position()[1])
        print(array3D)
    
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



