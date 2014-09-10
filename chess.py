__author__ = 'Adam'
import sys
from board import Board


class Game:
    def __init__(self):
        # self.player_1 = Player("white")
        # self.player_2 = Bot3435("black")
        self.board = Board()
        self.choices = {
            "1": self.board.print_board,
            "2": self.round,
            "3": self.quit
        }

    @staticmethod
    def show_choices():
        print("""
        Chess Options

        1. Show game board
        2. Move a piece
        3. Quit

        """)

    def play(self):
        """Play a game of chess."""
        while True:
            self.show_choices()
            choice = input("Enter an option:  ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    # Option 1
    def print_game_board(self):
        """Print the game board to terminal"""
        print("Showing game board")

    # Option 2
    def round(self):
        is_success = self.board.move()
        if is_success:
            self.board.player_2.move()
        else:
            self.round()

    # Option 3
    @staticmethod
    def quit():
        print("Thank you for playing Chess!")
        sys.exit(0)

if __name__ == "__main__":
    game = Game()
    game.play()