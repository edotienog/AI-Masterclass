#Practical use of math module in python to calculate full rest day fit into training programm

import math 

total_days = 50
training_days_per_week = 5
weeks = total_days / 7

# Calculate total training days
print(f"Total days: {total_days}")
print(f"Full weeks: {math.floor(weeks)}")

#Distance using pythagorean theorem
walk_east = 3.0 # Km
walk_north = 4.0 # Km
distance = math.sqrt(walk_east**2 + walk_north**2)
print(f"Distance from starting point: {distance} Km")