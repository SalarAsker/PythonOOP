from LunchCard import LunchCard
from PaymentTerminal import PaymentTerminal


if __name__ == "__main__":
    exactum = PaymentTerminal()

    print("Initial funds:", exactum.terminal_funds) # Corrected from exactum.funds
    print()

    # Cash payment
    change = exactum.eat_lunch(10)
    print("Cash lunch")
    print("Change:", change)
    print("Funds:", exactum.terminal_funds) # Corrected from exactum.funds
    print("Lunches:", exactum.sold_lunches) # Corrected from exactum.lunches
    print()

    # Create a LunchCard
    card = LunchCard(7)
    print("Card balance:", card.balance)
    print()

    # Special lunch with card
    result = exactum.eat_special_lunch_lunchcard(card) # Corrected method name
    print("Special lunch with card")
    print("Payment successful:", result)
    print("Card balance:", card.balance)
    print()

    # Try another special lunch
    result = exactum.eat_special_lunch_lunchcard(card) # Corrected method name
    print("Another special lunch")
    print("Payment successful:", result)
    print("Card balance:", card.balance)
    print()

    # Regular lunch with card
    result = exactum.eat_lunch_lunchcard(card)
    print("Regular lunch with card")
    print("Payment successful:", result)
    print("Card balance:", card.balance)
    print()

    # Deposit money
    exactum.deposit_money_on_card(card, 50)
    print("After depositing $50")
    print("Card balance:", card.balance)
    print("Terminal funds:", exactum.terminal_funds) # Corrected from exactum.funds
    print()

    # Buy another special lunch
    result = exactum.eat_special_lunch_lunchcard(card) # Corrected method name
    print("Special lunch after deposit")
    print("Payment successful:", result)
    print("Card balance:", card.balance)
    print()

    # Final information
    print("FINAL INFORMATION")
    print("Funds available at terminal:", exactum.terminal_funds) # Corrected from exactum.funds
    print("Regular lunches sold:", exactum.sold_lunches) # Corrected from exactum.lunches
    print("Special lunches sold:", exactum.sold_special_lunches) # Corrected from exactum.specials