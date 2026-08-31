# A function that works with dictionary
def print_client(client):
    print(f"Name : {client['name']}")
    print(f"Goal : {client['goal']}")
    print(f"Bench : {client['bench_press_kg']} kg")
    print(f"Session: {client['weekly_session']} per week")
    print()

#Create dictionary list for client 
clients = [
    {"name": "James", "goal": "fat_loss", "bench_press_kg": 80, "weekly_session": 4},
    {"name": "Sandra", "goal": "endurance", "bench_press_kg": 50, "weekly_session": 3},
    {"name": "Mwangi", "goal": "muscle gain", "bench_press_kg": 100, "weekly_session": 5}
]

#Looping through the dictionary list of clients 
for client in clients:
    print_client(client)