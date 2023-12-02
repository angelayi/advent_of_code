import argparse
import logging 


def main1(file_name):
    with open(file_name, "r") as f:
        NUM_RED = 12
        NUM_GREEN = 13
        NUM_BLUE = 14

        good_games = 0
        while input := f.readline():

            input_split = input.split(":")
            game_num = int(input_split[0].split(" ")[1])
            logging.debug(f"Game {game_num}")

            valid = True
            sets_split = input_split[1].split(";")
            for set_str in sets_split:
                cubes = set_str.split(",")
                for cube_str in cubes:
                    cube_split = cube_str.split(" ")
                    num_cube = int(cube_split[1])
                    cube_color = cube_split[2]

                    if "red" in cube_color and num_cube > NUM_RED:
                        valid = False
                    elif "green" in cube_color and num_cube > NUM_GREEN:
                        valid = False
                    elif "blue" in cube_color and num_cube > NUM_BLUE:
                        valid = False

                    logging.debug(f"{num_cube}, {cube_color}, {valid}")
                    if not valid:
                        break
                
                if not valid:
                    break
            
            if valid:
                good_games += game_num
        
        print(good_games)


def main2(file_name):
    with open(file_name, "r") as f:
        power_total = 0
        while input := f.readline():

            input_split = input.split(":")
            game_num = int(input_split[0].split(" ")[1])
            logging.debug(f"Game {game_num}")

            max_red = 0
            max_blue = 0
            max_green = 0
            sets_split = input_split[1].split(";")
            for set_str in sets_split:
                cubes = set_str.split(",")
                for cube_str in cubes:
                    cube_split = cube_str.split(" ")
                    num_cube = int(cube_split[1])
                    cube_color = cube_split[2]

                    if "red" in cube_color:
                        max_red = max(max_red, num_cube)
                    elif "green" in cube_color:
                        max_green = max(max_green, num_cube)
                    elif "blue" in cube_color:
                        max_blue = max(max_blue, num_cube)

            logging.debug(f"{max_red}, {max_blue}, {max_green}")
            power_total += max_red * max_blue * max_green
            
        
        print(power_total)
    

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