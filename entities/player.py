from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities import Deck


class Player:

    def __init__(self, name: str):
        self.wins = 0
        self.card = None
        self.name = name

    def get_card(self, deck: Deck):
        self.card = deck.get_card()

    def record_victory(self):
        self.wins += 1
