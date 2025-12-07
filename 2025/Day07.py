# import os
# import sys
# import copy
# from pprint import pprint
# from functools import cache
from aocd import get_data
from tqdm import tqdm
# from aocd import submit
import time


def main():
    # # # # # # # # # # # #
    # Day 7: Laboratories #
    # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............""".splitlines()
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=7, year=2025).splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    beams = set()
    tracer = []
    for r, row in enumerate(aoc_input):
        if r == 0:
            for c, col in enumerate(row):
                if col == 'S':
                    beams.add(c)
                    tracer.append({c: 1})
                    break
            continue
        tracer.append({})
        for c, col in enumerate(row):
            if col == '^' and c in beams:
                p1 += 1
                # test.append((r,c))
                beams.remove(c)
                beams.add(c + 1)
                beams.add(c - 1)
                if c + 1 not in tracer[-1].keys():
                    tracer[-1][c + 1] = tracer[-2][c]
                else:
                    tracer[-1][c + 1] += tracer[-2][c]
                if c - 1 not in tracer[-1].keys():
                    tracer[-1][c - 1] = tracer[-2][c]
                else:
                    tracer[-1][c - 1] += tracer[-2][c]
                tracer[-2][c] = 0
        if len(tracer) > 1:
            for c2, v in tracer[-2].items():
                if c2 in tracer[-1].keys():
                    tracer[-1][c2] += v
                else:
                    tracer[-1][c2] = v
    p2 = sum(tracer[-1].values())
    
    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

if __name__ == '__main__':
    main()
 