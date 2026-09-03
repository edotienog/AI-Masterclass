# datetime module works with dates and times

from datetime import datetime, date

#Today's date and time

now = datetime.now()
print("Current date and time:", now)

#Just the date 
today = date.today()
print("Today's date:", today)
print("Year:", today.year)
print("Month:", today.month)

#Day between two dates
start = date(2025, 1, 1)
end = date(2025, 12, 31)
delta = end - start
print("Days between", start, "and", end, ":", delta.days)


