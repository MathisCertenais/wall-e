import threading
import time
from Tree.tree_arbre import Arbre
from objet_element.aspirateur import Aspirateur

class ThreadRobot(threading.Thread):
    def __init__(self, queue_elements, TI, x=0, y=0):
        #Init thread sup
        threading.Thread.__init__(self)
        self.x, self.y = x, y
        self.image_instant_T = None
        self.arbre = None
        self.queue_elements = queue_elements
        self.TI = TI
        self.aspirateur = Aspirateur(0,0)
        pass

    # Capture l'environnement à l'instant T. Capteur
    def capturer(self):
        self.image_instant_T = self.TI.photoshoot_env()
        pass

    def creerArbre(self):
        self.arbre = Arbre(self.aspirateur.get_position()[0], self.aspirateur.get_position()[1], self.image_instant_T)

    def JustDoIt(self):
        for action in self.arbre.getPlan():
            pos_list = self.aspirateur.get_position()
            print("position robot: ", pos_list)
            x, y = pos_list[0], pos_list[1]
            if action == "descend":
                self.aspirateur.set_position(x,y+1)
            elif action == "haut":
                self.aspirateur.set_position(x,y-1)
            elif action == "droite":
                self.aspirateur.set_position(x+1,y)
            elif action == "gauche":
                self.aspirateur.set_position(x-1,y)
            elif action == "aspirer":
                pass
            elif action == "ramasser":
                pass
            self.queue_elements.put(self.aspirateur)
            time.sleep(1)


    def run(self):
        #Boucle infine d'action du petit robot
        while True:
            #Capteur
            self.capturer()
            print(self.image_instant_T)

            #Créer arbre
            self.creerArbre()
            print(self.arbre)

            #Exploration
            self.arbre.clean_plan()
            # self.arbre.Depth_first_begin()
            # print(self.arbre.getPlan())

            print("Breadth_first: ")
            print(self.arbre.Breadth_first())
            print("Breadth_first finish")
            print(self.arbre.getPlan())

            #JustDoIt()
            self.JustDoIt()

            time.sleep(5)
            pass
            

    
