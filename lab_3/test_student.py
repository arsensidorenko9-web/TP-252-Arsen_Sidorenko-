import unittest
from Student import Student


class TestStudent(unittest.TestCase):

    def test_student(self):
        student = Student("Ivan", "123", "a@gmail.com", "KB-1")

        self.assertEqual(student.name, "Ivan")
        self.assertEqual(student.phone, "123")
        self.assertEqual(student.email, "a@gmail.com")
        self.assertEqual(student.group, "KB-1")


if __name__ == "__main__":
    unittest.main()