import numpy as np
import pandas as pd
import sys
# Librairie pour les fenêtres
import tkinter
from tkinter import *
# Librairie pour les images
from PIL import Image, ImageTk

from objet_element.objet_scene import *


# Création d'une fenêtre d'affichage
root=Tk()
# Personnalisation de la fenêtre
root.title("Manoir de Wall-E")
root.geometry("1080x720")
root.minsize(520, 400)

# Classe du tableau 3d qui contiendra les Objets
class My3DArray():
    tab = [[ [Objet_scene for col in range(3)] for col in range(1)] for row in range(1)]
    # Initilialisation
    def __init__(self):
        # Creation d'un Arrays 3d
        self.tab = [[ [Objet_scene for col in range(3)] for col in range(1)] for row in range(1)]

    # Mise a jour de la taille du tableau
    def updateLenght(self, index, columns):
        self.tab = [[ [Objet_scene for col in range(3)] for col in range(index)] for row in range(columns)]

    # Mise a jour des éléments du tableau
    def updateElement(self, Objet : Objet_scene):
        self.tab[Objet.get_position()[0]][Objet.get_position()[1]][self.checkElement(Objet)] = Objet

    # Observer les elements présent dans la troisieme dimension, en renvoyant l'indice où insérer celui-ci
    def checkElement(self, Objet : Objet_scene):
        # Renvoyer l'indice 0 s'il s'agit d'un poussiere
        if (Objet.get_name() == 'poussiere'):
            return 0
        # Renvoyer l'indice 1 s'il s'agit d'un bijoux
        if (Objet.get_name() == 'bijoux'):
            return 1
        # Renvoyer l'indice 2 s'il s'agit d'un robot
        return 2


    # Fonction toString pour afficher le contenu du tableau 3d
    def get3DArray(self):
        return self.tab

    def __str__(self):
        return print(self.tab)

# Initialisation du tableau 3d
array3D = My3DArray()

# Fonction qui permet de générer le manoir, avec comme paramètre le nombre de ligne et de colonne de la matrice, et la fenêtre d'affichage
def createMatrix(index, columns, root):

    # Initialisation du tableau 3d
    array3D.updateLenght(index,columns)

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
def insertElement(Objet_scene, root):
    
    # Deplacement de l'objet s'il s'agit d'un robot
    if Objet_scene.get_name() == 'aspirateur':
        # Suppression de l'image du robot sur l'interface
        # Suppression de l'objet robot dans le tableau 3d
        # Ajout de l'objet robot au nouvel emplacement dans le tableau 3d
        array3D.updateElement(Objet_scene)

    # Ajout de l'objet s'il s'agit d'une poussiere ou d'un bijoux
    elif Objet_scene.get_name() == 'poussiere':
        array3D.updateElement(Objet_scene)

    elif Objet_scene.get_name() == 'bijoux':
        array3D.updateElement(Objet_scene)


    # Creation d'un objet photo-image de l'image de l'élément concerné
    image = Image.open(Objet_scene.get_path())

    # Redimensionnement de l'image
    resized_image= image.resize((95,95), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    label = tkinter.Label(image=new_image)
    label.image = new_image
    # Position de l'image
    label.place(x=Objet_scene.get_position_pixel()[0], y=Objet_scene.get_position_pixel()[1])
    return

# Fonction qui permet d'aspirer un element, c'est a dire une poussiere ou un bijoux dans le manoir, 
# avec comme paramètre l'objet qui correspond a l'élément à ajouter, et la fenêtre d'affichage
def aspire(Object, root):

    return



