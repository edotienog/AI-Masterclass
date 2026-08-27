#Using in to check whether key exist in a dictionary

daily_log = {
    "steps": 92000,
    "water_glasses": 8,
    "fasting_protocol": "OMAD",
}

#using in to check the key-value

if  "steps" in daily_log:
    print("Steps recorded:", daily_log["steps"])
if "sleep_hour" not in daily_log:
    print("Sleep hours not logged")