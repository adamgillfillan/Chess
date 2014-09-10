__author__ = 'Adam'

import sys
import time
from pieces import Position
from player import Player
from bot3435 import Bot3435


class Board:
    def __init__(self):
        self.board = self.initialize()
        self.player_1 = Player("white")
        self.player_2 = Bot3435("black")

    def initialize(self):
        """Initialize the game board"""

        board = []
        chess_alphabet = 'ABCDEFGH'
        for i in range(1, 9):
            for letter in chess_alphabet:
                board.append(Position(letter, str(i)))

        return board

    def print_board_test(self):
        i = 0
        for element in self.board:
            print("{0}: {1}{2}".format(i, element.x, element.y))
            i += 1

    def print_board(self):
        i = 0
        chess_alphabet = 'ABCDEFGH'
        for i in range(8, 0, -1):
            print("{0}  ".format(i))

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
                if piece.posn.x == position.x and piece.posn.y == position.y:  # Does a valid piece exist here?
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