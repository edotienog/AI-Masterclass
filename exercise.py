# Exercise 1: CREATING VARIABLES
#  Create variable for your name, age, and city
# Print each using an f-string

name = "Edwin Gilbert Otieno"
age = 34
city = "Kisumu-Kenya"

print(f"My name is:, {name}, I am {age}, from {city}.")


# Exercise 2: CONDITIONALS
# Write a program that takes a score and prints a grade
# 90+ = A, 75+ = B, 60+ = C, below 60 = F
score = 56
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else: 
    print("F")

#EXERCISE 3: LOOPS
# Print the first 10 even numbers using a loop
for i in range(1, 21):
    if i % 2 == 0: # if number is divisibly 2 and equal zero its is even (modulus operator)
        print(i)

# Exercise 4: Challenge
# Ask the user for a number and print its multiplication table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
