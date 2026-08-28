# Dictionary exercise 

week_log =[
    {"Day": "Monday", "steps": 9200, "protocol": "OMAD"},
    {"Day": "Tuesday", "steps": 10500, "protocol": "2MAD"},
    {"Day": "Wednesday", "steps": 8800, "protocol": "OMAD"},
    {"Day": "Thursday", "steps": 11000, "protocol": "Autophagy Marathon"},
    {"Day": "Friday", "steps": 7600, "protocol": "OMAD"},
]

total = 0 # Initial the value to 0 ready to store the sum of steps
for log in week_log:
    print(log["Day"], "|", log["steps"], "|", log["protocol"])
    total += log["steps"] # adds total steps for the week

average = total / len(week_log)
print()
print("Average steps:", average)