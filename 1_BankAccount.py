class BankAccount:
  def __init__(self, balance_: float, owner_: str):
    self.balance = balance_
    self.owner = owner_
    

# An object of BankAccount class
petter_account = BankAccount(1000, "Petter Johansson")

# An object of BankAccount class
adam_account = BankAccount(1000, "Adam Johansson")

print(petter_account.owner)
print(petter_account.balance)

print(adam_account.owner)
print(adam_account.balance)
