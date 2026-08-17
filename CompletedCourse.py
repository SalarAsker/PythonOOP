from datetime import date

class CompletedCourse:
    def __init__(self, course_name: str, credits: int, completion_date: date):
        self.name = course_name
        self.credits = credits
        self.completion_date = completion_date


# Here we create some completed courses and add these to a list 
completed = []

# Adding maths
maths1 = CompletedCourse("Mathematics 1", 5, date(2024, 3, 11))
prog1 = CompletedCourse("Programming 1", 6, date(2023, 12, 17))

# Adding maths1 object sveral times
completed.append(maths1)
completed.append(maths1)
completed.append(maths1)

completed.append(prog1)

# Let's add a couple more straight to the list
completed.append(CompletedCourse("Physics 2", 4, date(2023, 11, 10)))
completed.append(CompletedCourse("Programming 2", 5, date(2025, 5, 19)))

# Update credits
completed[0].credits = 10
# Check the value for other
print(completed[1].credits)
print(completed[2].credits)

print(completed[0] is completed[1])
print(completed[0] is completed[2])

print(id(completed[0]))
print(id(completed[1]))
print(id(completed[2]))


# Go through all the completed courses, print out their names 
# and sum up the credits received
credits = 0
for course in completed:
    print(course.name)
    credits += course.credits

print("Total credits received:", credits)


