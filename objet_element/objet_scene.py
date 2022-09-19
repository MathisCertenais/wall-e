# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:32:03 2022

@author: aboug
"""

class Objet_scene:
    
    point = 0
    name = ""
    pos_x = 0
    pos_y = 0
    path = ""
    
    def __init__(self,ipoint, iname, ipos_x, ipos_y, ipath):
        self.point = ipoint
        self.name = iname
        self.pos_x = 101*ipos_x 
        self.pos_y = 101*ipos_y
        self.path = ipath
        
    def get_point(self):
        return self.point
    
    def get_position(self):
        doublet = 2*[0]
        doublet[0] = self.pos_x
        doublet[1] = self.pos_y
        return doublet
    
    def get_name(self):
        return self.name

    def get_path(self):
        return self.path
    
    
        
    
    
    