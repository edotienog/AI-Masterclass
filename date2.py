from datetime import date

#How many days until a goal date?
today = date.today()    
goal_date = date(2026, 12, 31)
days_left = (goal_date - today).days
print("Days until end of 2025", goal_date, ":", days_left)

#Format the date as text 
formatted = today.strftime("%B %d, %Y")
print("Formatted date:", formatted)