from entities.deck import Deck
from entities.player import Player


class Game:

    def __init__(self):
        self.player_1 = Player(name=input("Введите имя 1-го игрока: "))
        self.player_2 = Player(name=input("Введите имя 2-го игрока: "))
        self.deck = Deck()

    def opening_cards(self):
        message = f"{self.player_1.name} вытянул {self.player_1.card}, а {self.player_2.name} вытянул {self.player_2.card}"
        print(message)

    def who_wins(self):
        if self.player_1.card > self.player_2.card:
            self.player_1.record_victory()
            print(f"В этом раунде победил: {self.player_1.name}")
        else:
            self.player_2.record_victory()
            print(f"В этом раунде победил: {self.player_2.name}")

    def run(self):
        while self.deck.count_cards() >= 2:
            message = "Введите Х для выхода, любая другая клавиша, чтобы продолжить: "
            answer = input(message).upper()
            if answer == "X" or answer == "Х":
                break
            self.player_1.get_card(self.deck)
            self.player_2.get_card(self.deck)
            self.opening_cards()
            self.who_wins()
        print(f"Игра закончена!\nИтоговый счёт:\n  {self.player_1.name} - {self.player_1.wins}\n  {self.player_2.name} - {self.player_2.wins}")


if __name__ == "__main__":
    game = Game()
    game.run()
