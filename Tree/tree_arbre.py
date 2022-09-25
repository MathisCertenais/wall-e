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
                
    def parcourir(self):
        print(self.memory_map)
        
            
        