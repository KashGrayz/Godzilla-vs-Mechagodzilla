# Godzilla-vs-Mechagodzilla

Create a folder for your project, then create a GitHub repository for the project.

Clone down the repository to your computer and put the invisible .git folder inside your project folder (as well as the .gitignore and README). Make an initial commit.

Create a new file for each class on the UML, as well as a main.py file that will serve as the entry point of your application.

Begin working on the user stories by filling in your classes from smallest to large. Begin with the Weapon class, then move on to the Dinosaur class, then the Robot class. 

Finally, fill out the methods for your battle logic in the Battlefield class. You will only need to import the Dinosaur and Robot classes into the Battlefield class.

You will run the game by creating an object from the Battlefield class inside of main.py and calling the run_game method!
---------------------------

Main Stories
 
(5 points): As a developer, I want to make at least 7 commits with good, descriptive messages. ***
(5 points): As a developer, I want to make a class for each of the following: Robot, Dinosaur, Weapon, Battlefield. ***
(10 points): As a developer, I want a Dinosaur to have a name, health, and attack_power.  ***
(10 points): As a developer, I want a Robot to have a name, health, and active_weapon. ***
(10 points): As a developer, I want a Weapon to have a name and attack_power. ***
(10 points): As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. This attack method should lower a Robot’s health by the value of the Dinosaur’s attack_power. 
(10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon. 
(10 points): As a developer, I want the battle to conclude once either the Robot or the Dinosaur has its health points reduced to zero.
 
Bonus Stories
(5 points): As a developer, I want to choose from a List of 3 possible weapons before a robot makes an attack. 
(5 points): As a developer, I want to create Fleet and Herd classes, allowing for a list of 3 Robots to battle against a list of 3 Dinosaurs.
