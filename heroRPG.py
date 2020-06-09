

#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random 

class Character:
    def __init__(self, name, health, power, gold):
        self.name = name
        self.health = health
        self.power = power
        self.gold = gold

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False   

    def attack(self, other):
        other.health -= self.power
        print(f"{self.name} does {self.power} damage to {other.name}")
        if not other.alive():
            print(f"{other.name} has died!")

    def dodge(self):
        return False

    def print_status(self):
        print("This character has {} health and {} power.".format(self.health, self.power))

class Hero(Character):
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))
    
    def attack(self, other):
        if other.dodge():
            print(f"{other.name} has dodged! No damage.")
        else:
            dice = random.randint(1, 6)
            if dice == 5:
                other.health -= self.power * 2
                print("CRITICAL HIT!")
                print(f"{self.name} does {self.power * 2} damage to {other.name}")
            else:
                other.health -= self.power
                print(f"{self.name} does {self.power} damage to {other.name}")
            if not other.alive():
                print(f"{other.name} has died!")
                print(f"You gain {other.gold} gold.")
                self.gold += other.gold 

class Baddie(Character):
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

class Goblin(Baddie):
    pass

class Zombie(Baddie):
    def alive(self):
        return True

class Medic(Baddie):
    def attack(self, other):
        heal = random.randint(1, 6)
        if heal == 5:
            self.health += 2
            print("The Medic has healed himself!")
            
        other.health -= self.power
        print(f"{self.name} does {self.power} damage to {other.name}")
        if not other.alive():
            print(f"{other.name} has died!")

class Shadow(Baddie):
    def dodge(self):
        chance = random.randint(0,10)
        if chance == 0:
            return False
        else:
            return True

sigmund = Hero("Sigmund", 30, 5, 0)
goblin = Goblin("Blorg", 6, 2, 5)
zombie = Zombie("Zombage", 300, 1, 100)
medic = Medic("Dr. Evil", 50, 1, 20)
shadow = Shadow("Shadow", 1, 1, 30)

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
        # prompt for baddie
        # main(baddie)
        pass
    elif choice == "3":
        # print stats
        pass
    elif choice == "4":
        print("Goodbye!")
    else:
        print("sorry, that wasn't a choice.")
        camp()


camp()
