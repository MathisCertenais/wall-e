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
            valeur_rand = random.randint(0,2)
            val_x = random.randint(0, self.x-3)
            val_y = random.randint(0, self.y-3)
            print("ValRand: ",valeur_rand," Valx: ",val_x," Valy: ",val_y)
            if valeur_rand == 0:
                #Bijoux
                self.queue_elements.put(Bijoux(val_x, val_y))
                pass
            elif valeur_rand == 1:
                #Poussiere
                self.queue_elements.put(Poussiere(val_x, val_y))
                #pass
            else:
                #Cas où on ne fait rien
                pass


            valeur_sleep = random.randint(10,50)
            print("Sleep: ",valeur_sleep," secondes")
            time.sleep(valeur_sleep)
            



