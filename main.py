# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:54:46 2022

@author: unknown
"""

#Imports
from queue import Queue
from objet_element.bijoux import *

# Imports Threads
from ui.interface import ThreadInterface
from objet_element.main import ThreadEnvironnement

bijoux = Bijoux(1,3)
#Créer sync queues
queue_elements = Queue()
queue_elements.put(bijoux)

#Créer thread objets
TE = ThreadEnvironnement(queue_elements)
TI = ThreadInterface(queue_elements)


#Run Thread objects
TE.start()
TI.run()

#And love the life because I said it