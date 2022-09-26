#import numpy as np
#import pandas as pd
import sys
import copy
# Librairie pour les fenêtres
import tkinter
from tkinter import *
# Librairie pour les images
from PIL import Image, ImageTk

from objet_element.objet_scene import *

# Classe du tableau 3d qui contiendra les Objets
class My3DArray():
    # Initilialisation
    def __init__(self, x=5, y=5):
        # Creation d'un Arrays 3d
        self.x, self.y = x,y
        self.tab = [[ [] for col in range(x)] for row in range(y)]

    # Mise a jour de la taille du tableau
    def updateLenght(self, index, columns):
        self.tab = [[ [] for col in range(index)] for row in range(columns)]

    # Mise a jour des éléments du tableau
    def updateElement(self, Objet : Objet_scene):
        self.tab[Objet.get_position()[0]][Objet.get_position()[1]].append(Objet)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_value(self, x, y):
        return self.tab[x][y]


    # Fonction toString pour afficher le contenu du tableau 3d
    def get3DArray(self):
        return self.tab

    # def __str__(self):
    #     return print(self.tab)




class ThreadInterface():
    def __init__(self, queue_elements,x=5,y=5):
        # Création d'une fenêtre d'affichage
        self.root=Tk()
        # Personnalisation de la fenêtre
        self.root.title("Manoir de Wall-E")
        self.root.geometry("1080x720")
        self.root.minsize(520, 400)
        
        # Créer la matrice
        self.createMatrix(x,y)

        # Initialisation du tableau 3d
        self.array3D = My3DArray()

        # Les queues qui sont nécessaires au worker
        self.queue_elements = queue_elements



    # Fonctions lancés par thread.start et qui tournera en boucle
    def run(self):
        self.root.update()
        while True:
            if not self.queue_elements.empty():
                self.insertElement(self.queue_elements.get_nowait())
            self.root.update()


    # Fonction qui permet de générer le manoir, avec comme paramètre le nombre de ligne et de colonne de la matrice, et la fenêtre d'affichage
    def createMatrix(self, index, columns):

        # Initialisation des points de coordonnées
        i = 0
        j = 0
        # Création des lignes horizontales
        for x in range(index+1):
            verticale_line = Frame(self.root, bg='blue', height=1,width=columns*100)
            verticale_line.place(x=0, y=j)
            j += 100 

        # Création des lignes verticales
        for x in range(columns+1):
            verticale_line = Frame(self.root, bg='blue', height=index*100,width=1)
            verticale_line.place(x=i, y=0)
            i += 100 
        
        # Centrer la matrice

        return 

    # Fonction qui permet d'inserer un element, c'est a dire un robot, une poussiere ou un bijoux dans le manoir, 
    # avec comme paramètre l'objet qui correspond a l'élément à ajouter, et la fenêtre d'affichage
    def insertElement(self,Objet_scene):
        
        # Deplacement de l'objet s'il s'agit d'un robot
        if Objet_scene.get_name() == 'aspirateur':
            # Suppression de l'image du robot sur l'interface
            # Suppression de l'objet robot dans le tableau 3d
            # Ajout de l'objet robot au nouvel emplacement dans le tableau 3d
            self.array3D.updateElement(Objet_scene)

        # Ajout de l'objet s'il s'agit d'une poussiere ou d'un bijoux
        elif Objet_scene.get_name() == 'poussiere':
            self.array3D.updateElement(Objet_scene)

        elif Objet_scene.get_name() == 'bijoux':
            self.array3D.updateElement(Objet_scene)


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

    # Retourne une image de l'environnement à l'instant T
    def photoshoot_env(self):
        return copy.deepcopy(self.array3D)

    # Fonction qui permet d'aspirer un element, c'est a dire une poussiere ou un bijoux dans le manoir, 
    # avec comme paramètre l'objet qui correspond a l'élément à ajouter, et la fenêtre d'affichage
    def aspire(self, Object, root):
        return






