# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:32:03 2022

@author: aboug
"""

class Noeud : 
    def __init__(self,obj, x, y,noeudN=None,noeudS=None, noeudW=None, noeudE=None):
        self.obj = obj #liste des objet poussière, bijoux ou robot
        self.x, self.y = x, y
        self.noeudN = noeudN
        self.noeudS = noeudS
        self.noeudW = noeudW
        self.noeudE = noeudE
    
    def setNoeudN(self, noeud):
        self.noeudN = noeud

    def setNoeudS(self, noeud):
        self.noeudS = noeud

    def setNoeudE(self, noeud):
        self.noeudE = noeud

    def setNoeudW(self, noeud):
        self.noeudW = noeud

    def getNoeudN(self):
        return self.noeudN

    def getNoeudS(self):
        return self.noeudS

    def getNoeudE(self):
        return self.noeudE

    def getNoeudW(self):
        return self.noeudW

    def get_obj(self):
        return self.obj

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    
        
    
    
    