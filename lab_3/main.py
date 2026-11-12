
import sys
from Student import Student
from StudentList import StudentList
from Utils import Utils


def main():
    filename = "lab2.csv"

    student_list = StudentList()
    utils = Utils()

    student_list.students = utils.load_data(filename)

    while True:
        print("C - Додати")
        print("D - Видалити")
        print("P - Показати")
        print("U - Оновити")
        print("X - Вийти")

        choice = input("Ваш вибір: ").upper()

        if choice == "C":
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            group = input("Група: ")

            student = Student(name, phone, email, group)
            student_list.add(student)

        elif choice == "D":
            name = input("Введіть ім'я: ")
            position = student_list.find_position(name)

            if position != -1:
                student_list.delete(position)
                print("Студента видалено")
            else:
                print("Студента не знайдено")

        elif choice == "P":
            for student in student_list.get_all():
                print(student)

        elif choice == "U":
            name = input("Введіть ім'я: ")
            position = student_list.find_position(name)

            if position != -1:
                student = Student(
                    input("Нове ім'я: "),
                    input("Новий телефон: "),
                    input("Новий email: "),
                    input("Нова група: ")
                )

                student_list.update(position, student)
                print("Дані оновлено")
            else:
                print("Студента не знайдено")

        elif choice == "X":
            utils.save_data(filename, student_list.get_all())
            print("Дані збережено")
            break


if __name__ == "__main__":
    main()
