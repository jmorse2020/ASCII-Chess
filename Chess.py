from Board import Board
from Piece import Alliance

def is_game_over() -> bool:
    pass

def get_next_move(turn : Alliance):
    pass


def play_game():
    board = Board()
    turn = Alliance.WHITE
    while not is_game_over():
        move = get_next_move(turn)
        board.make_move(move)
        turn = (turn + 1) % 2
