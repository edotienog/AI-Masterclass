#Standard loop Approach

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

goal_days = []
for steps in weekly_steps:
    if steps >= 8000:
        goal_days.append(steps)
print(goal_days)


#Using list comprehension to achieve the same result
#List comprehension format is: [expression for item iterable if condition]
print("---LIST COMPREHENSION---")
goal_days_lc = [steps for steps in weekly_steps if steps >= 8000]
print(goal_days_lc)