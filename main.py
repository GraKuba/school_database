import sys
sys.argv = 0
# GLOBAL VARIABLES
data_storage = []


# CLASSES


class Classroom:
    def __init__(self, index, head_teacher, student):
        self.index = index
        self.head_teacher = head_teacher
        self.students = student
        return


class HeadTeacher:
    def __init__(self, name, classroom):
        self.name = name
        self.classroom = classroom
        return


class Teacher:
    def __init__(self, name, classroom, subject):
        self.name = name
        self.classroom = classroom
        self.subject = subject
        return


class Student:
    def __init__(self, name, classroom):
        self.name = name
        self.classroom = classroom
        return


# DOWNLOADING DATA FROM IN.TXT

while True:
    description = input()
    if description == "wychowawca":
        full_name = input()
        inputs = ["wychowawca", full_name]
        while True:
            inp = input()
            if inp == "":
                break
            inputs.append(inp)
        data_storage.append(inputs)

    elif description == "nauczyciel":
        full_name = input()
        subject = input()
        inputs = ["nauczyciel", full_name, subject]
        while True:
            inp = input()
            if inp == "":
                break
            inputs.append(inp)
        data_storage.append(inputs)
    elif description == "uczen":
        full_name = input()
        classroom = input()
        inputs = ["uczen", full_name, classroom]
        data_storage.append(inputs)
    else:
        if False or "stop":
            break

for idx in data_storage:
    print(idx)


