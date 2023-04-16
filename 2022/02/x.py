import argparse
import logging 


points = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}
compare = {("A", "X"): 3, ("B", "Y"): 3, ("C", "Z"): 3, 
              ("C", "X"): 6, ("A", "Y"): 6, ("B", "Z"): 6, 
              ("B", "X"): 0, ("C", "Y"): 0, ("A", "Z"): 0}
end_points = {"X":0, "Y":3, "Z":6}

def main(file_name):
    with open(file_name, "r") as f:
        inputs = f.read()
        logging.debug(inputs)
    
    rounds = [play.split(' ') for play in inputs.split('\n')]
    logging.debug(rounds)

    me_points = 0
    for elf, me in rounds:
        me_points += points[me]
        me_points += compare[(elf, me)]
    print(me_points)

    me_points = 0
    for elf, me in rounds:
        me_points += end_points[me]

        if compare[(elf, "X")] == end_points[me]:
            me_points += points["X"]
        elif compare[(elf, "Y")] == end_points[me]:
            me_points += points["Y"]
        elif compare[(elf, "Z")] == end_points[me]:
            me_points += points["Z"]
    print(me_points)



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
    main(args.inputfile)