# Random module to generate random numbers in python

import random

#Random interger between 1 and 10 (inclusive)
print("Random Number:", random.randint(1, 10))

#Random float between 0 and 1
print("Random Float:", random.random())

#Random choice from a list
skills = ['Python', 'Java', 'C++', 'JavaScript', 'SQL', 'HTML', 'CSS']
print("Today's Skill:", random.choice(skills))

#Shuffle a list
random.shuffle(skills)
print("Shuffled Skills:", skills)