import sys

# GLOBAL VARIABLES
data_storage = []
action = sys.argv[1]
head_teachers = []
teachers = []
students = []
classes_working = []
classes = []
v1 = []
v2 = []
dct = {}

# CLASSES

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


# CREATING A LISTS OF UNIQUE CLASSROOMS AND NAMES

for idx in classes_working:
    for single_idx in idx:
        if single_idx not in classes:
            classes.append(single_idx)

head_teachers_names = []
for person in head_teachers:
    head_teachers_names.append(person.name)
teachers_names = []
for person in teachers:
    teachers_names.append(person.name)
students_names = []
for person in students:
    students_names.append(person.name)


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
    print(f"Wychowawca: {head_teachers_list} | Uczniowie: {student_list}")
if len(sys.argv) > 2:
    action = sys.argv[1] + " " + sys.argv[2]
    if action in head_teachers_names:
        for person in head_teachers:
            if person.name == action:
                for person_1 in students:
                    if person_1.classroom in person.classroom:
                        student_list.append(person_1.name)
        print(f"Wychowawca: {action} | Uczniowie: {student_list}")
    elif action in teachers_names:
        for person in teachers:
            if person.name == action:
                for single_class in person.classroom:
                    for person_1 in head_teachers:
                        if single_class in person_1.classroom:
                            if person_1.name not in head_teachers_list:
                                head_teachers_list.append(person_1.name)
        print(f"Nauczyciele: {head_teachers_list}")
    elif action in students_names:
        for person in students:
            if person.name == action:
                for idx in teachers:
                    if person.classroom in idx.classroom:
                        v1.append(idx.name)
                        v2.append(idx.subject)
        for idx in range(len(v1)):
            dct[v1[idx]] = v2[idx]
        for position in dct:
            print(f"{position} | {dct[position]}")
    else:
        print("Nieodpowienia komenda")
