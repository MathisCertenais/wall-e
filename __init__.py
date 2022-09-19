from objet_element.bijoux import *
from ui.interface import *

print ("test des classes")

#♣intanciation
bijoux = Bijoux(1,3)

print("nom de l'objet' :" + bijoux.get_name())
print ("chemin  de l'image " + bijoux.get_path())
print (" position : " + "(" + str(bijoux.get_position()[0]) + "," + str(bijoux.get_position()[1]) +")" )

createMatrix(5, 5, root)
insertElement(bijoux, root)
# Affichage de la fenêtre
root.mainloop()