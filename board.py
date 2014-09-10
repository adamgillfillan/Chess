__author__ = 'Adam'

from pieces import Position


class Board:
    def __init__(self):
        self.board = self.initialize()

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
        for element in self.board:
            print("{0}: {1}{2}".format(i, element.x, element.y))
            i += 1