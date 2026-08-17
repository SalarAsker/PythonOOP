
# Class Person
class Person:
    def __init__(self, person_name: str, person_height: int):
        self.person_name = person_name
        self.person_height = person_height

# Class Attraction
class Attraction:
    def __init__(self, attraction_name:str, min_height: int):
        self.attraction_name = attraction_name
        self.min_height = min_height
        self.total_visitor = 0

    def __str__(self):
        return f"Attraction name: {self.attraction_name}, Total visitor: {self.total_visitor}"


    def admit_visitor(self, person: Person):
        if person.person_height >= self.min_height:
            self.total_visitor += 1

            print(f"{person.person_name} go on board!")
        else:
            print(f"{person.person_name} is too short")


# Create an attraction
# Attraction name and min allowed height
rollercoaster_attraction = Attraction("Rollercoaster", 130)

# Create two persons with the height
alice = Person("Alice", 170)
john = Person("John", 100)

# Check if they can ride, 
rollercoaster_attraction.admit_visitor(alice)
rollercoaster_attraction.admit_visitor(john)

# print the information before the rollercoaster starts
print(rollercoaster_attraction)

