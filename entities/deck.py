from random import shuffle
from entities import Card


class Deck:

    def __init__(self):
        self.cards = []
        for value in range(9):
            for suit in range(4):
                current_card = Card(value=value, suit=suit)
                self.cards.append(current_card)
        self.shuffle()

    def get_card(self) -> Card | None:
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def shuffle(self) -> None:
        shuffle(self.cards)

    def __repr__(self):
        deck = ", ".join([str(card) for card in self.cards])
        return f"{deck}"
