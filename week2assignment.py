# Exercise 1: List Operations 
# Create a list of 5 fruits 
#Sort it reverse it, then add one more item 

fruits = [
    "manago",
    "banana",
    "apple",
    "orange",
    "grape"
]

fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.append("pawpaw")
print(fruits)
print()

# Exercise 2: Dictionary work
# Create a dictionary for a student with name, age, and grade 
# print each using the key

student = {"name": "Evans Kidero", "age": "28", "grade": "B+"}

    

#Print each using key
for key, value in student.items():
    print(f"{key}: {value}")
print()
# Exercise 3: Nested Data 
#Create a list of 3 students dictionaries 
# Loop through and print each student's name

students = [
    {"name": "Evans Kidero", "age": "28", "grade": "B+"},
    {"name": "James Orengo", "age": "24", "grade": "A"},
    {"name": "John Mbandi", "age": "23", "grade": "C+"},
]

#Loop through each list

for s in students:
    print(f"{s['name']}: {s['grade']}")

#Building a simple phonebook
#store 3 contact as a dictionary name: number 
#Print a formatted contact list 

phonebook = {"Eric": "071294588", "Amina": "070853941", "James": "0712891292"}

print("--- Contacts ---")
for name, number in phonebook.items():
    print(f"{name}: {number}")