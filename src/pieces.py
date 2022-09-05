from typing import Tuple

from .consts import *
from .game_board import GameBoard
from .utils import calc_xy


def can_move(piece_xy: str, target_xy: str, board: GameBoard):
    if piece_xy == target_xy:  # do not allow to skip move by moving to the same xy
        return False

    piece, is_white = board.get_piece(piece_xy)

    stage1 = can_move_stage1(piece, piece_xy, target_xy, board)  # check if chess can move like that
    if not stage1:
        return False

    target_piece, target_is_white = board.get_piece(target_xy)

    if target_piece != ' ' and is_white == target_is_white:  # check if player tries to eat his own chess
        return False

    return can_move_stage2((piece, is_white), piece_xy, target_xy,
                           board)  # check if player tries to jump over his chess


def check_(y, x, is_white: bool, board: GameBoard):
    chess, target_is_white = board.get_piece_xy(y, x)
    return not (chess != ' ' and is_white == target_is_white)


def can_move_stage2(piece: Tuple[str, bool], piece_xy: str, move_xy: str, board: GameBoard):
    y1, x1 = calc_xy(piece_xy)
    y2, x2 = calc_xy(move_xy)

    piece, is_white = piece

    if piece in (BLACK_PAWN, WHITE_PAWN):
        if x1 == x2:
            r = (y1 + 1, y2) if piece == BLACK_PAWN else (y2 - 1, y1, - 1)
            for y in range(*r):
                if not check_(y, x1, is_white, board):
                    return False
            return True

        # x1 != x2, seems like player tries to eat a chess
        return True
    elif piece in (BLACK_ROOK, WHITE_ROOK):
        if x1 == x2:
            ma = max(y1, y2)
            mi = min(y1, y2)
            for y in range(mi + 1, ma):
                if not check_(y, x1, is_white, board):
                    return False
            return True
        else:
            ma = max(x1, x2)
            mi = min(x1, x2)
            for x in range(mi + 1, ma):
                if not check_(y1, x, is_white, board):
                    return False
            return True
    elif piece in (BLACK_KING, WHITE_KING):
        return True
    elif piece in (BLACK_BISHOP, WHITE_BISHOP):
        steps = abs(x1 - x2)

        step_x = -1 if x1 > x2 else 1
        step_y = -1 if y1 > y2 else 1

        for i in range(1, steps):
            if not check_(y1 + i * step_y, x1 + i * step_x, is_white, board):
                return False
        return True
    elif piece in (BLACK_QUEEN, WHITE_QUEEN):
        pass
    elif piece in (BLACK_KNIGHT, WHITE_KNIGHT):
        pass
    else:
        print(piece)
        raise Exception()


def can_move_stage1(piece: str, piece_xy: str, move_xy: str, board: GameBoard):
    y1, x1 = calc_xy(piece_xy)
    y2, x2 = calc_xy(move_xy)

    if piece == BLACK_PAWN:
        if y1 == 1 and y2 in [2, 3] and x1 == x2:
            return True

        if y2 - y1 == 1 and x1 == x2:
            return True

        if y2 - y1 == 1 and abs(x1 - x2) == 1:
            chess, is_white = board.get_piece(piece_xy)
            return chess != ' '

        return False
    elif piece == WHITE_PAWN:
        if y1 == 6 and y2 in [5, 4] and x1 == x2:
            return True

        if y1 - y2 == 1 and x1 == x2:
            return True

        if y1 - y2 == 1 and abs(x1 - x2) == 1:
            chess, is_white = board.get_piece(piece_xy)
            return chess != ' '

        return False
    elif piece in (BLACK_ROOK, WHITE_ROOK):
        return x1 == x2 or y1 == y2
    elif piece in (BLACK_KING, WHITE_KING):
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1
    elif piece in (BLACK_BISHOP, WHITE_BISHOP):
        return abs(x1 - x2) == abs(y1 - y2)
    elif piece in (BLACK_QUEEN, WHITE_QUEEN):
        return abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2
    elif piece in (BLACK_KNIGHT, WHITE_KNIGHT):
        t1 = abs(x1 - x2)
        t2 = abs(y1 - y2)

        return (t1 == 1 and t2 == 2) or (t1 == 2 and t2 == 1)
    else:
        print(piece)
        raise Exception()
