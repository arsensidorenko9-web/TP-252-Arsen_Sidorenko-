globalList = [
   {"name":"Bob", "phone":"0631234567", "email": "bob@gmail.com", "group": "КБ-253"},
      {"name":"Emma", "phone":"0631234567", "email": "emma@gmail.com", "group": "КБ-253"},
      {"name":"Jon",  "phone":"0631234567", "email": "jon@gmail.com", "group": "КБ-253"},
      {"name":"Zak",  "phone":"0631234567", "email": "zak@gmail.com", "group": "КБ-253"}
  ]


def printAllList(listForPrinting):
    for item in listForPrinting:
        str = "Name = " + item["name"] + " Phone = " + item["phone"] + " Email = " + item["email"] + " Group = " + item["group"]
        print(str)

def findPosition(listForFinding, nameForFinding):
    index = 0
    for item in listForFinding:
        if item["name"] < nameForFinding: 
            index += 1
        else:
            break
    return index

def addElemToSortedList(listForAdd, newElem):
    positionForInsert = findPosition(listForAdd, newElem["name"])
    listForAdd.insert(positionForInsert, newElem)
    return

def getElement():
    name = input("Please enter the name ")
    phone = input("Please enter the phone ")
    email = input("Please enter the email ")
    group = input("Please enter the group ")

    return {"name":name, "phone":phone, "email": email, "group":group}

def deleteElem(listForDel, name):
    indexForDel = findPosition(listForDel, name)
    if indexForDel < len(listForDel) and listForDel[indexForDel]["name"] == name:
        del listForDel[indexForDel]
        return True
    else:
        return False

def updeteElement(listForUpdate):
    name = input("Введіть ім'я студента: ")
    index = findPosition(listForUpdate, name)

    if index < len(listForUpdate) and listForUpdate[index]["name"] == name:
        del listForUpdate[index]
        addElemToSortedList(listForUpdate, getElement())
        print("Дані змінено")
    else:
        print("Студента не знайдено")
    return


def main():
    while True:
        chouse = input("Please enter the commanfd [C - add new elem, D - delete elem,  P - print all List, U - update element, X - exit] ")
        match chouse:
            case "C" | "c" :
                newElem = getElement()
                addElemToSortedList(globalList, newElem)
            case "D" | "d":
                nameElemForDel = input("Please enter the name for delete ")
                if deleteElem(globalList, nameElemForDel):
                    print("Element has been deleed")
                else:
                    print("Element hasn't been found")
            case "P" | "p" :
                printAllList(globalList)
            case "U" | "u" :
                updeteElement(globalList)
            case "X" | "x" :
                print("Exit")
                break
            case _:
                print("Wrong operation")


main()

