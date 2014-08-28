__author__ = 'Adam'
from pieces import *


class TestPawn:
    """Test Pawn values"""

    def pytest_funcarg__valid_pawn(self):
        return Pawn(Position('A', '2'), 'white')

    def test_pawn_position(self, valid_pawn):
        assert valid_pawn.posn.x == 'A'
        assert valid_pawn.posn.y == '2'

    def test_pawn_attributes(self, valid_pawn):
        assert valid_pawn.color == 'white'
        assert valid_pawn.shape == 'P'
        assert valid_pawn.value == '2'