#Accessing a dictionary value using key and dictionary name

daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5 
}

print("Steps today:", daily_log["steps"])
print("Hydration today:", daily_log["water_glasses"],"glasses")
print("Protocol:", daily_log["fasting_protocol"], "fasting")
print("Cold shower:", daily_log["cold_shower"])
