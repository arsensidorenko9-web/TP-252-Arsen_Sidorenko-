import unittest
from Utils import Utils
from Student import Student


class TestUtils(unittest.TestCase):

    def test_save_load(self):
        utils = Utils()

        students = [
            Student("Ivan", "123", "a@gmail.com", "KB-1")
        ]

        utils.save_data("test.csv", students)
        result = utils.load_data("test.csv")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Ivan")


if __name__ == "__main__":
    unittest.main()