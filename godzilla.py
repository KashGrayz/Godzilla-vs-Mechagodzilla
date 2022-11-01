# Dinosaur/ Godzilla class and attributes

from unicodedata import name

from mechagodzilla import Robot


class Dinosaur:
    
    def __init__(self, name, attack_power): #Base info
        self.name = name
        self.attack_power = attack_power
        self.health = 120
        

    def dino_attack(self, robot): #Attack method
        self.robot = robot
        print(f"{self} attacks with Atomic Breath ")
        
    
