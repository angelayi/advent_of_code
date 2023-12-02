import argparse
import logging 


def main1(file_name):
    with open(file_name, "r") as f:
        calibration_sum = 0
        while input := f.readline():
            logging.debug(input)

            first_num = None
            for i in input:
                if str(i).isdigit():
                    first_num = int(i)
                    break
            
            last_num = None
            for i in reversed(input):
                if str(i).isdigit():
                    last_num = int(i)
                    break
            
            logging.debug(f"{first_num}, {last_num}")
            calibration_sum += first_num * 10 + last_num

        print(calibration_sum)


DIGIT_NUMS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def main2(file_name):
    with open(file_name, "r") as f:
        calibration_sum = 0
        while input := f.readline():
            logging.debug(input)

            parsed_input = []
            index = 0
            while index < len(input):
                if str(input[index]).isdigit():
                    parsed_input.append(int(input[index]))
                    index += 1
                    continue

                if index < len(input) - 3:
                    if input[index:index + 3] in DIGIT_NUMS.keys():
                        logging.debug(f"3: {input[index:index + 3]}")
                        parsed_input.append(DIGIT_NUMS[input[index:index + 3]])
                        index += 2
                        continue

                if index < len(input) - 4:
                    if input[index:index + 4] in DIGIT_NUMS.keys():
                        logging.debug(f"4: {input[index:index + 4]}")
                        parsed_input.append(DIGIT_NUMS[input[index:index + 4]])
                        index += 3
                        continue
                
                if index < len(input) - 5:
                    if input[index:index + 5] in DIGIT_NUMS.keys():
                        logging.debug(f"5: {input[index:index + 5]}")
                        parsed_input.append(DIGIT_NUMS[input[index:index + 5]])
                        index += 4
                        continue

                index += 1
            
            logging.debug(parsed_input)
        
            logging.debug(f"{parsed_input[0]}, {parsed_input[-1]}")
            logging.debug("\n")
            calibration_sum += parsed_input[0] * 10 + parsed_input[-1]

    print(calibration_sum)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-problem',
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
