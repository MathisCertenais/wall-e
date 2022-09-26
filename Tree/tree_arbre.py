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
        

    def construction_arbre(self,x,y):
        if (x >= 0 and x < self.max_x and y >= 0 and y < self.max_y):
            tuple_pos = [str(x),str(y)]
            tuple_pos_string = ','.join(tuple_pos)
            if (tuple_pos_string in self.memory_map):
                return self.memory_map[tuple_pos_string]
            else:
                self.memory_map[tuple_pos_string] = Noeud(self.tab.get_value(x, y))
                self.memory_map[tuple_pos_string].setNoeudN(self.construction_arbre(x, y+1))
                self.memory_map[tuple_pos_string].setNoeudS(self.construction_arbre(x, y-1))
                self.memory_map[tuple_pos_string].setNoeudE(self.construction_arbre(x+1, y))
                self.memory_map[tuple_pos_string].setNoeudW(self.construction_arbre(x-1, y))
                return self.memory_map[tuple_pos_string]
        else:
            return None

    def clean_plan(self):
        self.plan = []

    def getPlan(self):
        return self.plan

    def Depth_first_begin(self):
        self.Depth_first(self.racine)

    # Le sens choisi pour l'algo est Nord, Sud, Est et Ouest.
    def Depth_first(self, noeud):
        if noeud is not None:
            value = noeud.get_obj()
            if 1 == 0:
                self.plan.append("aspirer")
                return True
            else:
                if self.Depth_first(noeud.getNoeudN()):
                    self.plan.append("haut")
                    return True
                elif self.Depth_first(noeud.getNoeudS()):
                    self.plan.append("descend")
                    return True
                elif self.Depth_first(noeud.getNoeudE()):
                    self.plan.append("droite")
                    return True
                elif self.Depth_first(noeud.getNoeudW()):
                    self.plan.append("gauche")
                    return True
                else:
                    return False

            pass
        else:
            return False

    def parcourir(self):
        print(self.memory_map)
        
            
        