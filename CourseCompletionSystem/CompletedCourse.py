# File: CompletedCourse.py
from Course import Course
from Student import Student

class CompletedCourse:
    def __init__(self, student: Student, course: Course, grade: int):
        self.student = student
        self.course = course
        self.grade = grade

    def __str__(self):
        return f"""Student: {self.student.student_name},
with id: {self.student.student_number},
Has passed the course: {self.course.course_name}.
With {self.grade} grade."""