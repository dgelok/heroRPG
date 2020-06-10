
RESTRICTION_ON = True


import random 
from characters import *
# from items import *
class Item():
    def __init__(self, restrictToFight):
        self.restrictToFight = restrictToFight

class Tonic(Item):

    def use(self, r):
        if self.restrictToFight:
            if r:
                print("Can't use this now!")
            else:
                sigmund.health += 10
                print("Health goes up by 10!")
        else:
            sigmund.health += 10
            print("Health goes up by 10!")

#hero
sigmund = Hero("Sigmund", 30, 5, 10, 0, 5, {})

#items
SuperTonic = Tonic(True)
# SuperPoison = Poison(True)

#baddies
goblin = Baddie("Blorg the Goblin", 20, 2, 5, 0, 0)
zombie = Zombie("Peter the Zombie", 300, 1, 100, 0, 0)
medic = Medic("Dr. Evil", 40, 1, 20, 3, 0)
shadow = Baddie("Frank the Shadow", 1, 1, 30, 0, 18)
ghoul = Ghoul("Steve the Ghoul", 50, 4, 30, 1, 2, True)
slime = Slime("Bill the Slime", 30, 2, 5, 0, 4)

baddies = {
    "1": goblin,
    "2": zombie,
    "3": medic,
    "4": shadow,
    "5": ghoul,
    "6": slime,
}

def main(enemy):
    RESTRICTION_ON = False
    print("\n"*20)
    while enemy.alive() and sigmund.alive():
        
        sigmund.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. Attack")
        print("2. Use an Item")
        print("3. Flee\n")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            sigmund.attack(enemy)
        elif raw_input == "2":
            useItem(RESTRICTION_ON)
        elif raw_input == "3":
            print(f"Running away from {enemy.name}...")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.health > 0:
            enemy.attack(sigmund)
        print("\n")
    
    RESTRICTION_ON = True 

    if not sigmund.alive():
        print("You have died! Goodbye.\n\n\n")
    else:
        camp()

def camp():
    print("\n"*2)
    print("You are safe at the camp. What would you like to do?")
    print("""
    1. go to the shop
    2. go fighting
    3. check your stats
    4. use an item
    5. quit\n
    """)
    choice = input(">> ")
    if choice == "1":
        shop()
    elif choice == "2":
        baddie = input("""
    Who would you like to fight?
    1. goblin
    2. zombie
    3. medic
    4. shadow
    5. ghoul
    6. slime\n
    """)
        if int(baddie) <= len(baddies):
            main(baddies[baddie])
        else:
            camp()
    elif choice == "3":
        sigmund.print_status()
        print(f"You have {sigmund.gold} gold, {sigmund.armor} armor, {sigmund.evade} evade, and {sigmund.power} power.\n")
        camp()
    elif choice == "4":
        useItem(RESTRICTION_ON)
        camp()
    elif choice == "5":
        print("Goodbye!")
    else:
        print("sorry, that wasn't a choice.")
        camp()

def shop():
    print(f"""\n\n\n
    Welcome to the shop.
    You currently have {sigmund.gold}gp.
    What would you like to purchase?
    
    1. SuperTonic - 10gp
    2. Armor Upgrade - 15gp
    3. Evade - 20gp
    4. Sword Upgrade - 20gp
    5. Nothing
    \n""")
    myinput = input(">> ")
    if myinput == "1":
        if sigmund.gold >= 10:
            sigmund.gold -= 10
            sigmund.supplies["SuperTonic"] = SuperTonic
            print("One SuperTonic added to supplies!")
        else:
            print("Sorry, you do not have enough gold.")            
    # elif myinput == "2":
    #     if sigmund.gold >= 15:
    #         sigmund.gold -= 15
    #         sigmund.armor += 2
    #         print(f"You upgrade your armor. Your armor is now at level {sigmund.armor}.")
    #     else:
    #         print("Sorry, you do not have enough gold.") 
    # elif myinput == "3":
    #     if sigmund.gold >= 20:
    #         sigmund.gold -= 20
    #         sigmund.evade += 2
    #         print(f"You upgrade your skills. Your evade is now at level {sigmund.evade}.")
    #     else:
    #         print("Sorry, you do not have enough gold.") 
    # elif myinput == "4":
    #     if sigmund.gold >= 20:
    #         sigmund.gold -= 20
    #         sigmund.power += 5
    #         print(f"You upgrade your skills. Your power is now at level {sigmund.power}.")
    # else:
        pass
        
    print("Going back to the camp...\n")
    camp()

def useItem(s):
    print("You have the following supplies: \n")
    for item in sigmund.supplies:
        print("\t" + item)

    itemchoice = input("What would you like to use? >> ")
    if itemchoice not in sigmund.supplies:
        print("I'm sorry, you don't have that.")
    else: 
        myitem = sigmund.supplies[itemchoice]
        myitem.use(s)



camp()
