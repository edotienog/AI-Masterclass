#A comprehension can also transform each item.
#Without a filter, it applies the transformation to every item
#Converting steps to kilometers

weekly_steps = [10000, 12000, 8000, 15000, 11000, 9000, 13000]  

#Convert each steps count to km
# Assuming 1.3 kmp per 1000 steps
km_walked = [round(s * 1.3/1000, 2) for s in weekly_steps]
print("Steps:", weekly_steps)
print("Km :", km_walked)

#Assuming 0.04 calories per steps 
calories_burnt = [round(k * 0.04, 2) for k in weekly_steps]
print("Calories_Burnt:", calories_burnt)
 