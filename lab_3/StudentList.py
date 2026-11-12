class StudentList:
    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)
       

    def delete(self, position):
        if 0 <= position < len(self.students):
            self.students.pop(position)

    def update(self, position, student):
        if 0 <= position < len(self.students):
            self.students[position] = student
            

    def find_position(self, name):
        for i in range(len(self.students)):
            if self.students[i].name == name:
                return i
        return -1

    def get_all(self):
        return self.students

    def __len__(self):
        return len(self.students)