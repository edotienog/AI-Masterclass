# Return exits the functions and send a value back to the caller

def calculate_average_steps(steps_list):
    total = sum(steps_list)
    average = total/ len(steps_list)
    return average 

# Weekly steps data
weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]
avg = calculate_average_steps (weekly_steps)
print("Average steps this week:", avg)

# Define the function
def get_status(steps):
    if steps > 10000:
        return "Exceeded"
    elif 8000 <= steps <= 10000: 
        return "Hit"
    else: 
        return "Missed"
# Call the function for each day and print results
for day, steps in enumerate(weekly_steps, start=1):
    status = get_status(steps)
    print(f"Day {day}: {steps} steps → {status}")