# using pop() method to remove item by its index position

weekly_steps = [9200, 10500,8800, 11000, 7600]
print("Before:", weekly_steps)

#New variable for item removed
removed = weekly_steps.pop() # Removes the last item in the list
print("Removed:", removed)
print("After:", weekly_steps)

#Removing an item at a specific index position using pop() method

removed2 = weekly_steps.pop(1) #remove item at index 1
print("Removed:", removed2)
print("After:", weekly_steps)
