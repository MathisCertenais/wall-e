from objet_scene import Objet_scene
from bijoux import Bijoux
from poussiere import Poussiere
from aspirateur import Aspirateur

def main():
    print ("test des classes")
    
    #â™£intanciation
    bijoux = Bijoux(0,1)
    aspirateur = Aspirateur(0, 5)
    
    print("nom de l'objet' :" + bijoux.get_name())
    print ("chemin  de l'image " + bijoux.get_path())
    print (" position : " + "(" + str(bijoux.get_position()[0]) + "," + str(bijoux.get_position()[1]) +")" )
    
    
    
main()