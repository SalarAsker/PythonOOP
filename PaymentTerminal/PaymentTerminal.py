# File: PaymentTerminal.py

from LunchCard import LunchCard

class PaymentTerminal:
    def __init__(self):
        self.terminal_funds = 1000 # start terminal funds
        self.sold_lunches = 0 # lunch sale statistics
        self.sold_special_lunches = 0 # special_lunch sale statistics

    # Normal lunch cash payment
    def eat_lunch(self, payment: float):
        price = 2.50

        if payment >= price:
            self.terminal_funds += price
            self.sold_lunches += 1
            return payment - price

        return payment
    
    # Special lunch cash payment
    def eat_special(self, payment: float):
        price = 4.50

        if payment >= price:
            self.terminal_funds += price
            self.sold_special_lunches += 1
            return payment - price

        return payment

    # Normal lunch card payment
    def eat_lunch_lunchcard(self, card: LunchCard):
        price = 2.50
        if card.subtract_from_card(price):
            self.sold_lunches += 1
            return True
        return False

     # Special lunch card payment
    def eat_special_lunch_lunchcard(self, card: LunchCard):
        price = 4.50
        if card.subtract_from_card(price):
            self.sold_lunches += 1
            return True
        return False

    # Deposit money on the card, the student gives cash to the terminal, so:
    # the card balance increases
    # the terminal's cash increases
    def deposit_money_on_card(self, card: LunchCard, amount_to_add: float):
        card.deposit_money(amount_to_add)
        self.terminal_funds += amount_to_add