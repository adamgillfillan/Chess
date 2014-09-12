__author__ = 'Adam'
from pieces import *
from board import Board


class Player:

    def __init__(self, color):
        self.color = color
        if color == 'white':
            self.pawns = [Pawn(Position('A', '2'), color),
                          Pawn(Position('B', '2'), color),
                          Pawn(Position('C', '2'), color),
                          Pawn(Position('D', '2'), color),
                          Pawn(Position('E', '2'), color),
                          Pawn(Position('F', '2'), color),
                          Pawn(Position('G', '2'), color),
                          Pawn(Position('H', '2'), color)]
            self.knights = [Knight(Position('B', '1'), color),
                            Knight(Position('G', '1'), color)]
            self.bishops = [Bishop(Position('C', '1'), color),
                            Bishop(Position('F', '1'), color)]
            self.rooks = [Rook(Position('A', '1'), color),
                          Rook(Position('H', '1'), color)]
            self.queen = [Queen(Position('D', '1'), color)]
            self.king = [King(Position('E', '1'), color)]
        else:
            self.pawns = [Pawn(Position('A', '7'), color),
                          Pawn(Position('B', '7'), color),
                          Pawn(Position('C', '7'), color),
                          Pawn(Position('D', '7'), color),
                          Pawn(Position('E', '7'), color),
                          Pawn(Position('F', '7'), color),
                          Pawn(Position('G', '7'), color),
                          Pawn(Position('H', '7'), color)]
            self.knights = [Knight(Position('B', '8'), color),
                            Knight(Position('G', '8'), color)]
            self.bishops = [Bishop(Position('C', '8'), color),
                            Bishop(Position('F', '8'), color)]
            self.rooks = [Rook(Position('A', '8'), color),
                          Rook(Position('H', '8'), color)]
            self.queen = [Queen(Position('D', '8'), color)]
            self.king = [King(Position('E', '8'), color)]
        self.pieces = []
        self.pieces.append(self.pawns)
        self.pieces.append(self.knights)
        self.pieces.append(self.bishops)
        self.pieces.append(self.rooks)
        self.pieces.append(self.queen)
        self.pieces.append(self.king)

    def move_piece_from(self):
        print("move piece")
        move = input("Enter the location of the piece you want to move (ex: A2):  ")
        position = Position(move[0], move[1])
        piece_valid = False
        my_piece = ""
        for pieces in self.pieces:
            for piece in pieces:
                if piece.posn.x == position.x and piece.posn.y == position.y:  # Does a valid piece exist here?
                    piece_valid = True
                    my_piece = piece
                    break
        if piece_valid:
            return my_piece
        else:
            return "False"

    def move(self):
        piece = self.move_piece_from()
        if piece != "False":
            old_posn = piece.posn
            move_2 = input("Enter the location you would like to move your {0}:  ".format(piece.type))
            position_2 = Position(move_2[0], move_2[1])
            is_success = piece.move(position_2)
            if is_success:
                return True, old_posn, piece
            else:
                return False