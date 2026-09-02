def weekly_report(name, steps_list, goal=8000):
    days_on_target = 0
    for s in steps_list:
        if s >= goal:
            days_on_target += 1
    average_steps = sum(steps_list) / len(steps_list)
    print(f"---{name}'s Weekly Report---")
    print(f"Days Tracked: {len(steps_list)}")    
    print(f"Days on goal: {days_on_target}")
    print(f"Average steps:{round(average_steps, 0)}")
    print()

weekly_report("Alice", [7500, 8200, 9000, 10000, 6500, 7000, 8000])
weekly_report("Bob", [5000, 6000, 7000, 8000, 9000, 10000, 11000], goal=10000)