# using del to remove/ delete key and valua in a dictionary

daily_log = {
    "steps": 92000,
    "water_glasses": 8,
    "fasting_protocol": "OMAD",
    "Junk_food": "delete me"
    }

#Deleting junk_food
del daily_log["Junk_food"]
print("After deleting junk food:", daily_log)