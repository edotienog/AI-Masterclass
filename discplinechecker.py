# Discipline Checker

steps = 9200
water_glasses = 8
cold_shower = True
fasting = "OMAD"  # "OMAD", "2MAD", "Autophagy Marathon" or "NONE"
workout = True 

print("=== DAILY DISCIPLINE CHECK==")
print()

if steps >= 10000:
    print("Steps: EXCELLENT -", steps)
elif steps >= 8000:
    print("Steps: ON TARGET -", steps)
else: 
    print("Steps: BELOW TARGET -", steps)

if water_glasses >=8:
    print("Water: GOOD -", water_glasses, "glasses")
else:
    print("Water: LOW -", water_glasses, "glasses")

if cold_shower: 
    print("Cold shower: DONE")
else: 
    print("Cold shower: SKIPPED")
if fasting == "Authophagy Marathon":
    print("Fasting: 48- HOURS FASTING ACTIVE")
elif fasting == "OMAD" or fasting =="2MAD":
    print("Fasting: PROTOCOL ACTIVE -", fasting)
else:
    print("Fasting: NO protocol today")

if workout: 
    print("Workout: COMPLETE")
else: 
    print("Workout: REST DAY")

print()
discipine_win = cold_shower and workout and steps >= 8000 and water_glasses >=8
if discipine_win:
    print("VERDICT: Full discipline day. Every box checked.")
elif not cold_shower and not workout:
    print("VERDICT: Rough day.Get back on track tomorrow.")
else:
    print("VERDICT: Partial. Good effort. Tighten up tomorrow.")

