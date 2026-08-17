# File: LunchCard.py
# LunchCard class
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    # Return the balance
    def show_balance(self):
        return f"Card balance: {self.balance} $" 

    # Deposit money
    def deposit_money(self, amount: float):
        self.balance += amount
        print(f"New balance is: {self.balance} $")

    # Pay with card
    def subtract_from_card(self, amount: float):
        if self.balance > amount:
            self.balance -= amount
            return True
        return False

    