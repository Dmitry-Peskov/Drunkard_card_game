class Card:
    __SUITS = ["♠", "♥", "♦", "♣"]
    __VALUES = ["6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟", "🥷", "👸", "🫅", "🎴"]

    def __init__(self, suit: int, value: int):
        self.suit = suit
        self.value = value
        self.img = self.__SUITS[suit] + self.__VALUES[value]

    def __lt__(self, other: "Card"):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False

    def __gt__(self, other: "Card"):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False

    def __repr__(self):
        return f"{self.img}"
