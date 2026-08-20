# NESTED CONDITIONS: TRAINING SESSION CHECK

workout_done = True 
weight_lifted_kg = 5200
personal_best_kg = 5000

if workout_done: 
    print("workout logged.")
    if weight_lifted_kg > personal_best_kg:
        print("New personal best! Previous:",personal_best_kg, "kg")
        print("New record:", weight_lifted_kg, "kg")
    else:
        print("Solid session. No new record today.")
else:
    print("Rest day. No workout logged.")