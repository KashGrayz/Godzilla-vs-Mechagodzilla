# Robot/ Mechagodzilla Class and attributes



from weapons import Weapon


class Robot:

    def __init__(self, name): #Base info

        self.name = name
        self.health = 100
        self.active_weapon = Weapon

    def bot_attack(self, dinosaur): #Attack method
        self.dinosaur = dinosaur
        print(f'{self} attacks {dinosaur} with {self.active_weapon}')

        
        
        

