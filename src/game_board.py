from typing import Tuple

from .consts import *
from .utils import calc_xy


class GameBoard:
    def __init__(self):
        self.pieces = []
        self.pieces.append(
            [BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEEN, BLACK_KING, BLACK_BISHOP, BLACK_KNIGHT, BLACK_ROOK])
        self.pieces.append([BLACK_PAWN] * 8)
        self.pieces.append([' '] * 8)
        self.pieces.append([' '] * 8)
        self.pieces.append([' '] * 8)
        self.pieces.append([' '] * 8)
        self.pieces.append([WHITE_PAWN] * 8)
        self.pieces.append(
            [WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEEN, WHITE_KING, WHITE_BISHOP, WHITE_KNIGHT, WHITE_ROOK])

        self.logs = []

        self.white_turn = True

    def get_piece(self, piece_xy: str) -> Tuple[str, bool]:  # (symbol, is_white)
        x, y = calc_xy(piece_xy)

        return self.get_piece_xy(x, y)

    def get_piece_xy(self, x: int, y: int) -> Tuple[str, bool]:  # (symbol, is_white)
        piece = self.pieces[x][y]

        return piece, piece in WHITE_PIECES

    def move_chess(self, piece_xy: str, move_xy: str):
        self.white_turn = not self.white_turn

        piece_x, piece_y = calc_xy(piece_xy)
        move_x, move_y = calc_xy(move_xy)

        self.pieces[move_x][move_y] = self.pieces[piece_x][piece_y]
        self.pieces[piece_x][piece_y] = ' '

        self.logs.append(f'{piece_xy} → {move_xy}')
