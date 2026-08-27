# Looping in dictionary using key and value both

daily_log = {
    "steps": 92000,
    "water_glasses": 8,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5,
    "cold_shower": True,
}

#loop through key and value together

for key, value in daily_log.items():
    print(key, ":", value)
print()
# Loop throuhg keys only in dictionary
print("==Prints only Key Alone in Dictionary==")
for key in daily_log.keys():
    print(key)

print()
#Loop through values in dictionary
print("==Prints only values in Dictionary==")
for value in daily_log.values():
    print(value)