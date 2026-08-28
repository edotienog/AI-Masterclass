# using a dictionary as list itself 

weekly_summary = {
    "week": 1, 
    "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "protocol": ["2MAD", "OMAD", "Autophagy Marathon", "OMAD", "2MAD", "OMAD"],
    "cold_shower_completed": 6
}

print("Week:", weekly_summary["week"])
print("Total days tracked:",len(weekly_summary["steps"]))
print("First day steps:", weekly_summary["steps"][0])
print("Average steps:", sum(weekly_summary ["steps"] ) / len(weekly_summary["steps"]))