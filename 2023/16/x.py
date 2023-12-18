import argparse
from collections import defaultdict
from enum import Enum
import logging
from typing import List, Tuple, Optional


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def reflect(self, beam):
        if beam == "/":
            if self == Direction.RIGHT:
                return Direction.UP
            elif self == Direction.UP:
                return Direction.RIGHT
            elif self == Direction.DOWN:
                return Direction.LEFT
            elif self == Direction.LEFT:
                return Direction.DOWN
            else:
                raise RuntimeError(f"{self}")
        elif beam == "\\":
            if self == Direction.RIGHT:
                return Direction.DOWN
            elif self == Direction.UP:
                return Direction.LEFT
            elif self == Direction.DOWN:
                return Direction.RIGHT
            elif self == Direction.LEFT:
                return Direction.UP
            else:
                raise RuntimeError(f"{self}")
        return self()


def pprint(grid, visited=None):
    if logging.DEBUG <= logging.root.level:
        return
    
    visited_pos = set(i[0] for i in visited) if visited is not None else None
    s = ""
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if visited is not None and (i, j) in visited_pos:
                s += f"x "
            else:
                s += f"{val} "
        s += "\n"
    logging.debug(f"\n{s}")
    return s


def get_next_move(pos, direction, grid) -> Optional[Tuple[int, int]]:
    new_pos = None
    if direction == Direction.UP:
        if pos[0] != 0:
            new_pos = (pos[0] - 1, pos[1])
    elif direction == Direction.DOWN:
        if pos[0] != len(grid) - 1:
            new_pos = (pos[0] + 1, pos[1])
    elif direction == Direction.LEFT:
        if pos[1] != 0:
            new_pos = (pos[0], pos[1] - 1)
    elif direction == Direction.RIGHT:
        if pos[1] != len(grid[0]) - 1:
            new_pos = (pos[0], pos[1] + 1)
    else:
        raise RuntimeError(f"{direction}")
    return new_pos


def get_next_moves(pos, direction, grid) -> List[Tuple[Tuple[int, int], Direction]]:
    moves = []
    
    pos_value = grid[pos[0]][pos[1]]

    if pos_value == "|":
        if direction in [Direction.UP, Direction.DOWN]:
            next_pos = get_next_move(pos, direction, grid)
            if next_pos is not None:
                moves.append((next_pos, direction))
        
        else:
            for new_direction in [Direction.UP, Direction.DOWN]:
                next_pos = get_next_move(pos, new_direction, grid)
                if next_pos is not None:
                    moves.append((next_pos, new_direction))

    elif pos_value == "-":
        if direction in [Direction.LEFT, Direction.RIGHT]:
            next_pos = get_next_move(pos, direction, grid)
            if next_pos is not None:
                moves.append((next_pos, direction))

        else:
            for new_direction in [Direction.LEFT, Direction.RIGHT]:
                next_pos = get_next_move(pos, new_direction, grid)
                if next_pos is not None:
                    moves.append((next_pos, new_direction))

    elif pos_value in ("/", "\\"):
        new_direction = direction.reflect(pos_value)
        next_pos = get_next_move(pos, new_direction, grid)
        if next_pos is not None:
            moves.append((next_pos, new_direction))
    
    else:
        next_pos = get_next_move(pos, direction, grid)
        if next_pos is not None:
            moves.append((next_pos, direction))
    
    return moves


def main1(file_name):
    grid = []
    with open(file_name, "r") as f:
        while input := f.readline():
            grid.append([*input[:-1]])
    pprint(grid)

    moves = {((0, 0), Direction.RIGHT)}
    visited = set()
    while moves:
        pos, direction = moves.pop()
        visited.add((pos, direction))
        next_moves = get_next_moves(pos, direction, grid)
        pprint(grid, visited)
        logging.debug(f"{pos}, {next_moves}\n")
        for next_move in next_moves:
            if next_move not in visited:
                moves.add(next_move)
        
    print(len(set(i[0] for i in visited)))


def main2(file_name):
    grid = []
    with open(file_name, "r") as f:
        while input := f.readline():
            grid.append([*input[:-1]])
    pprint(grid)

    start_moves = [((0, i), Direction.DOWN) for i in range(len(grid[0]))]
    start_moves.extend([((i, 0), Direction.RIGHT) for i in range(len(grid))])
    start_moves.extend([((len(grid) - 1, i), Direction.UP) for i in range(len(grid[0]))])
    start_moves.extend([((i, len(grid[0]) - 1), Direction.LEFT) for i in range(len(grid))])

    best = 0
    for start in start_moves:
        moves = {start}
        visited = set()
        while moves:
            pos, direction = moves.pop()
            visited.add((pos, direction))
            next_moves = get_next_moves(pos, direction, grid)
            pprint(grid, visited)
            logging.debug(f"{pos}, {next_moves}\n")
            for next_move in next_moves:
                if next_move not in visited:
                    moves.add(next_move)
            
        num_energized = len(set(i[0] for i in visited))
        if num_energized > best:
            best = num_energized
    
    print(best)
    

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