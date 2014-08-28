__author__ = 'Adam'
from pieces import *


class TestPiece:
    """Test Piece values"""

    def pytest_funcarg__valid_piece(self):
        return {'Pawn':   Pawn(Position('A', '2'), 'white'),
                'Knight': Knight(Position('A', '2'), 'white'),
                'Rook':   Rook(Position('A', '2'), 'white'),
                'Bishop': Bishop(Position('A', '2'), 'white'),
                'Queen':  Queen(Position('A', '2'), 'white'),
                'King':   King(Position('A', '2'), 'white')}

    def assert_attributes(self, piece, shape, value, type):
        assert piece.shape == shape
        assert piece.value == value
        assert piece.type == type

    def test_piece_position(self, valid_piece):
        for key, piece in valid_piece.items():
            print(" Piece: {0}\n ".format(key))
            assert piece.posn.x == 'A'
            assert piece.posn.y == '2'

    def test_piece_attributes(self, valid_piece):
        for key, piece in valid_piece.items():
            assert piece.color == 'white'
            if key == 'Pawn':
                self.assert_attributes(piece, 'P', '2', key)
            elif key == "Knight":
                self.assert_attributes(piece, 'G', '3', key)
            elif key == "Rook":
                self.assert_attributes(piece, 'R', '7', key)
            elif key == "Bishop":
                self.assert_attributes(piece, 'B', '7', key)
            elif key == "Queen":
                self.assert_attributes(piece, 'Q', '7', key)
            elif key == "King":
                self.assert_attributes(piece, 'K', '1', key)