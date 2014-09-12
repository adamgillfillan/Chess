__author__ = 'Adam'

import sys
import time
from pieces import Position
from player import Player
from bot3435 import Bot3435
from termcolor import colored


class Board:
    def __init__(self):
        self.board = self.initialize()
        self.player_1 = Player("white")
        self.player_2 = Bot3435("black")

    def initialize(self):
        """Initialize the game board"""

        board = []
        for i in range(64):
            board.append("X")
        return board

    def print_board(self):
        k = 1
        numbers = '87654321'
        print("\n")
        for i in range(8):
            print("{0}  {1} {2} {3} {4} {5} {6} {7} {8}".format(numbers[i],
                                                                self.board[i+0 + k],
                                                                self.board[i+1 + k],
                                                                self.board[i+2 + k],
                                                                self.board[i+3 + k],
                                                                self.board[i+4 + k],
                                                                self.board[i+5 + k],
                                                                self.board[i+6 + k],
                                                                self.board[i+7 + k],))
            k += 1
        print("   A B C D E F G H")