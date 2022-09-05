#
# Chess symbols
#

# White
WHITE_KING = '♔'
WHITE_QUEEN = '♕'
WHITE_ROOK = '♖'
WHITE_BISHOP = '♗'
WHITE_KNIGHT = '♘'
WHITE_PAWN = '♙'
WHITE_PIECES = [WHITE_KING, WHITE_QUEEN, WHITE_ROOK, WHITE_BISHOP, WHITE_KNIGHT, WHITE_PAWN]

# Black
BLACK_KING = '♚'
BLACK_QUEEN = '♚'
BLACK_ROOK = '♜'
BLACK_BISHOP = '♝'
BLACK_KNIGHT = '♞'
BLACK_PAWN = '♟'
BLACK_PIECES = [BLACK_KING, BLACK_QUEEN, BLACK_ROOK, BLACK_BISHOP, BLACK_KNIGHT, BLACK_PAWN]

GAME_BOARD = '''
  ┌───┬───┬───┬───┬───┬───┬───┬───┐
8 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │    %s
  ├───┼───┼───┼───┼───┼───┼───┼───┤
7 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │    %s
  ├───┼───┼───┼───┼───┼───┼───┼───┤
6 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │    %s
  ├───┼───┼───┼───┼───┼───┼───┼───┤
5 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │    %s
  ├───┼───┼───┼───┼───┼───┼───┼───┤
4 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │    %s
  ├───┼───┼───┼───┼───┼───┼───┼───┤
3 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │    %s
  ├───┼───┼───┼───┼───┼───┼───┼───┤
2 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │    %s
  ├───┼───┼───┼───┼───┼───┼───┼───┤
1 │ %s │ %s │ %s │ %s │ %s │ %s │ %s │ %s │    %s
  └───┴───┴───┴───┴───┴───┴───┴───┘
    A   B   C   D   E   F   G   H
'''
