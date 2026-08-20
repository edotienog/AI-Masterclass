#Program for Personal trainer tracking 
number_of_exercises = 6 
sets_per_exercise = 4
reps_per_set = 10
average_weight_per_rep_kg = 60  
session_duration_minutes = 45

#Total sets 
total_sets = number_of_exercises * sets_per_exercise
print("Total sets in the session:", total_sets)

#Total reps
total_reps = total_sets * reps_per_set
print("Total reps in the session:", total_reps)

#Total volume(kg) lifted in the session
total_kgs_lifted = total_sets * reps_per_set * average_weight_per_rep_kg
print("Total weight lifted in the session (kg):", total_kgs_lifted)

#Reps per minutes 
reps_per_minutes = total_reps // session_duration_minutes
print("Reps per minute:", reps_per_minutes)

print(f"Total volume exceeds 10000 kg:", total_kgs_lifted >= 10000)
