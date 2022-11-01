
from godzilla import Dinosaur
from mechagodzilla import Robot
from time import sleep

from weapons import Weapon

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
        sleep(1.75)
        print(f'\n{self.robot.name} \nHealth: {self.robot.health} \nAttack Power: {self.weapon.attack_power}\n')
        sleep(1)
        
        pass
    
    def display_winner(self):
         pass
