#Imports
import threading
import time, random

from objet_element.bijoux import Bijoux
from objet_element.poussiere import Poussiere

#Class hérite Thread
class ThreadEnvironnement(threading.Thread):
    #Constructeur
    def __init__(self, queue_elements, x=5, y=5):
        #Init thread sup
        threading.Thread.__init__(self)

        #Obtenir queue sync
        self.queue_elements = queue_elements

        #Obtenir x et y de la matrice
        self.x, self.y = x, y

    #Boucle infinies génère éléments
    def run(self):
        while True:
            valeur_rand = random.randint(0,1)
            val_x = random.randint(0, self.x-1)
            val_y = random.randint(0, self.y-1)
            print("ValRand: ",valeur_rand," Valx: ",val_x," Valy: ",val_y)
            if valeur_rand == 0:
                #Bijoux
                self.queue_elements.put(Bijoux(val_x, val_y))
                pass
            elif valeur_rand == 1:
                #Poussiere
                self.queue_elements.put(Poussiere(val_x, val_y))
                pass
            else:
                #Cas où on ne fait rien
                pass


            #valeur_sleep = random.randint(0.1, 0.2)
            #Between 0 and 1 float values   
            valeur_sleep = random.uniform(0.2, 0.4)
            print("Sleep: ",valeur_sleep," secondes")
            time.sleep(valeur_sleep)
            



