# Robot/ Mechagodzilla Class and attributes



from weapons import Weapon


class Robot:

    def __init__(self, name): #Base info

        self.name = name
        self.health = 100
        self.active_weapon = Weapon

    def bot_attack(self, dino): #Attack method
        self.dino = dino
        self.active_weapon - int(self.dino.health)
        return self.dino.health
    

        
        
        

