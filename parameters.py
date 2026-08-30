# Paramates: Passing information into 

def check_steps(steps): 
    if steps >= 10000:
        print(steps, "steps - Goal exceeded")
    elif steps >= 8000:
        print(steps, "steps - Goal hit")
    else: 
        print(steps, "Steps - Below goal")


check_steps(9200)
check_steps(7500)
check_steps(11000)