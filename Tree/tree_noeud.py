# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:32:03 2022

@author: aboug
"""

class Noeud : 
    def __init__(self,obj,arbreN=None,arbreS=None, arbreW=None, arbreE=None):
        self.obj = obj #liste des objet poussière, bijoux ou robot
        self.arbreN = arbreN
        self.arbreS = arbreS
        self.arbreW = arbreW
        self.arbreE = arbreE
    
    def setNoeudN(self, noeud):
        self.arbreN = noeud

    def setNoeudS(self, noeud):
        self.arbreS = noeud

    def setNoeudE(self, noeud):
        self.arbreE = noeud

    def setNoeudW(self, noeud):
        self.arbreW = noeud

    def get_obj(self):
        return self.obj
    
    
        
    
    
    