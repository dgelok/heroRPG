from characters import *

#hero
sigmund = Hero("Sigmund", 30, 5, 200, 0, 5, {})

#items
SuperTonic = Tonic(False)
SuperPoison = Poison(True)
mmegapoison = MegaPoison(True)
mmegatonic = MegaTonic(False)

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

