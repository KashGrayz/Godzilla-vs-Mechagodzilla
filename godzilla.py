# Dinosaur/ Godzilla class and attributes

from unicodedata import name


class Dinosaur:
    
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 120
        

    def dino_attack(self, robot):
        self.name = name
        self.robot = robot
        print(f"{self} attacks with Atomic Breath ")
    
