#SMP Daily target 

daily_steps = [8200, 5100, 11300, 6800, 9400, 4200, 10100]
target = 8000

# Use for loop to print daily count and whether it hit 8000 steps (SMP daily target)
for steps in daily_steps: 
    if steps >= 8000:
        print(f"Daily target hit: {steps}")
    else:
        print(f"Daily count: {steps}")
