
from godzilla import Dinosaur
from mechagodzilla import Robot
from weapons import Weapon
from time import sleep

# Battlefeild class and attributes

class Battlefield(object):

    def __init__(self):
        self.robot = Robot('Mechagodzilla')
        self.dino = Dinosaur('Godzilla', 10)
        self.weapon = Weapon('Buzz Hands', 15)
        self.mech_attack = self.robot.bot_attack(self.dino)
        self.zilla_attack = self.dino.dino_attack(self.robot)

    def run_game(self): #initiate session
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        
    def display_welcome(self): #Run intro
        sleep(1)
        print('\n Tokyo is in ruins again!\n')
        sleep(1)
        print('\n These titans are here for carnage\n')
        sleep(1)
        print('\n Who is the King of Monsters!?\n')
        sleep(1)
        print('\n Prepare for....\n')
        sleep(2)
        print('\n Godzilla VS Mechagodzilla!!!\n')
        
    def battle_phase(self):
        sleep(1.5)
        print(f'\n{self.dino.name} \nHealth: {self.dino.health} \nAttack Power: {self.dino.attack_power}\n')
        sleep(1)
        print(f'''\nSKREEEONGK!!! {self.dino.name} emerges from Tokyo bay!!\n''')
        sleep(2)
        print(f'\n{self.robot.name} \nHealth: {self.robot.health} \nAttack Power: {self.weapon.attack_power}\n')
        sleep(1)
        print(f'boom! CRACK!!! {self.robot.name} has dropped from the sky!!!')
        
        while self.dino.health > 0 and self.robot.health > 0:
            sleep(1)
            
            print(f'''\n{self.robot.name} attacks {self.dino.name} with {self.weapon.name} for {self.weapon.attack_power}!!!''')
            
            self.mech_attack
            
            sleep(1)
            
            print(f'\n{self.dino.name} has {self.dino.health} health remaining!')
            
            sleep(1)
            
            print(f'''\n{self.dino.name} uses Atomic Breath on {self.robot.name} for {self.dino.attack_power}!!! ''')
            
            self.zilla_attack
            
            print(f'\n{self.robot.name} has {self.robot.health} energy remaining!')
            if self.dino.health == 0:
                sleep(2)
                print(f'''{self.dino.name} has been DEFEATED!! 
                {self.robot.name} lanches back into the clouds!!! ''')
            elif self.robot.health == 0:
                sleep(2)
                print(f'''{self.robot.name} is no longer FUNCTIONAL!!! 
                {self.dino.name} wallows back into Tokyo Bay...''')
        
    
    def display_winner(self):
         pass
