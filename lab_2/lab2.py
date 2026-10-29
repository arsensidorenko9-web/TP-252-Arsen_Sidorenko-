
import csv
from sys import argv

def loadData(filename):
    with open(filename, encoding="utf-8-sig") as file:
        return sorted(csv.DictReader(file), key=lambda x: x["name"])

def saveData(filename, students):
    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "phone", "email", "group"])
        writer.writeheader()
        writer.writerows(students)

def printAllList(students):
    for item in students:
        print(item)

def findPosition(students, name):
    index = 0
    for item in students:
        if item["name"] < name:
            index += 1
        else:
            break
    return index

def addElemToSortedList(students, newElem):
    position = findPosition(students, newElem["name"])
    students.insert(position, newElem)

def getElement():
    name = input("Ім'я: ")
    phone = input("Телефон: ")
    email = input("Email: ")
    group = input("Група: ")
    return {"name": name, "phone": phone, "email": email, "group": group}

def deleteElem(students, name):
    index = findPosition(students, name)
    if index < len(students) and students[index]["name"] == name:
        del students[index]
        return True
    return False

def updateElement(students):
    name = input("Введіть ім'я студента: ")
    index = findPosition(students, name)

    if index < len(students) and students[index]["name"] == name:
        del students[index]
        addElemToSortedList(students, getElement())
        print("Дані змінено")
    else:
        print("Студента не знайдено")

def main():
    filename = argv[1]
    globalList = loadData(filename)

    while True:
        choice = input("C-додати, D-видалити, P-показати, U-змінити, X-вихід: ").lower()

        match choice:
            case "c":
                addElemToSortedList(globalList, getElement())
            case "d":
                name = input("Ім'я для видалення: ")
                print("Видалено" if deleteElem(globalList, name) else "Не знайдено")
            case "p":
                printAllList(globalList)
            case "u":
                updateElement(globalList)
            case "x":
                saveData(filename, globalList)
                print("Дані збережено")
                break
            case _:
                print("Невідома команда")

if __name__ == "__main__":
    main()
