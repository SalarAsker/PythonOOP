# Class har constructor with private attribues
class CreditCard:
    def __init__(self,name:str, number:str,balance:float):
        self.__name = name
        self.__number = number
        self.__balance = balance

    # Property Getter for the name attribute
    # Property Getter should be first.
    @property
    def name(self):
        return self.__name

    # Property Setter for the name attribute
    @name.setter
    def name(self,name):
        if name:
            self.__name = name
        else:
            raise ValueError("The name can not be empty")

 # Property Getter for the number attribute
    # Property Getter should be first.
    @property
    def number(self):
        return self.__number

    # Property Setter for the name attribute
    @name.setter
    def number(self,name):
        if name:
            self.__name = name
        else:
            raise ValueError("The name can not be empty")

    

# Create a customer
client1 = CreditCard("Alice","1010",1000)
# Get the name using property getter
print(client1.name)
# Update name using property setter
client1.name = "Alice Johansson"
print(f"Name is update: {client1.name}")