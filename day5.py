#SMP Daily target 

daily_steps = [8200, 5100, 11300, 6800, 9400, 4200, 10100]
target = 8000

# Use for loop to print daily count and whether it hit 8000 steps (SMP daily target)
for steps in daily_steps: 
    if steps >= target:
        print(f"Daily target hit: {steps}")
    else:
        print(f"Daily count: {steps}")

#using while loop to skip any day below 5000 when calculating weekly average

total = 0
valid_days = 0
i = 0

# Instead of len(), use the list itself to control the loop
while i < daily_steps.index(daily_steps[-1]) + 1:
    if daily_steps[i] < 5000:
        i += 1
        continue  # skip days below 5000
    total += daily_steps[i]
    valid_days += 1
    i += 1

average = total / valid_days if valid_days > 0 else 0
print("\nWeekly Summary:")
print(f"Valid days (>=5000 steps): {valid_days}")
print(f"Average steps (valid days only): {average:.2f}")