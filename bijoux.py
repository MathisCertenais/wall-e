# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:54:46 2022

@author: aboug
"""

from objet_scene import Objet_scene

class Bijoux(Objet_scene):
    
    def __init__(self, ipos_x, ipos_y):
        super().__init__(10, "bijout", ipos_x, ipos_y, "/my/path")