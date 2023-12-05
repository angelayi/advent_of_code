import argparse
from collections import defaultdict
import logging


def main1(file_name):
    with open(file_name, "r") as f:
        total_points = 0
        while input := f.readline():
            card_split = input.split(":")
            logging.debug(card_split[0])

            numbers_split = card_split[1].split("|")
            winning_numbers = set(int(n) for n in numbers_split[0].split(" ") if n != "")
            scratched_numbers = set(int(n) for n in numbers_split[1].split(" ") if n != "")
            logging.debug(winning_numbers)
            logging.debug(scratched_numbers)

            intersection = winning_numbers.intersection(scratched_numbers)
            logging.debug(intersection)
            if len(intersection) > 0:
                total_points += 2 ** (len(intersection) - 1)
        
    print(total_points)


def main2(file_name):
    with open(file_name, "r") as f:
        num_scratch = defaultdict(int)
        while input := f.readline():
            card_split = input.split(":")
            card_num = int(card_split[0].split(" ")[-1])
            num_scratch[card_num] += 1
            logging.debug(f"Card {card_num}")

            numbers_split = card_split[1].split("|")
            winning_numbers = set(int(n) for n in numbers_split[0].split(" ") if n != "")
            scratched_numbers = set(int(n) for n in numbers_split[1].split(" ") if n != "")
            logging.debug(winning_numbers)
            logging.debug(scratched_numbers)

            intersection = winning_numbers.intersection(scratched_numbers)
            logging.debug(intersection)
            for i in range(len(intersection)):
                num_scratch[card_num + i + 1] += num_scratch[card_num]
        
        print(sum(num_scratch.values()))
    

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