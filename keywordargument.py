# Passing an argument by name instead of position using a keyword argument

def client_report(name, goal, sessions=4, bench_kg=60):
    print(f"Client: {name} | Goal: {goal} | Sessions: {sessions} | Bench Press: {bench_kg} kg")

#Positional arguments 
client_report("John", "Lose Weight")

#Keyword arguments: Order does not matter
client_report(goal="Gain Muscle", name="Sarah", bench_kg=80)

#Mix of positional and keyword arguments
client_report("Sandra", "endurance", bench_kg=50)
