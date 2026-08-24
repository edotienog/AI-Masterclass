# Fasting protocol Checker

fasting = "Autophagy Marathon" # "OMAD", "2MAD", "Autophagy Marathon" or "None"
cold_shower = False


# FASTING PROTOCOL
print("==FASTING PROTOCOL==")
print()

if fasting == "Autophagy Marathon":
    print("48 hours Fasting Protocol COMPLETED:", fasting)
elif fasting == "OMAD" or "2MAD":
    print("Fasting protocol ACTIVE:")
else: 
    print("No Fasting protocol logged")

print()

#COLD SHOWER

peak_discipline = fasting and cold_shower
if fasting == "Autophagy Marathon" and cold_shower == True:
    print("PEAK DISCIPLINE DAY")
else: 
    print("NOT PEAK DISCIPLINE")



