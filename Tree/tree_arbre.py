# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:48:59 2022

@author: aboug
"""
from Tree.tree_feuille import Feuille
from Tree.tree_noeud import Noeud



class Arbre : 
    def __init__(self,pos_x,pos_y,itab):
        self.val = Noeud(itab[pos_x][pos_y])
        self.fils = Feuille()
        self.tab = itab #tableau 3d en mémoire
        self.construction_arbre(pos_x,pos_y,itab)
    
    def insert_fils(self, arbre_fils):
        self.fils.insert_noeud(arbre_fils)
        
    def get_val(self):
        return self.val.get_obj() #return la list d'objet
    
    def get_feuille(self):
        return self.fils.get_list ()
    
    def est_vide(arbre):
        return arbre is None
    
    def insert_obj(self,tab,i,j):
        rows = len(tab)
        cols = len(tab[0])
        fils = Feuille()
        while(0<=i<=cols & 0<=j<=rows):
            self.filsN = Arbre(i,j,tab)
                    #arbre_tmp = Arbre(i,j,tab)
                    #fils.insert_noeud(arbre_tmp)
        return fils #liste des fils à l'index (i,j)

                
    def verification_feuille(self,pere,feuille_lst):
        verite = True
        for i in (0,len(feuille_lst),1):
            if (feuille_lst[i] == pere):
                verite = False
        return verite
    
    def construction_arbre(self,pos_x,pos_y,itab):
        self.val = Noeud(itab[pos_x][pos_y]) #pere
        rows = len(itab)
        cols = len(itab[0])
        for i in (0,cols,1):
            for j in (0,rows,1):
                arbre_enfant = self.insert_obj(itab,i,j)
                if(self.verification_feuille(self.val,arbre_enfant)):
                    self.insert_fils(arbre_enfant)
                #debug
                #print("list_fille")
                #print(arbre_enfant.get_list())
                
    def show(self):
        while(self.est_vide() == False):
            N = str(self.get_val())
            F = str(self.get_feuille())
            print("N : " + N)
            print("-> " + F)
            
        