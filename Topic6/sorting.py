students = [
    {"name": "Петя", "grade": 81},
    {"name": "Максим", "grade": 99},
    {"name": "Антон", "grade": 75},
    {"name": "Василь", "grade": 99}
]

print("За іменем:")
print(sorted(students, key=lambda x: x["name"]))

print("За оцінкою:")
print(sorted(students, key=lambda x: x["grade"]))