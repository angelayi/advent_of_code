import argparse
from collections import defaultdict
import logging


def main1(file_name):
    with open(file_name, "r") as f:
        seeds_str = f.readline()
        seeds = [int(s) for s in seeds_str.split(":")[1].split(" ") if s != ""]
        seeds = sorted(seeds)
        logging.debug(seeds)
        f.readline()  # first empty line

        for _ in range(7):
            ranges = []
            map_name = f.readline()  # name
            logging.debug(map_name[:-1])
            while input_str := f.readline():
                if input_str == "\n":
                    break
                
                maps = tuple(int(s) for s in input_str.split(" "))
                ranges.append(maps)
            
            logging.debug(ranges)
            ranges = sorted(ranges, key=lambda a: a[1])

            new_seeds = []
            map_idx = 0
            seed_idx = 0
            while seed_idx < len(seeds) and map_idx < len(ranges):
                s = seeds[seed_idx]
                while map_idx < len(ranges):
                    if s < ranges[map_idx][1]:
                        logging.debug(f"HERE1 {s}, {ranges[map_idx]}, {s}")
                        new_seeds.append(s)
                        seed_idx += 1
                        break
                    elif s >= ranges[map_idx][1] and s < ranges[map_idx][1] + ranges[map_idx][2]:
                        logging.debug(f"HERE2 {s}, {ranges[map_idx]}, {s + ranges[map_idx][0] - ranges[map_idx][1]}")
                        new_seeds.append(s + ranges[map_idx][0] - ranges[map_idx][1])
                        seed_idx += 1
                        break
                    else:
                        logging.debug(f"HERE3 {s}, {ranges[map_idx]}")
                        map_idx += 1
            
            if seed_idx < len(seeds):
                for i in range(seed_idx, len(seeds)):
                    new_seeds.append(seeds[i])
            
            seeds = sorted(new_seeds)
            logging.debug("")
            logging.debug(f"seeds {seeds}")
        
    print(min(seeds))


def main2(file_name):
    with open(file_name, "r") as f:
        seeds_str = f.readline()
        seeds = [int(s) for s in seeds_str.split(":")[1].split(" ") if s != ""]
        # List of [min, max] ranges (inclusive)
        seeds = [[seeds[i], seeds[i] + seeds[i + 1] - 1] for i in range(0, len(seeds), 2)]
        seeds = sorted(seeds)
        logging.debug(seeds)
        f.readline()  # first empty line

        for _ in range(7):
            ranges = []
            map_name = f.readline()  # name
            logging.debug(map_name[:-1])
            while input_str := f.readline():
                if input_str == "\n":
                    break
                
                # (dest, source, range)
                maps = tuple(int(s) for s in input_str.split(" "))
                ranges.append(maps)
            
            ranges = sorted(ranges, key=lambda a: a[1])
            logging.debug(ranges)

            new_seeds = []
            map_idx = 0
            seed_idx = 0
            while seed_idx < len(seeds) and map_idx < len(ranges):
                curr_s = seeds[seed_idx]
                while map_idx < len(ranges):
                    if curr_s[0] < ranges[map_idx][1] and curr_s[1] < ranges[map_idx][1]:
                        logging.debug(f"HERE1 {curr_s}, {ranges[map_idx]}, {curr_s}")
                        new_seeds.append(curr_s)
                        seed_idx += 1
                        break

                    elif curr_s[0] < ranges[map_idx][1]:
                        assert curr_s[1] >= ranges[map_idx][1]
                        logging.debug(f"HERE2 {curr_s}, {ranges[map_idx]}, {(curr_s[0], ranges[map_idx][1] - 1)}")
                        new_seeds.append([curr_s[0], ranges[map_idx][1] - 1])
                        curr_s = [ranges[map_idx][1], curr_s[1]]

                    elif curr_s[0] >= ranges[map_idx][1] and curr_s[1] < ranges[map_idx][1] + ranges[map_idx][2]:
                        diff = ranges[map_idx][0] - ranges[map_idx][1]
                        logging.debug(f"HERE3 {curr_s}, {ranges[map_idx]}, {(curr_s[0] + diff, curr_s[1] + diff)}")
                        new_seeds.append(sorted([curr_s[0] + diff, curr_s[1] + diff]))
                        seed_idx += 1
                        break

                    elif curr_s[0] >= ranges[map_idx][1] and curr_s[0] < ranges[map_idx][1] + ranges[map_idx][2]:
                        assert curr_s[1] >= ranges[map_idx][1] + ranges[map_idx][2]
                        diff = ranges[map_idx][0] - ranges[map_idx][1]
                        logging.debug(f"HERE4 {curr_s}, {ranges[map_idx]}, {(curr_s[0] + diff, ranges[map_idx][1] + ranges[map_idx][2] - 1 + diff)}")
                        new_seeds.append(sorted([curr_s[0] + diff, ranges[map_idx][1] + ranges[map_idx][2] - 1 + diff]))
                        curr_s = [ranges[map_idx][1] + ranges[map_idx][2], curr_s[1]]

                    else:
                        assert curr_s[0] >= ranges[map_idx][1] + ranges[map_idx][2]
                        assert curr_s[1] >= ranges[map_idx][1] + ranges[map_idx][2]
                        logging.debug(f"HERE5 {curr_s}, {ranges[map_idx]}")
                        map_idx += 1
            
            if seed_idx < len(seeds):
                logging.debug(f"HERE6 {curr_s}")
                new_seeds.append(curr_s)
                seed_idx += 1
                for i in range(seed_idx, len(seeds)):
                    logging.debug(f"HERE6 {seeds[i]}")
                    new_seeds.append(seeds[i])
            
            seeds = sorted(new_seeds)
            logging.debug("")
            logging.debug(f"seeds {seeds}")
        
    print(min(seeds)[0])
    

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