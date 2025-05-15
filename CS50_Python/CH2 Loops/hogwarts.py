# Simple list of student names
students = ["Hermione", "Harry", "Ron"]

# Iterate through list directly
for student in students:
    print(student)

# Iterate through list using indexes
for i in range(len(students)):
    print(i + 1, students[i])  # i+1 to show 1-based counting

# Dictionary mapping students to houses
students = {
    "Hermione": "Griffindor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin"
}

# Access dictionary values by key
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

# Iterate through dictionary keys and print key-value pairs
for student in students:
    print(student, students[student], sep=", ")

# List of dictionaries - each student has multiple attributes
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}  # None represents absence of value
]

# Access each student's attributes in the list of dictionaries
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")