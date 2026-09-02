# Multiple parameter with default paramaters 

def log_day(steps, water=8, protocol="OMAD"):
    print(f"Steps: {steps} | Water: {water} glasses | Protocol: {protocol}")

#Calling the function with all parameters
log_day(9200) # Uses both defaults 
log_day(10500, water=9) # Override water only
log_day(8800, water=7, protocol="2MAD") # Override both