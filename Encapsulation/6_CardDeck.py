from random import shuffle

class DeckOfCards:
    def __init__(self):
        # Delegate initialization to a private helper method
        self.__reset_deck()

    # Private helper method (internal implementation detail)
    def __reset_deck(self):
        self.__deck = []
        suits = ["spades", "hearts", "clubs", "diamonds"]
        
        # Populate 52 standard playing cards
        for suit in suits:
            for number in range(1, 14):
                self.__deck.append((suit, number))
                
        # Shuffle the newly generated cards
        shuffle(self.__deck)

    # Public interface method
    def deal(self, number_of_cards: int) -> list:
        hand = []
        # Remove and return the top cards from the deck
        for _ in range(number_of_cards):
            if len(self.__deck) > 0:
                hand.append(self.__deck.pop())
            else:
                raise ValueError("Cannot deal cards: the deck is empty.")
        return hand

    # Public action that reuses the internal helper
    def restart_game(self):
        """Clears existing state and rebuilds a fresh shuffled deck."""
        self.__reset_deck()

deck = DeckOfCards()
hand1 = deck.deal(5)
print("Hand 1:", hand1)

hand2 = deck.deal(5)
print("Hand 2:", hand2)

deck.restart_game()
print("Hand 1:", hand1)
