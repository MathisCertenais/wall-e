# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:48:59 2022

@author: aboug
"""
from Tree.tree_noeud import Noeud



class Arbre : 
    def __init__(self,pos_x,pos_y,itab):
        
        self.pos_x, self.pos_y = pos_x, pos_y
        self.tab = itab #tableau 3d en mémoire
        self.max_x, self.max_y = self.tab.get_x(), self.tab.get_y()
        self.memory_map = {}

        self.racine = self.construction_arbre(self.pos_x, self.pos_y)

        self.plan = []
        self.memory_map_recherche = {}

        self.frontiere = []
        

    def construction_arbre(self,x,y):
        if (x >= 0 and x < self.max_x and y >= 0 and y < self.max_y):
            tuple_pos = [str(x),str(y)]
            tuple_pos_string = ','.join(tuple_pos)
            if (tuple_pos_string in self.memory_map):
                return self.memory_map[tuple_pos_string]
            else:
                self.memory_map[tuple_pos_string] = Noeud(self.tab.get_value(x, y), x, y)
                self.memory_map[tuple_pos_string].setNoeudN(self.construction_arbre(x, y-1))
                self.memory_map[tuple_pos_string].setNoeudS(self.construction_arbre(x, y+1))
                self.memory_map[tuple_pos_string].setNoeudE(self.construction_arbre(x+1, y))
                self.memory_map[tuple_pos_string].setNoeudW(self.construction_arbre(x-1, y))
                return self.memory_map[tuple_pos_string]
        else:
            return None

    def clean_plan(self):
        self.plan = []
        self.memory_map_recherche = {}

    def getPlan(self):
        return self.plan

    def poussiereIn(self, liste):
        print("value from x,y: ", liste)
        for element in liste:
            if element.get_name() == "poussiere":
                return True
        return False

    def Depth_first_begin(self):
        self.clean_plan()
        self.Depth_first(self.racine)

    # Le sens choisi pour l'algo est Nord, Sud, Est et Ouest.
    def Depth_first(self, noeud):
        if noeud is not None:
            key = str(noeud.get_x())+","+str(noeud.get_y())
            if key in self.memory_map_recherche:
                return False
            value = noeud.get_obj()
            if self.poussiereIn(value):
                self.plan.insert(0,"aspirer")
                return True
            else:
                self.memory_map_recherche[key] = noeud
                if self.Depth_first(noeud.getNoeudN()):
                    self.plan.insert(0,"haut")
                    return True
                elif self.Depth_first(noeud.getNoeudS()):
                    self.plan.insert(0, "descend")
                    return True
                elif self.Depth_first(noeud.getNoeudE()):
                    self.plan.insert(0,"droite")
                    return True
                elif self.Depth_first(noeud.getNoeudW()):
                    self.plan.insert(0, "gauche")
                    return True
                else:
                    return False

            pass
        else:
            return False


    #Recherche en largeur
    def Breadth_first(self):
        self.clean_plan()


    def Breadth_first_frontiere(self, noeud):
        if noeud.getNoeudN() is not None:
            valeur = noeud.getNoeudN().get_obj()
            if self.poussiereIn(valeur):
                return True
            else:
                self.frontiere.append(noeud)

        if noeud.getNoeudS() is not None:
            valeur = noeud.getNoeudS().get_obj()
            if self.poussiereIn(valeur):
                return True
            else:
                self.frontiere.append(noeud)

        if noeud.getNoeudE() is not None:
            valeur = noeud.getNoeudE().get_obj()
            if self.poussiereIn(valeur):
                return True
            else:
                self.frontiere.append(noeud)

        if noeud.getNoeudW() is not None:
            valeur = noeud.getNoeudW().get_obj()
            if self.poussiereIn(valeur):
                return True
            else:
                self.frontiere.append(noeud)
        
        return False
        


    def parcourir(self):
        print(self.memory_map)
        
            
        