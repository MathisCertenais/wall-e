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
        self.pos_x = ipos_x 
        self.pos_y = ipos_y
        self.path = ipath
        
    def get_point(self):
        return self.point
    
    def get_position(self):
        return (self.pos_x,self.pos_y)
    
    def get_name(self):
        return self.name

    def get_path():
        return path
    
    
        
    
    
    