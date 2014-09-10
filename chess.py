__author__ = 'Adam'
import sys
import time
from player import Player
from bot3435 import Bot3435
from pieces import Position


class Game:
    def __init__(self):
        self.player_1 = Player("white")
        self.player_2 = Bot3435("black")
        self.choices = {
            "1": self.print_game_board,
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

    def print_game_board(self):
        """Print the game board to terminal"""
        print("Showing game board")

    @staticmethod
    def error_message(error):
        if error == 1:
            print("Invalid move. Please try again.")
        if error == 2:
            print("You have no piece at this location.")

    @staticmethod
    def successful_move_message(old_posn, piece):
        for letter in "Moving piece ...":
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.3)

        print("\n\nYou successfully moved your {0} from {1}{2} to {3}{4}!".format(
            piece.type, old_posn.x, old_posn.y, piece.posn.x, piece.posn.y))

    def move_piece_from(self):
        print("move piece")
        move = input("Enter the location of the piece you want to move (ex: A2):  ")
        position = Position(move[0], move[1])
        piece_valid = False
        my_piece = ""
        for pieces in self.player_1.pieces:
            for piece in pieces:
                if piece.posn.x == position.x and piece.posn.y == position.y:
                    piece_valid = True
                    my_piece = piece
                    break
        if piece_valid:
            return my_piece
        else:
            self.error_message(2)
            return "False"

    def move(self):
        piece = self.move_piece_from()
        if piece != "False":
            old_posn = piece.posn
            move_2 = input("Enter the location you would like to move your {0}:  ".format(piece.type))
            position_2 = Position(move_2[0], move_2[1])
            is_success = piece.move(position_2)
            if is_success:
                self.successful_move_message(old_posn, piece)
                return True
            else:
                self.error_message(1)
                return False

    def round(self):
        is_success = self.move()
        if is_success:
            self.player_2.move()
        else:
            self.round()

    @staticmethod
    def quit():
        print("Thank you for playing Chess!")
        sys.exit(0)

if __name__ == "__main__":
    game = Game()
    game.play()