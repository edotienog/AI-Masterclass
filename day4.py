# Discipline Grader
import math

steps  = 7500
sleep = 6
water_glasses = 5
cold_shower = False
Pages_read = 15
target_steps = 10000


#Steps 
if steps >= 10000:
    print("Excellent! You've met your step goal for the day.")
elif steps >= 7500:
    print("Good job! You've met your step goal for the day.")
else:
    print("Needs more work otherwise")

#Water 
if water_glasses >= 8:
    print("You've meet your daily water intake")
else: 
    print("Needs to drink more water")

#Cold Shower 

if cold_shower == True:
    print("Completed")
else:
    print("Skipped")

#Pages read

if Pages_read >= 10:
    print ("You have met you daily pages read")
else:
    print ("You did not met daily pages read")


progress_pct = (steps / target_steps) * 100

rounded = math.floor(progress_pct)

print("Summary:", rounded, "% of the daily target achieved")