__author__ = 'Adam'


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

    @staticmethod
    def convert_letter_to_num(posn):
        """Convert a posn.x value from letter to number for indexing in the board array"""
        letters = 'ABCDEFGH'
        i = 0
        for letter in letters:
            if posn.x == letter:
                print(posn.x, letter, i)
                return i
            i += 1

    def update_board(self, from_posn, piece):
        old_x_value = self.convert_letter_to_num(from_posn)
        new_x_value = self.convert_letter_to_num(piece.posn)

        # Must take 8 less the old y value
        # Note: the board's x, y values are switched compared to Piece x, y values >.<
        self.board[8 - int(from_posn.y)][old_x_value] = "X"
        self.board[8 - int(piece.posn.y)][new_x_value] = piece.shape