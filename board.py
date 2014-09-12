__author__ = 'Adam'

from pieces import *


class Board:
    def __init__(self):
        self.board = self.initialize()

    def initialize(self):
        """Initialize the game board"""
        board = [["X" for i in range(8)] for j in range(8)]

        for i in range(8):
            board[1][i] = "P"
            board[6][i] = "P"

        for i in range(0, 8, 7):
            board[i][0] = "R"
            board[i][1] = "G"
            board[i][2] = "B"
            board[i][3] = "Q"
            board[i][4] = "K"
            board[i][5] = "B"
            board[i][6] = "G"
            board[i][7] = "R"
        return board

    def print_board(self):
        k = 1
        numbers = '87654321'
        print()
        for i in range(8):
            print(numbers[i], end="  ")
            for k in range(8):
                print(self.board[i][k], end=" ")
            print()
        print("   A B C D E F G H")

    # def update_board(self, list_of_pieces_1, list_of_pieces_2):
    #     for pieces in list_of_pieces_1:
    #         for piece in pieces:
    #             if piece.posn.x

    def convert_letter_to_num(self, posn):
        letters = 'ABCDEFGH'
        i = 0
        for letter in letters:
            if posn.x == letter:
                return i
            i += 1

    def update_board(self, from_posn, to_posn):
        x_value = self.convert_letter_to_num(from_posn)
        for i in range(8):
            for k in range(8):
                if self.board[i][k] == from_posn.x:
                    pass