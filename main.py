import sys

# GLOBAL VARIABLES
data_storage = []
print(sys.argv)

# CLASSES

class Classroom:
    def __init__(self, index, head_teacher, student):
        self.index = index
        self.head_teacher = head_teacher
        self.students = student
        return


class HeadTeacher:
    def __init__(self, first_name, last_name, classroom):
        self.first_name = first_name
        self.last_name = last_name
        self.classroom = classroom
        return


class Teacher:
    def __init__(self, first_name, last_name, classroom, subject):
        self.first_name = first_name
        self.last_name = last_name
        self.classroom = classroom
        self.subject = subject
        return


class Student:
    def __init__(self, first_name, last_name, classroom):
        self.first_name = first_name
        self.last_name = last_name
        self.classroom = classroom
        return

# FUNCTIONS

for idx in data_storage
