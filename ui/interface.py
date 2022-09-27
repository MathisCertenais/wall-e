#import numpy as np
#import pandas as pd
import sys
# Librairie pour les fenêtres
import tkinter
from tkinter import *
from tkinter.ttk import *
# Librairie pour les images
from PIL import Image, ImageTk

from objet_element.objet_scene import *

objetDimension = []
# Classe du tableau 3d qui contiendra les Objets
class My3DArray():
    # Tableau 3d avec une liste qui représente la 3e dimension, et qui accueillera les Objets 
    tab = [[ [] for col in range(1)] for row in range(1)]
    # Initilialisation
    def __init__(self):
        # Creation d'un Arrays 3d
        self.tab = [[ [] for col in range(1)] for row in range(1)]

    # Mise a jour de la taille du tableau
    def updateLength(self, index, columns):
        self.tab = [[ [] for col in range(index)] for row in range(columns)]

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

    # Retourner le nombre de poussières et de bijoux présent à l'index et la colonne entré en paramètre
    def getElementNumber(self, index, columns):
        # Mise a zero du compteur
        doublet = 2*[0]
        # Recuperation de liste contenant des Objets aux coordonnées récupérés en paramètre
        tab =  self.tab(index, columns)
        # Parcours du tableau pour récupérer le nombre de poussieres et de bijoux
        for x in tab:
            if (x.get_name() == 'poussiere'):
                doublet[0] += 1

            elif (x.get_name() == 'bijoux'):
                doublet[1] += 1

        return doublet

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

    def __str__(self):
        return print(self.tab)




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
        k = 0
        l = 0

        # Création d'un gadget de toile
        canvas=Canvas(self.root, width=500, height=300)
        canvas.pack()

        # Création des lignes verticales
        for x in range(5+1):
            canvas.create_line(0, j, 5*100, j)
            j += 100 

        # Création des lignes horizontales
        for x in range(5+1):
            canvas.create_line(i, 0, i, 5*100)
            i += 100 

        # Génération de la trinité
        for x in range(5):
            for x in range(5):
                canvas.create_line(50+k, 60+l, 50+k, 100+l)
                canvas.create_line(0+k, 0+l, 50+k, 60+l, 100+k, 0+l, 0+k, 0+l)
                k +=100
            k = 0
            l += 100
        # Intégration du canvqs à la fenêtre principale et le rendre extensible.
        canvas.pack(fill = BOTH, expand = True)
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
            self.array3D.updateElement(Objet_scene)

        # Ajout de l'objet s'il s'agit d'une poussiere ou d'un bijoux
        elif Objet_scene.get_name() == 'poussiere':
            self.array3D.updateElement(Objet_scene)
            # Recuperation du nombre de poussiere dans la case concernée
            element = self.getElementNumber(Objet_scene.get_position()[0], Objet_scene.get_position()[1])[0]

        elif Objet_scene.get_name() == 'bijoux':
            # Recuperation du nombre de bijoux dans la case concernée
            element = self.getElementNumber(Objet_scene.get_position()[0], Objet_scene.get_position()[1])[1]

        # Creation d'un objet photo-image de l'image de l'élément concerné
        image = Image.open(Objet_scene.get_path())
        # Si y a deja cette image, ne pas lajouter
        
        # Couper l'image en 2 si y a un autre element


        # Redimensionnement de l'image
        resized_image= image.resize((95,95), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)
        label = tkinter.Label(image=new_image)
        label.image = new_image
        # Ajout du compteur
        element
        text = Label(self, text=element)
        text.place(x=Objet_scene.get_position_pixel()[0], y=Objet_scene.get_position_pixel()[1])

        # Position de l'image
        label.place(x=Objet_scene.get_position_pixel()[0], y=Objet_scene.get_position_pixel()[1])
        return

    # Fonction qui permet d'aspirer un element, c'est a dire une poussiere ou un bijoux dans le manoir, 
    # avec comme paramètre l'objet qui correspond a l'élément à ajouter, et la fenêtre d'affichage
    def aspire(self, Object, root):
        return






