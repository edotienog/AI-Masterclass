from math import sqrt, floor, ceil

from random import random, randint, choice

# No need to write math.sqrt() or random.randint()

print("Square root of 225:", sqrt(225))
print(" Floor of 9.7:", floor(9.7))
print(" Ceiling of 9.7:", ceil(9.7))

protocols = ["OMAD", "2MAD", "Autophagy Marathon"]
print("Random protocol:", choice(protocols))
print("Random Steps Bonus:", randint(100, 500), "steps")