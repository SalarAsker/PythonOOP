# Person class
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # Method to check who is older
    def older_than(self, another: "Person"):
        return self.age < another.age

# Create some perosns

muhammad = Person("Muhammad ibn Musa al-Khwarizmi", 780)
pascal = Person("Blaise Pascal", 1623)
grace = Person("Grace Hopper", 1906)

# Find out who is older
if muhammad.older_than(pascal):
    print(f"{muhammad.name} is older than {pascal.name}")
else:
    print(f"{pascal.name} is older than {muhammad.name}")

