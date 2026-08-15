

class Person:
  def __init__(self, name_: str):
    # Validate the name using helper function
    if not self.name_ok(name_):
      raise ValueError("Name value is empty")
    
    # Assign the value if no excepton
    self.name = name_
  
  # Helper function
  def name_ok(self, name):
    return len(name) > 0
  
  def return_first_name(self):
    return self.name.split(" ")[0]
  
  def return_last_name(self):
    return self.name.split(" ")[1]

peter = Person("Peter Pythons")
print(peter.return_first_name())
print(peter.return_last_name())

paula = Person("Paula Pythonnen")
print(paula.return_first_name())
print(paula.return_last_name())