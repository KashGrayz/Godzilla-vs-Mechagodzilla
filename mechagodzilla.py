# Robot/ Mechagodzilla Class and attributes

from unicodedata import name
from weapons import Weapon

class Robot:

    def __init__(self, name):

        self.name = name
        self.health = 100
        self.active_weapon = Weapon

    def bot_attack(self, dinosaur):
        self.name = name
        self.dinosaur = dinosaur
        print(f'{self} attacks with {Weapon}')
        
        
        

