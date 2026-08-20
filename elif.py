#IF + ELIF + ELSE : GRADED STEPS CHECK

steps = 6000

if steps >= 10000: 
    print(" Excellent! You reached your daily goal")
elif steps >= 8000: 
    print("On target! You are close to reaching your daily goal")
elif steps >= 5000:
    print("Halfway there! You are making progress towards your daily goal")
else:
    print("Below target. Today was sedentary")
