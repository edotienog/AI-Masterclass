# My personal log dictionary

my_log = {
    "steps": 7800,
    "water_glasses": 10,
    "fasting_protocol": "2MAD",
    "cold_shower": False,
    "sleep_hours": 7
}

print("My Log:")
for key, value in my_log.items():
    print(f" {key} : {value}")
print()
#Check if steps is greater than or equal to 8000

if my_log["steps"] >= 8000:
    print("Target steps reached:")
else: 
    print("Target not reached:")