#Exercise with steps counts using append, remove, and reverse

steps = [8800, 6500, 11000, 9200, 7300]
steps.append(10500)
steps.remove(6500)
steps.sort(reverse=True)
print("Final list:", steps)

#Count days over 9000
high_days = 0
for s in steps:
    if s >=9000:
        high_days += 1
print("Days of 9000 steps:",high_days)