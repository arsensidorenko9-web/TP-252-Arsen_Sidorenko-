from lab2 import findPosition, addElemToSortedList, deleteElem, loadData, saveData


def test_findPosition():
    students = [{"name": "Bob"}, {"name": "Jon"}]
    assert findPosition(students, "Jon") == 1


def test_addStudent():
    students = [{"name": "Bob"}]
    addElemToSortedList(students, {"name": "Emma"})
    assert students[1]["name"] == "Emma"


def test_deleteStudent():
    students = [{"name": "Bob"}]
    assert deleteElem(students, "Bob") == True
    assert len(students) == 0