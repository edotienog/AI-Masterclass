# BREAK STOP WHEN TARGET IS HIT

daily_steps = [3200, 7100, 9800, 10500, 6400, 11200]
target = 10000

for steps in daily_steps: 
    print(f"Checking:{steps} steps")
    if steps >= target:
        print(f"Target hit on this day: {steps} steps. Stopping search.")
        break