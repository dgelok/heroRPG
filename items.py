
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

class Poison(Item):
    pass

