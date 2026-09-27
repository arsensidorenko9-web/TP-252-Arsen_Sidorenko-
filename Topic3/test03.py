
student = {
    "name": "Арсен",
    "age": 18,
    "city": "Чернігів",
    "course": 2
}
print("словник:", student)
print("Ключі:", list(student.keys()))
print("Значення (values):", list(student.values()))
print("Пари (items):", list(student.items()))

student.update({"group": "CS-252"})
print("Після update():", student)

del student["group"]
print("Після del", student)

student.clear()
print("Після clear():", student)