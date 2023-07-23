from enum import Enum

class Material(Enum):
    PAWN = 1,
    KNIGHT = 2,
    BISHOP = 3,
    ROOK = 4,
    QUEEN = 5,
    KING = 6

class Alliance(Enum):
    WHITE = 1,
    BLACK = 2

class Piece:
    def __init__(self, material=None, alliance=None) -> None:
        self.material = material
        self.alliance = alliance
