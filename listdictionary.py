# A list of dictionary with several records in the list

week_log = [
    {"day": "Monday", "steps": 9200, "protocol": "OMAD","cold_shower": True},
    {"day": "Tuesday", "steps": 10500, "protocol":"2MAD", "cold_shower": True},
    {"day": "Wednesday", "steps": 8800, "protocol": "OMAD", "cold_shower": False},
    {"day": "Thursday", "steps": 11000, "protocol": "Autophaghy Marathon", "cold_shower": True},
    {"day": "Friday", "steps": 7600, "protocol": "OMAD", "cold_shower": True},
]
#print(week_log)

# Accesing value inside nested data 

# Steps from the first day of (Monday)
print("Monday steps:", week_log[0]["steps"]) 
# Day name of the third record (Wednesday)
print("Wednesday protocol:", week_log[2]["protocol"]) 
# Second day, all details
print("Tuesday details:", week_log[1])