from objet_element.objet_scene import *
from objet_element.bijoux import *
from objet_element.aspirateur import *
from objet_element.poussiere import *
from ui.interface import *


bijoux = Bijoux(1,3)
aspirateur = Aspirateur(2,3)
poussiere = Poussiere(1,2)
'''
self = [[[Objet_scene for col in range(3)] for row in range(5)] for row in range(5)]
self[1][0][0] = 1
print("qqqqq"+str(self))
'''

createMatrix(5, 5, root)
insertElement(poussiere, root)
insertElement(aspirateur, root)


# Affichage de la fenêtre
root.mainloop()