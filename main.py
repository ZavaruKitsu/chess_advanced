from copy import copy

from src import GAME_BOARD, clear_console, GameBoard, get_move
from src.pieces import can_move

board = GameBoard()


def draw_board():
    clear_console()
    flatten = [item for sublist in board.pieces for item in sublist]

    logs = copy(board.logs)[-8:][::-1]
    if len(logs) < 8:
        logs += ['.'] * (8 - len(logs))

    # take 8 last
    for i, item in enumerate(logs):
        flatten.insert(8 * (i + 1) + i, item)

    print(GAME_BOARD % tuple(flatten))


if __name__ == '__main__':
    err = ''

    while 1:
        draw_board()
        print('    Turn: ' + ('WHITE' if board.white_turn else 'BLACK'))
        print()
        print('  ' + err)
        piece_xy = get_move('  SELECT')

        if piece_xy == 'CLEAR':
            draw_board()
            continue

        piece = board.get_piece(piece_xy)

        if piece[0] == ' ':
            err = 'EMPTY CHESS'
            continue

        if piece[1] != board.white_turn:
            err = 'NOT YOUR CHESS'
            continue

        print(f'  SELECTED {piece[0]}')

        move_xy = get_move('  MOVE')

        if not can_move(piece_xy, move_xy, board):
            err = 'INVALID MOVE'
            continue

        board.move_chess(piece_xy, move_xy)

        err = ''
