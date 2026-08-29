# A mini project creating contact book and using search function to locate names 
# Creating the data structure and verify it prints correctly
contact_book = [
    {"name": "Edwin Otieno", "Phone": "0719124592","skill": "welding", "city":"Nairobi"},
    {"name": "Bruce Banner", "Phone": "0719920812","skill": "plumbing", "city": "Mombasa"},
    {"name": "Peter Parker", "Phone": "078919121","skill": " upholstery", "city": "Eldoret"},
    {"name": "Lupita nyongo", "Phone": "0790818981","skill": "Tailoring", "city": "Nairobi"},
    {"name": "Sylvester stallone", "Phone": "0791821921","skill": "Mechanic", "city": "Kisumu"}
]
print("Stored Contacts:", len(contact_book[0]))
print(contact_book[0])

#Step 2: Display all contact 
# Using a loop to print a clean format 

print("==== CONTACT BOOK====")

for i, contact in enumerate(contact_book):
    print(f"\n{i+1}. {contact['name']}")
    print(f" Phone: {contact['Phone']}")
    print(f" Skill: {contact['skill']}")
    print(f" City: {contact['city']}")
print()
# Step 3: Search by name and print results
#Looping and comparing the list with the search value
print("=== SEARCH CONTACT BY NAME ===")
search_name = "James Otieno"
found = False

for contact in contact_book:
    if contact["name"] == search_name:
        print("Contact found:")
        print(f" name: {contact['name']}")
        print(f" Phone: {contact['Phone']}")
        print(f" Skill: {contact['skill']}")
        print(f" City: {contact['city']}")
        found = True
        break

if not found:
        print("No contact found with name",search_name)
print()
print("=== SEARCH BY CITY ===")
# Step 4: Search by City

search_city = "Nairobi"
print(f"Contacts in {search_city}:")
for contact in contact_book:
     if contact["city"] == search_city:
        print(f" name: {contact['name']} | {contact['Phone']} | {contact['skill']}")
print()
#Step 5: Add a new contact 
print("=== Adding New Contact ===")
new_contact = {"name": "Kevin Mwangi", "Phone": "0767890123","skill": "beekeeping", "city":"Nakuru"}
contact_book.append(new_contact)
print("After:", len(contact_book), "contacts")
print("Last contact:", contact_book[-1])
print(" === SUMMARY ===")
print(f"\nTotal contacts: {len(contact_book)}")