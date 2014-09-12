__author__ = 'Adam'
from board import Board
from pieces import Position


class TestBoard:
    """Test Board functions"""

    board = Board()

    def test_convert_letter_to_num(self):
        letters = 'ABCDEFGH'
        i = 0
        for letter in letters:
            assert self.board.convert_letter_to_num(Position(letter, 1)) == i
            i += 1