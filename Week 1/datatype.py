#Variable and Data Types   
#INTERGERS: int
steps = 7800
water_glasses = 12
pages_read = 20
sleep_hours = 8
bench_press_reps = 10

#Float: Decimal numbers
body_weight = 70.5
km_walked = 5.2
body_fat_percentage = 15.5

#strings: str
name = "Edwin Gilbert Otieno"
fasting_protocol = "18:6"
skill_of_the_day = "Python Programming"
morning_goal = "Go for a run"

#boolean: boo
cold_weather = True
workout_completed = False
fasting_active = True

print("Steps today:", steps)
print("Water glasses:", water_glasses)
print("Fasting:", fasting_active)
print("Name:", name)
print("Cold weather:", cold_weather)
print("Workout completed:", workout_completed)


#using type() function to check the data type of a variable
print(type(steps))
print(type(body_weight))
print(type(skill_of_the_day))
print(type(cold_weather))

#Printing variable with text
#method 1: Using comma
fav_meal = "Rice and beans"
print("My favorite meal is", fav_meal)

#method 2: Using f-string (the better way
certification = "Plumbing level 5"
print(f"My certification is {certification}")

