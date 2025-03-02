students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "jack russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
    ]


for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")

students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

for i in range(len(students)):
    print(i + 1, students[i])
