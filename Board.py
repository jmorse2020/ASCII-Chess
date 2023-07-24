from Piece import *

class Board:
    _boardState = [[]]

    def __init__(self) -> None:
        pass

    def reset_board(self):
        self._boardState = [[None for _ in range(8)] for _ in range(8)]
        self._boardState = [
            [Piece(Material.ROOK, Alliance.BLACK), Piece(Material.KNIGHT, Alliance.BLACK), Piece(Material.BISHOP, Alliance.BLACK), Piece(Material.QUEEN, Alliance.BLACK),
             Piece(Material.KING, Alliance.BLACK), Piece(Material.BISHOP, Alliance.BLACK), Piece(Material.KNIGHT, Alliance.BLACK), Piece(Material.ROOK, Alliance.BLACK)],
            [Piece(Material.PAWN, Alliance.BLACK) for _ in range(8)],
            [None for y in range(8)] for x in range(4),
            [Piece(Material.PAWN, Alliance.WHITE) for _ in range(8)]
            [Piece(Material.ROOK, Alliance.WHITE), Piece(Material.KNIGHT, Alliance.WHITE), Piece(Material.BISHOP, Alliance.WHITE), Piece(Material.QUEEN, Alliance.WHITE),
             Piece(Material.KING, Alliance.WHITE), Piece(Material.BISHOP, Alliance.WHITE), Piece(Material.KNIGHT, Alliance.WHITE), Piece(Material.ROOK, Alliance.WHITE)]            
        ]

    def get_piece_at(self, x, y):
        pass

    def get_moves(self, piece : Piece):
        pass

    def make_move(self,):
        pass