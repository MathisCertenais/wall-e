from objet_element.bijoux import *
from objet_element.aspirateur import *
from objet_element.poussiere import *

from ui.interface import *


bijoux = Bijoux(1,3)
aspirateur = Aspirateur(2,3)
poussiere = Poussiere(1,2)

print("nom de l'objet' :" + poussiere.get_name())
createMatrix(4, 3, root)
insertElement(poussiere, root)
insertElement(aspirateur, root)

# Affichage de la fenêtre
root.mainloop()