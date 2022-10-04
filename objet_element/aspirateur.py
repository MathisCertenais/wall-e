from objet_element.objet_scene import Objet_scene

class Aspirateur(Objet_scene):
    
    def __init__(self, ipos_x, ipos_y):
        super().__init__(0, "aspirateur", ipos_x, ipos_y, "./ui/pictures/aspirateur.png")
        #super().__init__(0, "aspirateur", ipos_x, ipos_y, "C:\\Users\\Mathis\\Documents\\code\\wall-e\\ui\\pictures\\aspirateur.png")
        self.action = []

    def getAction(self):
        retour_actions = self.action.copy()
        self.action = []
        return retour_actions

    def addAction(self, action):
        self.action.append(action)
