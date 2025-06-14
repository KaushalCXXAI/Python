# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]

# gryffindors =[
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)


# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])

# students = ["Hermione", "Harry", "Ron"]

# gryffindor = []

# for student in students:
#     gryffindor.append({"name":student, "house": "Gryffindor"})

# print(gryffindor)

# students = ["Hermione", "Harry", "Ron"]

# gryffindor = [ {"name":student ,"house": "Gryffindor" } for student in students ]

# print(gryffindor)

# students = ["Hermione", "Harry", "Ron"]

# gryffindor =  {student: "Gryffindor"  for student in students }

# print(gryffindor)

students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i+1, students[i])

for i, students in enumerate(students):
    print(i+1, students)
