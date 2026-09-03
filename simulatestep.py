# Simulating steps counts 

import random

print("Simulating Step Counts for This Week:")
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days:
    steps = random.randint(5000, 13000)
    status = "OK" if steps >= 8000 else "Low"
    print(f"{day}: {steps} steps - {status}")