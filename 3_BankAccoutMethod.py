class BankAccount:

    def __init__(self, account_number_: str, owner_: str, balance_: float, annual_interest_: float):
        self.account_number = account_number_
        self.owner = owner_
        self.balance = balance_
        self.annual_interest = annual_interest_

    # This method adds the annual interest to the balance of the account
    def add_interest(self):
        self.balance += self.balance * self.annual_interest


# Creating several accoutns
peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)
marys_account = BankAccount("98765-432", "Mary Major", 2500.0, 0.02)
johns_account = BankAccount("11223-344", "John Doe", 500.0, 0.01)
janes_account = BankAccount("55667-788", "Jane Smith", 3000.0, 0.025)

# Addning interest on Peter's and Marys's account
peters_account.add_interest()
marys_account.add_interest() 

# Print all account balances
print(f"Peter's account balance: {peters_account.balance}")
print(f"Mary's account balance: {marys_account.balance}")
print(f"John's account balance: {johns_account.balance}")
print(f"Jane's account balance: {janes_account.balance}")