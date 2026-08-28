# A real world pattern with dictionaries typical called from an API or a database
#The dictionary uses list to include key-values 

clients =[
    {"name": "James", "goal": "fat loss", "weekly_sessions": 4, "bench_press_kg": 80},
    {"name": "Omollo", "goal": "muscle gain", "weekly_sessions": 5, "bench_press_kg": 100},
    {"name": "Sandra", "goal": "endurance", "weekly_sessions": 3, "bench_press_kg": 50},
    {"name": "Patrick", "goal": "fat loss", "weekly_sessions": 4, "bench_press_kg": 70} 
]

print("Fat loss clients:")
for client in clients:
    if client["goal"] == "fat loss":
        print("-", client["name"], "| Bench:", client["bench_press_kg"], "Kg | Sessions:", client["weekly_sessions"])