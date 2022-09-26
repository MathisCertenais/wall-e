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

# Liste de la 3e dimension de la matrice qui accueillera les Objets
objetDimension = list()
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

    def set_value(self, x, y, tab_value):
        self.tab[x][y] = tab_value

    # Retourner le nombre de poussières présent à l'index et la colonne entré en paramètre
    def getDustNumber(self, index, columns):
        # Mise a zero du compteur
        cpt = 0
        # Recuperation de liste contenant des Objets aux coordonnées récupérés en paramètre
        tab =  self.tab(index, columns)
        # Parcours du tableau pour récupérer le nombre de poussiere
        for x in tab:
            if (x.get_name() == 'poussiere'):
                cpt += 1

        return cpt

    # Retourner le nombre de bijoux présent à l'index et la colonne entré en paramètre
    def getJewelryNumber(self, index, columns):
        # Mise a zero du compteur
        cpt = 0
        # Recuperation de liste contenant des Objets aux coordonnées récupérés en paramètre
        tab =  self.tab(index, columns)
        # Parcours du tableau pour récupérer le nombre de bijoux
        for x in tab:
            if (x.get_name() == 'bijoux'):
                cpt += 1
                
        return cpt

    # Retourner le nombre de poussières présent à l'index et la colonne entré en paramètre
    def getDustNumber(self, index, columns):
        # Mise a zero du compteur
        cpt = 0
        # Recuperation de liste contenant des Objets aux coordonnées récupérés en paramètre
        tab =  self.tab(index, columns)
        # Parcours du tableau pour récupérer le nombre de poussiere
        for x in tab:
            if (x.get_name() == 'poussiere'):
                cpt += 1
                
        return cpt

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
        

        self.x, self.y = x, y
        # Créer la matrice
        self.createMatrix(x,y)

        # Initialisation du tableau 3d
        self.array3D = My3DArray(x, y)

        # Les queues qui sont nécessaires au worker
        self.queue_elements = queue_elements

        #score du robot
        self.score = 0



    # Fonctions lancés par thread.start et qui tournera en boucle
    def run(self):
        self.root.update()
        while True:
            if not self.queue_elements.empty():
                objet_queue = self.queue_elements.get_nowait()
                if objet_queue.get_name() =="aspirateur":
                    position_x, position_y = objet_queue.get_position()[0], objet_queue.get_position()[1]
                    for action in objet_queue.getAction():
                        if action == "aspirer":
                            for element in self.array3D.get_value(position_x, position_y):
                                if element.get_name() == "bijoux":
                                    self.score -= element.get_point()
                                else:
                                    self.score += element.get_point()
                            self.array3D.set_value(position_x, position_y, [])
                            pass
                        elif action == "ramasser":
                            new_liste = []
                            for element in self.array3D.get_value(position_x, position_y):
                                if element.get_name() == "bijoux":
                                    self.score += element.get_point()
                                else:
                                    new_liste.append(element)
                            self.array3D.set_value(position_x, position_y, new_liste)
                            pass
                        elif action == "bouger":
                            self.score -= 1
                self.insertElement(objet_queue)
                print("Score: ", self.score)
                self.createMatrix(self.x,self.y)
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






