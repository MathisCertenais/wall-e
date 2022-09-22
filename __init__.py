from objet_element.objet_scene import *
from objet_element.bijoux import *
from objet_element.aspirateur import *
from objet_element.poussiere import *
from ui.interface import *
from Tree.tree_arbre import Arbre


bijoux = Bijoux(1,3)
aspirateur = Aspirateur(2,3)
poussiere = Poussiere(1,2)
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
tab = [[1,2,3,4,5],[6,7,8,9,10]]
m_arbre = Arbre(0, 0, tab)
#m_arbre.show()