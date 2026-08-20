bench_press_sets = 5
reps_per_set = 10
weight_per_rep_kg = 65

total_reps = bench_press_sets * reps_per_set
total_volume_kg = total_reps * weight_per_rep_kg
reps_per_minutes = total_reps // 4 # assuming 4 minutes of work time

print("=== BENCH PRESS SESSION ===")
print(f"Sets: {bench_press_sets}")
print(f"Reps per set: {reps_per_set}")
print(f"Weight per rep (kg): {weight_per_rep_kg}")
print(f"Total reps: {total_reps}")
print(f"Total volume (kg): {total_volume_kg}")
print(f"Reps per minute: {reps_per_minutes}")