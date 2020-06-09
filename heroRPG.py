

#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random 
from characters import *
# from items import *

sigmund = Hero("Sigmund", 30, 5, 0)


goblin = Goblin("Blorg", 6, 2, 5)
zombie = Zombie("Zombage", 300, 1, 100)
medic = Medic("Dr. Evil", 50, 1, 20)
shadow = Shadow("Shadow", 1, 1, 30)

baddies = {
    "1": goblin,
    "2": zombie,
    "3": medic,
    "4": shadow,
}

def main(enemy):
    while enemy.alive() and sigmund.alive():
        
        sigmund.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            sigmund.attack(enemy)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.health > 0:
            enemy.attack(sigmund)

    camp()
        
def camp():
    print("You are back at the camp. What would you like to do?")
    print("""
    1. go to the shop
    2. go fighting
    3. check your stats
    4. quit
    """)
    choice = input(">> ")
    if choice == "1":
        # shop
        pass
    elif choice == "2":
        baddie = input("""
    Who would you like to fight?
    1. goblin
    2. zombie
    3. medic
    4. shadow\n
    """)
        main(baddies[baddie])
    elif choice == "3":
        sigmund.print_status()
        print(f"You have {sigmund.gold} gold.\n")
        camp()
    elif choice == "4":
        print("Goodbye!")
    else:
        print("sorry, that wasn't a choice.")
        camp()


camp()
