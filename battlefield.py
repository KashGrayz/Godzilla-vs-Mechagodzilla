
from godzilla import Dinosaur
from mechagodzilla import Robot
from time import sleep

from weapons import Weapon

# Battlefeild class and attributes

class Battlefield(object):

    def __init__(self):
        self.robot = Robot('Mechagodzilla')
        self.dino = Dinosaur('Godzilla', 10)
        self.weapon = Weapon('Buzz Hands', 10)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        
    def display_welcome(self):
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
        print(self.robot.health)
        print(self.dino.health)


    def display_winner(self):
         pass
