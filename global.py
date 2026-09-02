# Local scope variables are only accessible within the function they are defined in. They cannot be accessed outside of that function.
# Global scope are variable created outside a function. Exist for the entire program and can be read inside functions

step_goals = 8000 # global variable

def check_today(steps):
    results = "hit" if steps >= step_goals else "missed" # local variable
    print(f"Goal {results} for today! You walked {steps} steps.")

check_today(9200) 
check_today(7500)

# This would cause an error because results is a local variable and cannot be accessed outside the function
# print(results) 