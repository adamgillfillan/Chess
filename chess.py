__author__ = 'Adam'
import sys
import time
from board import Board
from termcolor import colored
from player import Player
from bot3435 import Bot3435


class Game:
    def __init__(self):
        self.player_1 = Player("white")
        self.player_2 = Bot3435("black")
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

    # Option 2
    def round(self):
        is_success, old_posn, piece = self.player_1.move()
        if is_success:
            self.successful_move_message(old_posn, piece)
            self.board.update_board(old_posn, piece)
            self.player_2.move()
        else:
            self.error_message(2)
            self.round()

    # Option 3
    @staticmethod
    def quit():
        print("Thank you for playing Chess!")
        sys.exit(0)

    @staticmethod
    def error_message(error):
        if error == 1:
            print(colored("Invalid move. Please try again.", "red"))
        if error == 2:
            print(colored("You have no piece at this location.", "red"))

    @staticmethod
    def successful_move_message(old_posn, piece):
        for letter in "Moving piece ...":
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.1)

        print(colored("\n\nYou successfully moved your {0} from {1}{2} to {3}{4}!".format(
            piece.type, old_posn.x, old_posn.y, piece.posn.x, piece.posn.y), "green"))

    def update_board(self):
        pass

if __name__ == "__main__":
    game = Game()
    game.play()