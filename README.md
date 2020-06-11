# Hero RPG!

Hero RPG (heroRPG.py) is a python-based RPG to be run on the command line. It was created as part of DigitalCrafts training (June 2020 Cohort), and designed for the development of OOP skills.

### Requirements

- Python3 or later (built on Python3.8)
- all helper modules (characters, variables, etc)

### Similar projects

I've designed two more text-based RPG games that are similar in concept; [Zorklon5](https://github.com/dgelok/Zorklon5) and [Pyramid_Game](https://github.com/dgelok/pyramidGame). Pyramid Game also utilizes OOP principles, but Zorklon5 is more highly-developed.  

### How it works

| Feature | Description |
| ----------- | ----------- |
| Characters | All characters are found in the characters.py file and inherit from the Character class. The Hero inherits directly, and all baddies inherit through the Baddie child class. Special features are enabled for different characters, such as regeneration (Ghoul), inability to be killed (Zombie), healing (Medic) and etc. Each character has attributes which affect their health, attack power, armor class, evasive abilities, and the amount of gold they carry. |
| Items | Also found in the characters.py file, items are a separate class which all inherit from the Item parent class. Items are added to the hero's supplies and used either at camp or during battle, depending on item functionality. |
| Instances | All instantiation takes place in variables.py, which imports from characters.py. All items, baddies, and our hero are created here. |
| Actions | All functions are found in heroRPG.py, our main file. Program flow begins in our camp() function, which provides the user with a list of action choices. The shop() function enables the hero to buy items or upgrades. The main() function is essentially a large while loop, providing a turn-based fight against an enemy object passed as an argument. The final function, useMe(), determines whether an item can be used, executes its use, and removes it from the here's supplies attribute. |

### Current bugs and possible additional developments

- Currently cannot add multiples of the same object to supplies.
- Zombie poison isn't working, and doesn't actually kill the zombie.
- A map mechanic should be added
- A way to "win" the game should be added
- Visual cleanup to make the game easier to follow for the user
