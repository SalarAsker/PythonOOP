from random import choice, randint

class Student:
    def __init__(self, id_: int, first_name_: str, last_name_: str):
        self.id = id_
        self.first_name = first_name_
        self.last_name = last_name_

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def new_student():
    first_names = ["Mark","Mindy","Mary","Mike"]
    last_names = ["Javanese", "Rusty", "Scriptor", "Pythons"]

    f_name = choice(first_names) # radomly pick a first name
    l_name = choice(last_names) # radomly pick a last name
    s_id = randint(1000,5000) # # radomly generate an id

    return Student(s_id, f_name, l_name) # Create and return a Student object

def change_first_name(student: Student):
    n = input("Enter a new first name? ")
    student.first_name = n


# Call the function five times and store the students in a list
students = []

for _ in range(5):
    students.append(new_student())

# Print all the students

for s in students:
    print(s)