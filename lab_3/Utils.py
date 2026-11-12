
import csv
from Student import Student


class Utils:
    def load_data(self, filename):
        students = []

        with open(filename, encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            print(reader.fieldnames)

            for row in reader:
                student = Student(
                    row["name"],
                    row["phone"],
                    row["email"],
                    row["group"]
                )
                students.append(student)

        students.sort(key=lambda x: x.name)
        return students

    def save_data(self, filename, students):
        with open(filename, "w", newline="", encoding="utf-8-sig") as file:
            fields = ["name", "phone", "email", "group"]
            writer = csv.DictWriter(file, fieldnames=fields)

            writer.writeheader()

            for student in students:
                writer.writerow(student.to_dict())


