import argparse
import logging
import math
from typing import Dict, List, Tuple


def parse_node(node_str) -> Tuple[str, str, str]:
    node_split = node_str.split(" = ")
    node_name = node_split[0]
    node_children_split = node_split[1].split(", ")
    left = node_children_split[0][1:]
    right = node_children_split[1][:-2]
    logging.debug(f"{node_name}, {left}, {right}")
    return node_name, left, right


def main1(file_name):
    graph: Dict[str, Tuple[str, str]] = {}

    with open(file_name, "r") as f:
        path = [*f.readline()][:-1]
        logging.debug(path)
        f.readline()  # empty line
        while node_str := f.readline():
            node, left, right = parse_node(node_str)
            graph[node] = (left, right)
    
    num_steps = 0
    curr_node = "AAA"
    path_idx = 0
    while curr_node != "ZZZ":
        if path[path_idx] == "L":
            curr_node = graph[curr_node][0]
        elif path[path_idx] == "R":
            curr_node = graph[curr_node][1]
        
        path_idx = (path_idx + 1) % len(path)
        num_steps += 1
    
    print(num_steps)
    

def main2(file_name):
    """
    Note: Part 2 is implemented s.t. it assumes that it takes a equal length to
    go from XXA -> XXZ and XXZ -> XXZ. But it's possible these two are different,
    in which case idk how to solve this wheeeee
    """
    graph: Dict[str, Tuple[str, str]] = {}
    start_nodes: List[str] = []

    with open(file_name, "r") as f:
        path = [*f.readline()][:-1]
        logging.debug(path)
        f.readline()  # empty line
        while node_str := f.readline():
            node, left, right = parse_node(node_str)
            graph[node] = (left, right)
            if node[-1] == "A":
                start_nodes.append(node)
    
    num_steps: List[int] = []

    for node in start_nodes: 
        path_idx = 0
        steps = 0
        while node[-1] != "Z":
            if path[path_idx] == "L":
                node = graph[node][0]
            elif path[path_idx] == "R":
                node = graph[node][1]
            
            path_idx = (path_idx + 1) % len(path)
            steps += 1
        
        num_steps.append(steps)

    print(math.lcm(*tuple(num_steps)))
    

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