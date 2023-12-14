import argparse
from collections import defaultdict
import logging

def get_common_val(nums):
    common_val = nums[0]
    for n in nums:
        if n != common_val:
            return None
    return common_val

def main1(file_name):
    with open(file_name, "r") as f:
        total_points = 0
        while input_str := f.readline():
            input = [int(s) for s in input_str.split(" ")]

            def subtract(nums):
                logging.debug(nums)
                subtracted = [nums[i  + 1] - nums[i] for i in range(len(nums) - 1)]

                if common_val := get_common_val(subtracted):
                    logging.debug(f"return1: {common_val}")
                    return common_val
            
                update_val = subtract(subtracted)
                logging.debug(f"return2: {subtracted[-1] + update_val}")
                return subtracted[-1] + update_val
            
            update_val = subtract(input)
            logging.debug(f"update_val: {update_val}")
            updated_val = input[-1] + update_val
            logging.debug(f"updated_val: {updated_val}")
            total_points += updated_val
        
    print(total_points)


def main2(file_name):
    with open(file_name, "r") as f:
        total_points = 0
        while input_str := f.readline():
            input = [int(s) for s in input_str.split(" ")]

            def subtract(nums):
                logging.debug(nums)
                subtracted = [nums[i  + 1] - nums[i] for i in range(len(nums) - 1)]

                if common_val := get_common_val(subtracted):
                    logging.debug(f"return1: {common_val}")
                    return common_val
            
                update_val = subtract(subtracted)
                logging.debug(f"return2: {subtracted[0] - update_val}")
                return subtracted[0] - update_val
            
            update_val = subtract(input)
            logging.debug(f"update_val: {update_val}")
            updated_val = input[0] - update_val
            logging.debug(f"updated_val: {updated_val}")
            total_points += updated_val
        
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