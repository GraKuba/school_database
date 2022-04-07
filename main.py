import sys

# GLOBAL VARIABLES
data_storage = []
action = sys.argv[1]
head_teachers = []
teachers = []
students = []
classes_working = []
classes = []
# CLASSES


"""class Klasa:
    def __init__(self, index, head_teacher, student):
        self.index = index
        self.head_teacher = head_teacher
        self.students = student"""


class Wychowawca:
    def __init__(self, name, classroom):
        self.name = name
        self.classroom = classroom


class Nauczyciel:
    def __init__(self, name, subject, classroom):
        self.name = name
        self.classroom = classroom
        self.subject = subject


class Uczen:
    def __init__(self, name, classroom):
        self.name = name
        self.classroom = classroom


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


# CREATING OBJECTS FOR EACH CLASS

for idx in data_storage:
    if idx[0] == "wychowawca":
        classes_tpl = idx[2:]
        classes_working.append(classes_tpl)
        for person in range(1):
            head_teachers.append(Wychowawca(idx[1], idx[2:]))
    elif idx[0] == "nauczyciel":
        classes_tpl = idx[3:]
        classes_working.append(classes_tpl)
        for person in range(1):
            teachers.append(Nauczyciel(idx[1], idx[2], idx[3:]))
    elif idx[0] == "uczen":
        classes_tpl = idx[2:]
        classes_working.append(classes_tpl)
        for person in range(1):
            students.append(Uczen(idx[1], idx[2]))


# CREATING A LIST OF UNIQUE CLASSROOMS

for idx in classes_working:
    for single_idx in idx:
        if single_idx not in classes:
            classes.append(single_idx)


# TAKING INPUT FROM THE TERMINAL AND RETURNING ADEQUATE INFORMATION

head_teachers_list = []
student_list = []
if action in classes:
    for person in head_teachers:
        if action in person.classroom:
            head_teachers_list.append(person.name)
    for person in students:
        if action in person.classroom:
            student_list.append(person.name)


print(head_teachers_list)
print(student_list)


"""print("Head Teachers")
for person in head_teachers:
    print(f"Full name: {person.name} | Classes: {person.classroom}")
print()
for person in teachers:
    print(f"Full name: {person.name} | Subject: {person.subject} | Classes: {person.classroom}")
print()
for person in students:
    print(f"Full name: {person.name} | Classes: {person.classroom}")"""

"""if action == Klasa.index:
    ...
elif action == Wychowawca.name:
    ...
elif action == Nauczyciel.name:
    ...
elif action == Uczen.name:
    ..."""
