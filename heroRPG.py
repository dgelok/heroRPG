#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

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

    def print_status(self):
        print("This character has {} health and {} power.".format(self.health, self.power))

class Hero(Character):
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

class Goblin(Character):
    def print_status(self):
        print("The Goblin has {} health and {} power.".format(self.health, self.power))

class Zombie(Character):
    def alive(self):
        return True

    def print_status(self):
        print("The Zombie has {} health and {} power.".format(self.health, self.power))

sigmund = Hero("Sigmund", 10, 5)
blorg = Goblin("Blorg", 6, 2)
zomb = Zombie("Zombage", 300, 1)

def main():
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    while zomb.alive() and sigmund.alive():
        sigmund.print_status()
        zomb.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            sigmund.attack(zomb)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if zomb.health > 0:
            zomb.attack(sigmund)


main()
