from datetime import date

class PlayerRegistration:
  def __init__(self, name_: str, year: int, month: int, day: int, points_: int):

    # Validate inputs and raise Exceptions for bad data
    # Exceptions stop the program execution
    if not self.name_ok(name_):
      raise ValueError("Player name must be at least 2 characters long.")
    if not self.points_ok(points_):
      raise ValueError("Points must be a positive integer.")
    if not self.date_ok(year, month, day):
      raise ValueError(f"Invalid date: {year}-{month}-{day}")

   # Assign verified values when there is no exception
    self.name = name_
    self.points = points_
    self.date = date(year, month, day)

    # Helper methods for validating data.
  def name_ok(self, name: str) -> bool:
      return len(name) >= 2

  def points_ok(self, points: int) -> bool:
      return points >= 0

  def date_ok(self, year: int, month: int, day: int) -> bool:
      try:
          date(year, month, day)
          return True
      except ValueError:
          return False


## Creating a player
Person1 = PlayerRegistration("Peter", 2025, 11, 25, 235)
# Printing all information
print(Person1.name)
print(Person1.points)
print(Person1.date)

Person1.name_ok("Clause")

# ## Creating a player with no name. IT WILL CAUSE AN ERROR
# Person1 = PlayerRegistration("", 2025, 11, 25, 235)
# # Printing all information
# print(Person1.name)
# print(Person1.points)
# print(Person1.date)

