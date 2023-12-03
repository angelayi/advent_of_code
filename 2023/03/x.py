import argparse
import logging
from typing import Dict, List, Tuple, Set


def is_symbol(s):
    return s not in (".", "\n") and (not s.isdigit())


def has_symbol(puzzle, r, c) -> bool:
    is_valid = False
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if i >= 0 and i < len(puzzle) and j >= 0 and j < len(puzzle[i]):
                is_valid = is_valid or is_symbol(puzzle[i][j])
    return is_valid


def main1(file_name):
    with open(file_name, "r") as f:
        puzzle: List[List[str]] = []
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
                    is_valid = is_valid or has_symbol(puzzle, r, c)

                else:
                    if is_valid:
                        sum_ += curr_num

                    curr_num = 0
                    is_valid = False
                
                logging.debug(f"{puzzle[r][c]}, {curr_num}, {is_valid}")
                c += 1

        print(sum_)


def has_gears(puzzle, r, c) -> Set[Tuple[int, int]]:
    gears = set()
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if i >= 0 and i < len(puzzle) and j >= 0 and j < len(puzzle[i]):
                if puzzle[i][j] == "*":
                    gears.add((i, j))
    return gears


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
                    gears.update(has_gears(puzzle, r, c))

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