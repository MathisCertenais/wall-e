import threading
import time
from Tree.tree_arbre import Arbre

class ThreadRobot(threading.Thread):
    def __init__(self, queue_elements, TI, x=2, y=4):
        #Init thread sup
        threading.Thread.__init__(self)
        self.x, self.y = x, y
        self.image_instant_T = None
        self.arbre = None
        self.TI = TI
        pass

    # Capture l'environnement à l'instant T. Capteur
    def capturer(self):
        self.image_instant_T = self.TI.photoshoot_env()
        pass

    def creerArbre(self):
        self.arbre = Arbre(self.x, self.y, self.image_instant_T)

    def choisir_plan(self):
        pass


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

            #print("Breadth_first: ")
            #print(self.arbre.Breadth_first())
            #print("Breadth_first finish")
            #print(self.arbre.getPlan())
            
            #GreadySearch
            print("GreadySearcht: ")
            self.arbre.Gready_search(self.x,self.y)
            print("GreadySearcht finish")
            print(self.arbre.getPlan())
            #JustDoIt()


            time.sleep(5)
            pass
            

    
