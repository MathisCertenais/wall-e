import networkx as nx

import numpy as np
from matplotlib import pyplot as plt
import random



# matrice image
col, row = 5,5
tab_scene = np.zeros((5, 5))
tab_scene

#Ajout des noeuds
# Affichage en mode graph

#Position
x = random.randint(1, 4)
y = random.randint(1, 4)
tab_scene[x,y] = 1

#Génération de poussière
for i in range(0, 3):
    a = random.randint(1, 4)
    b = random.randint(1, 4)
    tab_scene[a,b] = -1
    pass

#Génération de bijoux
for i in range(0, 3):
    a = random.randint(1, 4)
    b = random.randint(1, 4)
    if(tab_scene[a,b] != 0) :
        tab_scene[a,b] = -3
    else:
        tab_scene[a,b] = -2
    pass


