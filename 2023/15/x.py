import argparse
from collections import OrderedDict
import logging
from typing import Dict


def hash(seq):
    val = 0
    for c in seq:
        val = ((val + ord(c)) * 17) % 256
    return val


def main1(file_name):
    with open(file_name, "r") as f:
        input = f.readline()
    
    total_points = 0
    for seq in input.split(","):
        logging.debug(seq)
        hash_val = hash(seq)
        logging.debug(hash_val)
        total_points += hash_val

    print(total_points)


def main2(file_name):
    with open(file_name, "r") as f:
        input = f.readline()
    
    # box_number -> {label -> focal_length}
    boxes: Dict[int, OrderedDict[str, int]] = {}
    for seq in input.split(","):
        logging.debug(seq)
        if "-" in seq:
            label = seq[:-1]
            box_num = hash(label)
            logging.debug(box_num)
            
            if box_num not in boxes:
                continue

            lens_slots = boxes[box_num]
            
            if label not in lens_slots:
                continue

            del lens_slots[label]

        elif "=" in seq:
            label, focal_length = seq.split("=")
            box_num = hash(label)
            logging.debug(box_num)
            
            if box_num not in boxes:
                boxes[box_num] = OrderedDict()
            
            lens_slots = boxes[box_num]
            lens_slots[label] = int(focal_length)
        else:
            raise RuntimeError(f"bad {seq}")

        logging.debug(boxes)

    focusing_power = 0
    for b, labels in boxes.items():
        for i, focal_length in enumerate(labels.values()):
            logging.debug(f"{b + 1} {i + 1} {focal_length}")
            focusing_power += (b + 1) * (i + 1) * focal_length
    print(focusing_power)
    

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