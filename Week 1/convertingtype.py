steps_as_string = "9400" # this is a str, not a number
steps_as_int = int(steps_as_string) # convert the string to an integer

print(type(steps_as_string)) # <class 'str'>
print(type(steps_as_int)) # <class 'int'>

# You can now do maths with it

target = 10000
gap = target - steps_as_int
print(f"You are {gap} steps away from your target of {target} steps.")
