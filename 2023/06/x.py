import argparse
from collections import defaultdict
import logging
import math


def main1(file_name):
    with open(file_name, "r") as f:
        time_str = f.readline()
        distance_str = f.readline()
    
    times = [int(t) for t in time_str.split(":")[1].split(" ") if t != ""]
    distances = [int(d) for d in distance_str.split(":")[1].split(" ") if d != ""]

    num_ways = 1
    for time, distance in zip(times, distances):
        logging.debug(f"time = {time}, distance = {distance}")

        # total_distance >= (total_time - time_hold) * time_hold
        # time_hold^2 - total_time * time_hold + total_distance >= 0

        time_hold_1 = (time + math.sqrt(time ** 2 - 4 * distance)) / 2
        time_hold_2 = (time - math.sqrt(time ** 2 - 4 * distance)) / 2
        logging.debug(f"{time_hold_2} => {math.floor(time_hold_2)}, {time_hold_1} => {math.ceil(time_hold_1)}")

        ways = math.ceil(time_hold_1) - math.floor(time_hold_2) - 1
        logging.debug(f"ways: {ways}")
        num_ways *= ways
        
    print(num_ways)


def main2(file_name):
    with open(file_name, "r") as f:
        time_str = f.readline()
        distance_str = f.readline()
    
    time = int(time_str.split(":")[1].replace(" ", ""))
    distance = int(distance_str.split(":")[1].replace(" ", ""))
    logging.debug(f"time = {time}, distance = {distance}")

    # total_distance >= (total_time - time_hold) * time_hold
    # time_hold^2 - total_time * time_hold + total_distance >= 0

    time_hold_1 = (time + math.sqrt(time ** 2 - 4 * distance)) / 2
    time_hold_2 = (time - math.sqrt(time ** 2 - 4 * distance)) / 2
    logging.debug(f"{time_hold_2} => {math.floor(time_hold_2)}, {time_hold_1} => {math.ceil(time_hold_1)}")

    ways = math.ceil(time_hold_1) - math.floor(time_hold_2) - 1
    print(ways)

    

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