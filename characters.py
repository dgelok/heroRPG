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
            if hit <= 0:
                hit = 1
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
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

class Hero(Character):

    def __init__(self, name, health, power, gold, armor, evade, supplies=[]):
        self.supplies = supplies
        super(Hero, self).__init__(name, health, power, gold, armor, evade)
    
    def attack(self, other):
        if other.dodge():
            print(f"{other.name} has dodged! No damage.")
        else:
            dice = random.randint(0, 5)
            if dice == 0:
                hit = self.power * 2 - other.armor
                print("CRITICAL HIT!")
                print(f"{self.name} does {hit} damage to {other.name}")
                other.health -= hit
            else:
                hit = self.power - other.armor
                if hit <= 0:
                    hit = 1
                other.health -= hit
                print(f"{self.name} does {hit} damage to {other.name}")
            if not other.alive():
                print(f"{other.name} has died!")
                print(f"You gain {other.gold} gold.")
                self.gold += other.gold 
    
    # def useItem(self):
    #     print("You have the following supplies: \n")
    #     for item in self.supplies:
    #         print("\t" + item)

    #     itemchoice = input("What would you like to use? >> ")
    #     if itemchoice not in self.supplies:
    #         print("I'm sorry, you don't have that.")
    #     else: 
    #         if itemchoice == "SuperTonic":
    #             print("You use the SuperTonic and feel much better!")
    #             self.health += 10
    #             print(f"Health at {self.health}")
    #             self.supplies.remove("SuperTonic")

class Baddie(Character):

    def attack(self, other):
        if other.dodge():
            print(f"You dodge the attack! No damage.")
        else:
            hit = self.power - other.armor
            if hit <= 0:
                hit = 1
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

class Ghoul(Baddie):
    def __init__(self, name, health, power, gold, armor, evade, canResurrect):
        self.canResurrect = canResurrect
        super(Ghoul, self).__init__(name, health, power, gold, armor, evade)
    
    def alive(self):
        if self.health > 0:
            return True
        
        if self.health < 0 and self.canResurrect:
            print(f"{self.name} is reviving!")
            self.canResurrect = False
            self.health = 15
            self.evade += 1
            self.armor += 1
            self.power += 2
            return True
        else:
            return False

class Slime(Baddie):
    def attack(self, other):
        if other.dodge():
            print(f"{other.name} has dodged! No damage.")
        else:
            chance = random.randint(0, 20)
            if chance <= 6:
                print(f"{self.name} slips and misses you! No damage.")
            elif chance <= 18:
                hit = self.power - other.armor
                if hit <= 0:
                    hit = 1
                other.health -= hit
                print(f"{self.name} does {hit} damage to {other.name}")
            else:
                hit = self.power * 2 - other.armor
                print("CRITICAL HIT!")
                print(f"{self.name} does {hit} damage to {other.name}!!!")

            if not other.alive():
                print(f"{other.name} has died!")



