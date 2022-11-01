# Robot/ Mechagodzilla Class and attributes

from weapons import Weapon

class Robot:

    def __init__(self, name): #Base info

        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Buzz Hands', 15)

    def bot_attack(self, dino): #Attack method
        self.active_weapon.attack_power - dino.health
        

        
        
    

        
        
        

