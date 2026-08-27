# A list of dictionary with several records in the list

week_log = [
    {"day": "Monday", "steps": 9200, "protocol": "OMAD","cold_shower": True},
    {"day": "Tuesday", "steps": 10500, "protocol":"2MAD", "cold_shower": True},
    {"day": "Wednesday", "steps": 8800, "protocol": "OMAD", "cold_shower": False},
    {"day": "Thursday", "steps": 11000, "protocol": "Autophaghy Marathon", "cold_shower": True},
    {"day": "Friday", "steps": 7600, "protocol": "OMAD", "cold_shower": True},
]

# Accesing value inside nested data 

# Steps from the first day of (Monday)
print("Monday steps:", week_log[0]["steps"]) 
# Day name of the third record (Wednesday)
print("Wednesday protocol:", week_log[2]["protocol"]) 
# Second day, all details
print("Tuesday details:", week_log[1])
print()

# Looping through the dictionary list
print("== Week steps hit target 8000 ==")
for log in week_log:
    status = "Goal hit" if log["steps"] >= 8000 else "Below goal"
    print(log["day"], "-", log["steps"], "steps -", status)
print()
print("== Whether Cold shower was done==")

for log in week_log:
    status = "Cold shower done" if log["cold_shower"] == True else "Not Done"
    print(log["day"], status)