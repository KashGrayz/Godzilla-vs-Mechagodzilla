# Dinosaur/ Godzilla class and attributes

class Dinosaur:
    
    def __init__(self, name, attack_power): #Base info
        self.name = name
        self.attack_power = attack_power
        self.health = 130
        

    def dino_attack(self, robot): #Attack method
        self.robot = robot
        print(f"{self} attacks {robot} with Atomic Breath ")

    
