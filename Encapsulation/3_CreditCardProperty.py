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
    @number.setter
    def number(self,number):
        if number:
            self.__number = number
        else:
            raise ValueError("The account number can not be empty")

    # Only a property Getter for the balance attribute
    # Property Getter should be first.
    @property
    def balance(self):
        return self.__balance

# --- DOMAIN METHODS (DEPOSIT & WITHDRAWAL) ---
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    # --- DISPLAY METHOD ---
    def __str__(self) -> str:
        return f"CreditCard(Owner: {self.__name}, Number: {self.__number}, Balance: {self.__balance:.2f} kr)"


# --- TESTING THE CLASS ---
client1 = CreditCard("Alice", "1010", 1000.0)

# Check read-only balance property (returns float)
print(f"Current balance: {client1.balance} kr")  # Output: 1000.0

# Perform deposits and withdrawals via domain methods
client1.deposit(500.0)
print(f"After deposit: {client1.balance} kr")     # Output: 1500.0

client1.withdraw(200.0)
print(f"After withdrawal: {client1.balance} kr")  # Output: 1300.0

# Print full object summary
print(client1)