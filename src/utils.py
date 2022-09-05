import os

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_move(prompt: str):
    while 1:
        print()
        print(prompt)
        try:
            move = input('> ')
        except KeyboardInterrupt:
            clear_console()

            print('Game has ended!')
            print()

            exit(-1)

        if move.upper() == 'CLEAR':
            return move

        if len(move) != 2:
            print('  ' + '^' * len(move))
            print('  Wrong sequence')
            continue

        correct1 = move[0].upper() in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        correct2 = move[1] in [str(i) for i in range(1, 9)]

        if not correct1 or not correct2:
            print(f'  {" " if correct1 else "^"}{" " if correct2 else "^"}')
            print('  Wrong sequence')
            continue

        return move.upper()


def calc_xy(piece_xy: str):
    return 8 - int(piece_xy[1]), alphabet.index(piece_xy[0])
