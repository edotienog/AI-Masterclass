# A list of weekly steps 

week_steps = [9200, 7400, 10500, 8800, 6900, 11000, 9600]
target = 8000


#Loop whether you hit target 8000 steps
for steps in week_steps:
    if steps >= 8000:
        print("DAILY TARGET HIT -", steps)
    else:
        print("DID NOT HIT DAILY TARGET-", steps)

print()
# Total number of day tracked
print("== NUMBER OF DAYS TRACKED==")
print()
print(len(week_steps))
