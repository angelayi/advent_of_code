import argparse
import logging


def pprint(board, print_=False):
    s = ""
    for row in board:
        for col in row:
            s += f"{col} "
        s += "\n"

    logging.debug(f"\n{s}")   
    return s


def tilt_west(board):
    new_board = [["." for _ in range(len(board))] for _ in range(len(board[0]))]
    for j, col in enumerate(board):
        load = 0
        for i, val in enumerate(col):
            if val == "O":
                new_board[j][load] = "O"
                load += 1
            elif val == "#":
                new_board[j][i] = "#"
                load = i + 1
    
    logging.debug("tilt west")
    pprint(new_board)
    return new_board


def rotate_ccw(board):
    rotated_board = [["." for _ in range(len(board))] for _ in range(len(board[0]))]
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            rotated_board[len(board) - j - 1][i] = val

    logging.debug("rotate counter-clockwise")
    pprint(rotated_board)
    return rotated_board


def rotate_cw(board):
    rotated_board = [["." for _ in range(len(board))] for _ in range(len(board[0]))]
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            rotated_board[j][len(board) - i - 1] = val

    logging.debug("rotate clockwise")
    pprint(rotated_board)
    return rotated_board


def count_points(board):
    total_points = 0
    for row in board:
        for i, val in enumerate(row):
            if val == "O":
                total_points += (len(board) - i)
    
    return total_points


def main1(file_name):
    with open(file_name, "r") as f:
        board = []
        while input := f.readline():
            board.append([*input[:-1]])
    
    pprint(board)
    board = rotate_ccw(board)
    board = tilt_west(board)
    print(count_points(board))


def main2(file_name):
    BIG_NUM = 1000000000

    with open(file_name, "r") as f:
        board = []
        while input := f.readline():
            board.append([*input[:-1]])

    pprint(board)
    board = rotate_ccw(board)

    memo = {}
    for i in range(BIG_NUM):
        for _ in range(4):
            board = tilt_west(board)
            board = rotate_cw(board)

        board_str = pprint(board, True)
        if board_str in memo:
            break
        else:
            memo[board_str] = i

    num_cycles = i - memo[board_str]
    cycles_left = (BIG_NUM - i - 1) % num_cycles
    logging.debug("iter:", i)
    logging.debug("num_cycles:", num_cycles)
    logging.debug("cycles_left:", cycles_left)

    for _ in range(cycles_left):
        for _ in range(4):
            board = tilt_west(board)
            board = rotate_cw(board)

    print(count_points(board))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',
                        '--problem',
                        default='1',
                        help='Provide problem number. Example --problem 1, default=1')
    parser.add_argument('-log',
                        '--loglevel',
                        default='warning',
                        help='Provide logging level. Example --loglevel debug, default=warning' )
    parser.add_argument('-file',
                        '--inputfile',
                        required=True,
                        help='Provide input file name. Example --inputfile "input.txt"' )

    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel.upper())
    if args.problem == '1':
        main1(args.inputfile)
    elif args.problem == '2':
        main2(args.inputfile)