# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:48:59 2022

@author: aboug
"""
from objet_element.objet_scene import Objet_scene

class Poussiere(Objet_scene):
    
    def __init__(self, ipos_x, ipos_y):
        #super().__init__(5, "poussiere", ipos_x, ipos_y, "./ui/pictures/poussiere.png")
        super().__init__(5, "poussiere", ipos_x, ipos_y, "C:\\Users\\Mathis\\Documents\\code\\wall-e\\ui\\pictures\\poussiere.png")
   

