# Using random module to generate a random week number
import random
import math 

def generate_week():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    total = 0
    goal_days = 0

    for day in days:
        steps = random.randint(6000, 12000)  # Random steps between 1000 and 10000
        total += steps
        if steps >= 8000:
            goal_days += 1
            print(f"{day}: {steps} steps")

    avg = math.floor(total / len(days))
    print(f"\nAverage steps for the week: {avg}")
    print(f"Days on goal: {goal_days}/7")

generate_week()