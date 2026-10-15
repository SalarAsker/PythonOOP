class Student:
    def __init__(self,name:str, student_id:str):
        self.__name = name
        self.__student_id = student_id
        self.__study_credit = 0
    
    # Add credits to student
    def add_credits(self, study_credits):
        if study_credits > 0:
            self.__study_credit += study_credits

    def __str__(self):
        return f"{self.__name}, credits: {self.__study_credit}"

# You can add correct value to the credits
student_a = Student("Peter","1010")
student_a.add_credits(5)

# student_a.__name = "Peter Peter"
print(student_a.__study_credit)

