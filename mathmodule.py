import math

steps = 9400
target = 10000

progress_pct = (steps / target) * 100

# math.floor rounds DOWN to nearest whole number
rounded = math.floor(progress_pct)

print("Steps today:", steps)
print("Progress:", rounded, "%")

if progress_pct >= 100:
    print("Target hit")
elif progress_pct >= 80:
    print("Close. Push the last", target - steps, "steps.")
else:
    print("Still", target - steps, "steps to go")