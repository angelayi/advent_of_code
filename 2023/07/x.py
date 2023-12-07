import argparse
from collections import defaultdict
import logging


FIVE = 7
FOUR = 6
FULL_HOUSE = 5
THREE = 4
TWO_PAIR = 3
PAIR = 2
ONE = 1


def rank_hand(num_distinct_values, max_count):
    if num_distinct_values == 5:
        return ONE
    elif num_distinct_values == 4:
        assert max_count == 2
        return PAIR
    elif num_distinct_values == 3:
        if max_count == 2:
            return TWO_PAIR
        elif max_count == 3:
            return THREE
        else:
            raise RuntimeError(f"Got 3 distinct values but got max_count {max_count}")
    elif num_distinct_values == 2:
        if max_count == 4:
            return FOUR
        elif max_count == 3:
            return FULL_HOUSE
        else:
            raise RuntimeError(f"Got 2 distinct values but got max_count {max_count}")
    elif num_distinct_values == 1:
        assert max_count == 5
        return FIVE
    else:
        raise RuntimeError(f"Got {num_distinct_values}")


RANK = "0123456789TJQKA"

def main1(file_name):
    cards_points_bid = []
    with open(file_name, "r") as f:
        while input_str := f.readline():
            input_split = input_str.split(" ")
            cards = input_split[0]
            bid = int(input_split[1])
            logging.debug(f"{cards} {bid}")

            values = [RANK.index(c) for c in cards]
            count_values = defaultdict(int)
            for v in values:
                count_values[v] += 1

            max_count = max(count_values.values())
            num_distinct_values = len(count_values)

            hand_rank = rank_hand(num_distinct_values, max_count)
            cards_points_bid.append((hand_rank, values, bid))
                
    sorted_cards = sorted(cards_points_bid, key=lambda a: (a[0], a[1]))
    logging.debug(sorted_cards)

    total_points = 0
    for i, (_, _, bid) in enumerate(sorted_cards):
        total_points += (i + 1) * bid
        
    print(total_points)


# J is considered smallest now
JOKER_RANK = "0J23456789T1QKA"

def main2(file_name):
    cards_points_bid = []
    with open(file_name, "r") as f:
        while input_str := f.readline():
            input_split = input_str.split(" ")
            cards = input_split[0]
            bid = int(input_split[1])
            logging.debug(f"{cards} {bid}")

            values = [JOKER_RANK.index(c) for c in cards]
            count_values = defaultdict(int)
            for v in values:
                count_values[v] += 1

            num_joker = count_values[1]
            non_joker_counts = [c for v, c in count_values.items() if v != 1]
            if len(non_joker_counts) == 0:
                max_count = num_joker
                num_distinct_values = 1
            else:
                max_count = max(non_joker_counts) + num_joker
                num_distinct_values = len(count_values) - int(num_joker != 0)
            
            hand_rank = rank_hand(num_distinct_values, max_count)
            cards_points_bid.append((hand_rank, values, bid))
                
    sorted_cards = sorted(cards_points_bid, key=lambda a: (a[0], a[1]))
    logging.debug(sorted_cards)

    total_points = 0
    for i, (_, _, bid) in enumerate(sorted_cards):
        total_points += (i + 1) * bid
        
    print(total_points)
    

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
