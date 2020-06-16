
import random

#characters
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

#
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
    def __init__(self, name, health, power, gold, armor, evade, poisoned):
        super(Zombie, self).__init__(name, health, power, gold, armor, evade)
        self.poisoned = poisoned

    def alive(self):
        if self.poisoned == True:
            return False
        else:
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


#items 
class Item():
    def __init__(self, restrictToFight):
        self.restrictToFight = restrictToFight
    
    def canUse(self, status):
        if self.restrictToFight:
            if status: 
                return False
            else:
                return True
        return True

class Tonic(Item):
    def use(self, recipient):
        recipient.health += 10
        print("Health goes up by 10!")

class MegaTonic(Tonic):
    def use(self, recipient):
        recipient.health += 20
        print("Health goes up by 20!")

class Poison(Item):
    def use(self, recipient):
        recipient.health -= 10
        print(f"{recipient.name} has been poisoned! Health at {recipient.health}")

class MegaPoison(Item):
    def use(self, recipient):
        recipient.health -= 20
        print(f"{recipient.name} has been MEGA poisoned! Health at {recipient.health}!")

class ZombiePoison(Item):
    def use(self, recipient):
        try:
            recipient.poisoned == True
            print(f"{recipient.name} has been ZOMBIE MEGA ULTRA GIGA POISONED! He gonna die now!")
        except:
            print("ZombiePoison only works on Zombies!")