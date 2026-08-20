#COMBINING CONDITIONS: DAILY DISCIPLINE CHECK

steps = 9200 
water_glasses = 8 
cold_shower = False
sleep_hours = 7

#STEPS 
if steps >=8000 and water_glasses >= 8:
    print ("Steps and water: both on target")
else:
    print("Steps or water below target.")

#SLEEP 
if sleep_hours >=7 and cold_shower:
    print("Sleep and cold shower: both done.")
else:
    print("Sleep or cold shower missed.")

