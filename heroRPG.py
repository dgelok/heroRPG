
RESTRICTION_ON = True


import random 
from characters import *
from variables import *


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
    2. SuperPoison - 10gp
    3. Armor Upgrade - 15gp
    4. Sword Upgrade - 15gp
    5. Evade Upgrade - 20gp
    6. Nothing
    \n""")
    myinput = input(">> ")
    if myinput == "1":
        if sigmund.gold >= 10:
            sigmund.gold -= 10
            sigmund.supplies["SuperTonic"] = SuperTonic
            print("One SuperTonic added to supplies!")
        else:
            print("Sorry, you do not have enough gold.")            
    elif myinput == "2":
        if sigmund.gold >= 10:
            sigmund.gold -= 10
            sigmund.supplies["SuperPoison"] = SuperPoison
            print("One SuperPoison added to supplies!")
    elif myinput == "3":
        if sigmund.gold >= 15:
            sigmund.gold -= 15
            sigmund.armor += 2
            print(f"You upgrade your armor. Your armor is now at level {sigmund.armor}.")
        else:
            print("Sorry, you do not have enough gold.") 
    elif myinput == "4":
        if sigmund.gold >= 15:
            sigmund.gold -= 15
            sigmund.power += 3
            print(f"You upgrade your skills. Your power is now at level {sigmund.power}.")
        else:
            print("Sorry, you do not have enough gold.")
    elif myinput == "5":
        if sigmund.gold >= 20:
            sigmund.gold -= 20
            sigmund.evade += 2
            print(f"You upgrade your skills. Your evade is now at level {sigmund.evade}.")
        else:
            print("Sorry, you do not have enough gold.") 
    else:
        pass
        
    print("Going back to the camp...\n")
    camp()

def useItem(s):
    if sigmund.supplies == {}:
        print("\nYou have no supplies!")
        return

    print("You have the following supplies: \n")
    for item in sigmund.supplies:
        print("\t" + item)
    itemchoice = input("What would you like to use? >> ")
    if itemchoice not in sigmund.supplies:
        print("I'm sorry, you don't have that.")
        return

    myitem = sigmund.supplies[itemchoice]
    if not myitem.canUse(s):
        print("You can't use that now!")
        return
    
    myitem.use(sigmund)
    del sigmund.supplies[itemchoice]



camp()
