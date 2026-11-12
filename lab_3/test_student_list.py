import unittest
from Student import Student
from StudentList import StudentList


class TestStudentList(unittest.TestCase):

    def test_add(self):
        students = StudentList()
        students.add(Student("Ivan", "123", "a@gmail.com", "KB-1"))

        self.assertEqual(len(students), 1)

    def test_delete(self):
        students = StudentList()
        students.add(Student("Ivan", "123", "a@gmail.com", "KB-1"))
        students.delete(0)

        self.assertEqual(len(students), 0)

    def test_find(self):
        students = StudentList()
        students.add(Student("Ivan", "123", "a@gmail.com", "KB-1"))

        self.assertEqual(students.find_position("Ivan"), 0)


if __name__ == "__main__":
    unittest.main()