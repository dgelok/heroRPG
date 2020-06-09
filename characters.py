import random

class Character:
    def __init__(self, name, health, power, gold, armor, evade):
        self.name = name
        self.health = health
        self.power = power
        self.gold = gold
        self.armor = armor
        self.evade = evade

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False   

    def attack(self, other):
        if other.dodge():
            print(f"{other.name} has dodged! No damage.")
        else:
            hit = self.power - other.armor
            if hit < 0:
                hit = 0
            other.health -= hit
            print(f"{self.name} does {hit} damage to {other.name}")
            if not other.alive():
                print(f"{other.name} has died!")

    def dodge(self):
        dice = random.randint(0, 20)
        if self.evade > dice:
            return True
        else:
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
                hit = self.power - other.armor
                if hit < 0:
                    hit = 0
                other.health -= hit
                print(f"{self.name} does {hit} damage to {other.name}")
            if not other.alive():
                print(f"{other.name} has died!")
                print(f"You gain {other.gold} gold.")
                self.gold += other.gold 

class Baddie(Character):
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

    def attack(self, other):
        if other.dodge():
            print(f"You dodge the attack! No damage.")
        else:
            hit = self.power - other.armor
            other.health -= hit
            print(f"{self.name} does {hit} damage to you.")
            if not other.alive():
                print(f"{other.name} has died!")

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


