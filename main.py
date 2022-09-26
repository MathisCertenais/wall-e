# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:54:46 2022

@author: unknown
"""

#Imports
from queue import Queue
from objet_element.bijoux import *
from objet_element.poussiere import *
from Tree.tree_arbre import *
from Tree.tree_noeud import *



# Imports Threads
from ui.interface import ThreadInterface
from objet_element.main import ThreadEnvironnement
from robot.Robot import ThreadRobot

bijoux = Bijoux(1,3)
poussiere = Poussiere(2,3)
poussiere2 = Poussiere(3,4)
poussiere3 = Poussiere(1,2)
#Créer sync queues
queue_elements = Queue()
queue_elements.put(bijoux)
queue_elements.put(poussiere)
queue_elements.put(poussiere2)
queue_elements.put(poussiere3)
#Créer thread objets
TI = ThreadInterface(queue_elements)
TE = ThreadEnvironnement(queue_elements)
TR = ThreadRobot(queue_elements, TI)



#Run Thread objects
TE.start()
TR.start()
TI.run()

#And love the life because I said it