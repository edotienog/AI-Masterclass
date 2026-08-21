# CONTINUE SKIP INVALID DAYS 

daily_steps = [3200, 7100, 9800, 4100, 10500, 6400]
minimum = 7000

total = 0 
valid_days = 0

for steps in daily_steps:
    if steps < minimum:
        print(f"Skipping {steps} (below minimum)")
        continue #Skip this day, go to next
    total += steps
    valid_days += 1

print(f"\nValid days:{valid_days}")
print(f"Total steps (valid days):={total}")
print(f"Average: {total //valid_days}")


