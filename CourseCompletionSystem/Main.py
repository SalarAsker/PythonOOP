# Main.py
from Course import Course
from Student import Student
from CompletedCourse import CompletedCourse

# Create some student and save them in a list
students =[]
students.append(Student("Ollie", "1234", 10))
students.append(Student("Peter", "3210", 23))
students.append(Student("Lena", "9999", 43))
students.append(Student("Tina", "3333", 8))
students.append(Student("John","1210", 40))

# Create a course
programming1 = Course("Programming 1", "progx100", 7.5)

# Add completed course for each student with grace C for all
completed = []
for std in students:
    completed.append(CompletedCourse(std,programming1,"C"))

# Print result of all the students.
for com in completed:
    print(com)
    print()