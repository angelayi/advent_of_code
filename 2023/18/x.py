import argparse
import logging


def shoelace_theorem(points):
    area = 0
    for i in range(len(points) - 1):
        area += points[i][0] * points[i + 1][1] - points[i + 1][0] * points[i][1]
    
    # Add the contribution of the last edge
    area += points[len(points) - 1][0] * points[0][1] - points[0][0] * points[len(points) - 1][1]
    
    # Take the absolute value and divide by 2
    area = abs(area) / 2.0
    return area


def picks_theorem(area, num_points):
    return area - (num_points / 2) + 1
    

def main1(file_name):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"

    # direction, length, color
    perimeter = 0
    x, y = (0, 0)
    points = [(x, y)]
    with open(file_name, "r") as f:
        while input := f.readline():
            input_split = input.split(" ")
            direction, distance = input_split[0], int(input_split[1])

            if direction == UP:
                x -= distance
            elif direction == DOWN:
                x += distance
            elif direction == LEFT:
                y -= distance
            elif direction == RIGHT:
                y += distance
            else:
                raise RuntimeError(f"{direction} NYI")

            perimeter += distance       
            points.append((x, y))
    
    logging.debug(points)
    logging.debug(perimeter)

    area = shoelace_theorem(points)
    points_inside = picks_theorem(area, perimeter)
    print(points_inside + perimeter)


def main2(file_name):
    UP = "3"
    DOWN = "1"
    LEFT = "2"
    RIGHT = "0"

    # direction, length, color
    perimeter = 0
    x, y = (0, 0)
    points = [(x, y)]
    with open(file_name, "r") as f:
        while input := f.readline():
            input_split = input.split(" ")
            color = input_split[2][1:-2]
            direction = color[-1]
            distance = int(color[1:-1], 16)

            if direction == UP:
                x -= distance
            elif direction == DOWN:
                x += distance
            elif direction == LEFT:
                y -= distance
            elif direction == RIGHT:
                y += distance
            else:
                raise RuntimeError(f"{direction} NYI")

            perimeter += distance       
            points.append((x, y))
    
    logging.debug(points)
    logging.debug(perimeter)

    area = shoelace_theorem(points)
    points_inside = picks_theorem(area, perimeter)
    print(points_inside + perimeter)
    

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