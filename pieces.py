__author__ = 'Adam'


class Position():
    """
    Position class used to represent the physical location of a piece.
    Location is based on the x, y position.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Piece():
    """Piece Superclass. All piece objects inherit the Piece class"""

    def __init__(self, position, color):
        self.posn = position
        self.color = color

    def move(self, posn_2):
        """Abstract base class for moving."""
        # self.posn = posn_2
        # print("Your piece moved!")
        # print(self.posn.x, self.posn.y)
        print("Invalid move.")


class Pawn(Piece):
    shape = "P"
    type = "Pawn"
    value = "2"

    def move(self, posn_2):
        """Move pawn 1 space forward, unless on the first move of *this* pawn, then 2 spaces is allowed"""
        # super().move(posn_2)
        if abs(int(posn_2.y) - int(self.posn.y)) <= int(self.value) and posn_2.x == self.posn.x:
            self.posn = posn_2
            return True
        return False


class Knight(Piece):
    shape = "G"
    type = "Knight"
    value = "3"

    def move(self, posn_2):
        """Move Knight in L shape in any direction"""
        super().move(posn_2)


class Rook(Piece):
    shape = "R"
    type = "Rook"
    value = "7"

    def move(self, posn_2):
        """Move Rook * spaces on vertical or horizontal path"""
        # super().move(posn_2)
        if abs(int(posn_2.y) - int(self.posn.y)) <= int(self.value) and posn_2.x == self.posn.x:
            self.posn = posn_2
            return True
        if abs(ord(posn_2.x) - ord(self.posn.x)) <= int(self.value) and posn_2.y == self.posn.y:
            self.posn = posn_2
            return True
        return False


class Bishop(Piece):
    shape = "B"
    type = "Bishop"
    value = "100"

    def move(self, posn_2):
        """Move bishop * spaces on diagonal path"""
        super().move(posn_2)


class Queen(Piece):
    shape = "Q"
    type = "Queen"
    value = "100"

    def move(self, posn_2):
        """Move Queen * spaces in any direction"""
        super().move(posn_2)


class King(Piece):
    shape = "K"
    type = "King"
    value = "1"

    def move(self, posn_2):
        """Move King 1 space in any direction"""
        super().move(posn_2)