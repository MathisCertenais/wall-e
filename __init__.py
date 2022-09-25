from objet_element.objet_scene import *
from objet_element.bijoux import *
from objet_element.aspirateur import *
from objet_element.poussiere import *
from ui.interface import *
from Tree.tree_arbre import Arbre



'''
self = [[[Objet_scene for col in range(3)] for row in range(5)] for row in range(5)]
self[1][0][0] = 1
print("qqqqq"+str(self))
'''

#createMatrix(5, 5, root)
#insertElement(poussiere, root)
#insertElement(aspirateur, root)
#insertElement(bijoux, root)


# Affichage de la fenêtre
#root.mainloop()

# Création d'un arbre

print("Start")
matrice = My3DArray(3,3)
print("Arbre")
arbre = Arbre(0,0,matrice)
print("Affichage")
arbre.parcourir()
