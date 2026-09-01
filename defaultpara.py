# Default parameters are fallback values 

def check_steps(steps, goal=8000):
    """
    Check if the number of steps meets the goal.

    Parameters:
    steps (int): The number of steps taken.
    goal (int, optional): The step goal. Defaults to 8000.

    Prints:
    str: A message indicating whether the goal was met.
    """
    if steps >= goal:
        print(f"{steps} steps - Goal of {goal} hit")
    else:
        print(f"{steps} steps - Goal of {goal} missed")


#Use the default goal of 8000 steps
check_steps(9200)
check_steps(7500)