# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:55:45 2022

@author: aboug
"""

from objet_scene import Objet_scene

class Aspirateur(Objet_scene):
    
    def __init__(self, ipos_x, ipos_y):
        super().__init__(0, "aspirateur", ipos_x, ipos_y, "/my/path")