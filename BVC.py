# Person class
class Person:
    def __init__(self, name: str, age: int, height: float, weight: float):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class BabyCentre:
    # Create a data-attribute visitor using the default constructor
    def __init__(self):
        self.total_visitors = 0

    # Method for weighing
    # Returns the weight of the person passed as argument
    def weigh(self, person: Person):
        self.total_visitors += 1 # Increse the visitor by one
        return person.weight

    # Weight is increased by one after the feeding
    def feed(self, person: Person):
        person.weight += 1
        return person.weight

    def weigh_ins(self):
        return self.total_visitors

# Create two persons
eric = Person("Eric", 1, 80, 10)
peter = Person("Peter", 5, 116, 21)

# Get the weight from the baby centre
baby_centre = BabyCentre()

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

print(f"{eric.name} weighs {baby_centre.weigh(eric)}")
print(f"{peter.name} weighs {baby_centre.weigh(peter)}")

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

baby_centre.feed(eric)
baby_centre.feed(eric)
baby_centre.feed(eric)

print(f"{eric.name} weighs {baby_centre.weigh(eric)}")
print(f"{peter.name} weighs {baby_centre.weigh(peter)}")

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")