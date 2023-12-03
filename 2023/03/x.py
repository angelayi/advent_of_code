import argparse
import logging
from typing import Dict, List, Tuple, Set


def is_symbol(s):
    return s not in (".", "\n") and (not s.isdigit())


def main1(file_name):
    with open(file_name, "r") as f:
        puzzle = []
        while input := f.readline():
            puzzle.append([*input])
        
        logging.debug(puzzle)

        sum_ = 0

        for r in range(len(puzzle)):
            c = 0
            curr_num = 0
            is_valid = False
            while c < len(puzzle[r]):
                if puzzle[r][c].isdigit():
                    curr_num = curr_num * 10 + int(puzzle[r][c])

                    if c > 0:
                        left = puzzle[r][c-1]
                        logging.debug(f"left: {left}, {is_symbol(left)}")
                        is_valid = is_valid or is_symbol(left)

                        if r > 0:
                            left_up = puzzle[r - 1][c - 1]
                            logging.debug(f"left_up: {left_up}, {is_symbol(left_up)}")
                            is_valid = is_valid or is_symbol(left_up)

                        if r < len(puzzle) - 1:
                            left_down = puzzle[r + 1][c - 1]
                            logging.debug(f"left_down: {left_down}, {is_symbol(left_down)}")
                            is_valid = is_valid or is_symbol(left_down)

                    if c < len(puzzle[r]) - 1:
                        right = puzzle[r][c + 1]
                        logging.debug(f"right: {right}, {is_symbol(right)}")
                        is_valid = is_valid or is_symbol(right)

                        if r > 0:
                            right_up = puzzle[r - 1][c + 1]
                            logging.debug(f"right_up: {right_up}, {is_symbol(right_up)}")
                            is_valid = is_valid or is_symbol(right_up)

                        if r < len(puzzle) - 1:
                            right_down = puzzle[r + 1][c + 1]
                            logging.debug(f"right_down: {right_down}, {is_symbol(right_down)}")
                            is_valid = is_valid or is_symbol(right_down)

                    if r > 0:
                        up = puzzle[r - 1][c]
                        logging.debug(f"up: {up}, {is_symbol(up)}")
                        is_valid = is_valid or is_symbol(up)

                    if r < len(puzzle) - 1:
                        down = puzzle[r + 1][c]
                        logging.debug(f"down: {down}, {is_symbol(down)}")
                        is_valid = is_valid or is_symbol(down)

                else:
                    if is_valid:
                        sum_ += curr_num

                    curr_num = 0
                    is_valid = False
                
                logging.debug(f"{puzzle[r][c]}, {curr_num}, {is_valid}")
                c += 1

        print(sum_)


def main2(file_name):
    with open(file_name, "r") as f:
        puzzle = []
        while input := f.readline():
            puzzle.append([*input])
        
        logging.debug(puzzle)

        possible_gears: Dict[Tuple[int, int], List[int]] = {}

        for r in range(len(puzzle)):
            c = 0
            curr_num = 0
            gears: Set[Tuple[int, int]] = set()
            while c < len(puzzle[r]):
                if puzzle[r][c].isdigit():
                    curr_num = curr_num * 10 + int(puzzle[r][c])

                    if c > 0:
                        left = puzzle[r][c-1]
                        logging.debug(f"left: {left}, {is_symbol(left)}")
                        if left == "*":
                            gears.add((r, c - 1))

                        if r > 0:
                            left_up = puzzle[r - 1][c - 1]
                            logging.debug(f"left_up: {left_up}, {is_symbol(left_up)}")
                            if left_up == "*":
                                gears.add((r - 1, c - 1))

                        if r < len(puzzle) - 1:
                            left_down = puzzle[r + 1][c - 1]
                            logging.debug(f"left_down: {left_down}, {is_symbol(left_down)}")
                            if left_down == "*":
                                gears.add((r + 1, c - 1))

                    if c < len(puzzle[r]) - 1:
                        right = puzzle[r][c + 1]
                        logging.debug(f"right: {right}, {is_symbol(right)}")
                        if right == "*":
                            gears.add((r, c + 1))

                        if r > 0:
                            right_up = puzzle[r - 1][c + 1]
                            logging.debug(f"right_up: {right_up}, {is_symbol(right_up)}")
                            if right_up == "*":
                                gears.add((r - 1, c + 1))

                        if r < len(puzzle) - 1:
                            right_down = puzzle[r + 1][c + 1]
                            logging.debug(f"right_down: {right_down}, {is_symbol(right_down)}")
                            if right_down == "*":
                                gears.add((r + 1, c + 1))

                    if r > 0:
                        up = puzzle[r - 1][c]
                        logging.debug(f"up: {up}, {is_symbol(up)}")
                        if up == "*":
                            gears.add((r - 1, c))

                    if r < len(puzzle) - 1:
                        down = puzzle[r + 1][c]
                        logging.debug(f"down: {down}, {is_symbol(down)}")
                        if down == "*":
                            gears.add((r + 1, c))

                else:
                    if len(gears) > 0:
                        logging.debug(f"gears: {gears}")
                        for gear in gears:
                            adj_nums = possible_gears.get(gear, [])
                            adj_nums.append(curr_num)
                            possible_gears[gear] = adj_nums
                        logging.debug(f"possible gears: {possible_gears}")

                    curr_num = 0
                    gears = set()
                
                
                logging.debug(f"{puzzle[r][c]}, {curr_num}")
                c += 1

        logging.debug(f"possible gears: {possible_gears}")
        sum_ = 0
        for adj_nums in possible_gears.values():
            if len(adj_nums) == 2:
                sum_ += adj_nums[0] * adj_nums[1]

        print(sum_)
    

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