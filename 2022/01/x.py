import argparse
import logging

def main(file_name):
    with open(file_name, "r") as f:
        inputs = f.read()
        logging.debug(inputs)

    nested_inputs = [elf.split('\n') for elf in inputs.split('\n\n')]
    logging.debug(nested_inputs)
    nested_int_inputs = list(map(lambda inp: list(map(int, inp)), nested_inputs))
    logging.debug(nested_int_inputs)
    sum_inputs = list(map(sum, nested_int_inputs))
    logging.debug(sum_inputs)
    max_input = max(sum_inputs)
    print(max_input)

    sorted_inp = sorted(map(sum, nested_int_inputs))
    logging.debug(sorted_inp)
    last_3 = sorted_inp[-3:]
    logging.debug(last_3)
    last_3_sum = sum(last_3)
    print(last_3_sum)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
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
    main(args.filename)
