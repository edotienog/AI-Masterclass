# Adding key value in a dictionary

daily_log ={
    "steps": 92000,
    "water_glasses": 8,
    "fasting_protocol": "OMAD"
}

# Add a new key + value 
daily_log["pages_read"] = 30
print("After adding pages read:", daily_log)

# Updating an existing key
daily_log["steps"] = 10400
print("After updating steps:", daily_log)