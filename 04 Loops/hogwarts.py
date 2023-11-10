students = ["Hermione", "Harry", "Ron"]

# print(students[0])
# print(students[1])
# print(students[2])

# using for loop
for s in students:
    print(s)

# len returns the number of items in the list
for i in range(len(students)): 
    print(i + 1,students[i])

# Dictionaries
students = {
    "Hermione": "Hogwarts",
    "Harry": "Hogwarts",
    "Ron": "Hogwarts",
    "Draco": "Slytherin>",
}

for student in students:
    print(student, students[student], sep=", ")

# A list of dictionaries
students = [
    {"name": "Hermione", "house": "Hogwarts", "patronus":"Otter"},
    {"name": "Harry", "house": "Hogwarts", "patronus":"Stag"},
    {"name": "Ron", "house": "Hogwarts", "patronus":"Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus":None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")