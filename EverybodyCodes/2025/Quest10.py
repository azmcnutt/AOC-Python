# import os
# import sys
# import copy
# from pprint import pprint
# from functools import cache
from tqdm import tqdm
from ecd import get_inputs
import math
import time
from pprint import pprint
from copy import deepcopy
import re
import functools


GENERATED_NAMES = set()

def main():
    # # # # # # # # # # # # # # # # # # # # #
    # --- Quest 10: Feast on the Board ---  #
    # # # # # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    ecd_input = {
        '1': """...SSS.......
.S......S.SS.
..S....S...S.
..........SS.
..SSSS...S...
.....SS..S..S
SS....D.S....
S.S..S..S....
....S.......S
.SSS..SS.....
.........S...
.......S....S
SS.....S..S..""",
        '2': """...SSS##.....
.S#.##..S#SS.
..S.##.S#..S.
.#..#S##..SS.
..SSSS.#.S.#.
.##..SS.#S.#S
SS##.#D.S.#..
S.S..S..S###.
.##.S#.#....S
.SSS.#SS..##.
..#.##...S##.
.#...#.S#...S
SS...#.S.#S..""",
        '3': """...SSS.......
.S......S.SS.
..S....S...S.
..........SS.
..SSSS...S...
.....SS..S..S
SS....D.S....
S.S..S..S....
....S.......S
.SSS..SS.....
.........S...
.......S....S
SS.....S..S..""",
    }
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    ecd_input = get_inputs(quest=10, event=2025)# ["1"].splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    num_moves = 20

    p1 = 0
    p2 = 0
    p3 = 0

    # Part one
    # ecd_data = ecd_input['1'].splitlines()
    # brd_max_x_y = (len(ecd_data[0]), len(ecd_data))
    # start = False
    # for indx_y, y in enumerate(ecd_data):
    #     for indx_x, x in enumerate(y):
    #         if x == "D":
    #             start = (indx_x, indx_y)
    #             break
    #     if start:
    #         break

    # possible_moves = calc_moves_p1(start, brd_max_x_y, num_moves, set())

    # for m in possible_moves:
    #     if ecd_data[m[1]][m[0]] == "S":
    #         p1 += 1
    
    # Part two
    ecd_data = ecd_input['2'].splitlines()
    brd_max_x_y = (len(ecd_data[0]), len(ecd_data))
    dragons = False
    safe_zone = []
    sheep = []
    for indx_y, y in enumerate(ecd_data):
        for indx_x, x in enumerate(y):
            if x == "D":
                dragons = [(indx_x, indx_y)]
                continue
            elif x == "#":
                safe_zone.append((indx_x, indx_y))
                continue
            elif x == "S":
                sheep.append((indx_x, indx_y))

    p2 = calc_moves_p2(dragons, sheep, safe_zone, brd_max_x_y, num_moves)

    
    print(f'P1: {p1}, P2: {p2}, P3: {p3} in {time.time() - start_time} seconds.')

def calc_moves_p1(start, max_x_y, num_moves, cords):
    if not cords:
        cords = set()
    max_x = max_x_y[0]
    max_y = max_x_y[1]
    cur_x = start[0]
    cur_y = start[1]
    num_moves -= 1
    dirs = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (2, -1),
        (2, 1),
        (1, -2),
        (1, 2),
    ]

    for d in dirs:
        dir_x = d[0]
        dir_y = d[1]
        new_x = cur_x + dir_x
        new_y = cur_y + dir_y
        if 0 <= new_x <= max_x and 0 <= new_y <= max_y:
            cords.add((new_x, new_y))
            if num_moves:
                cords = calc_moves_p1((new_x, new_y), max_x_y, num_moves, cords)

    return cords

def calc_moves_p2(dragons, sheep, safe_zone, max_x_y, num_moves):
    sheep_eaten = 0
    max_x = max_x_y[0]
    max_y = max_x_y[1]
    # cur_x = start[0]
    # cur_y = start[1]
    new_dragons = []
    new_sheep = []
    num_moves -= 1
    dirs = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (2, -1),
        (2, 1),
        (1, -2),
        (1, 2),
    ]

    for dragon in dragons:
        for d in dirs:
            new_x = dragon[0] + d[0]
            new_y = dragon[1] + d[1]
            if 0 <= new_x <= max_x and 0 <= new_y <= max_y and (new_x, new_y) not in new_dragons:
                new_dragons.append((new_x, new_y))
    
    eaten, sheep = check_sheep(new_dragons, sheep, safe_zone)
    sheep_eaten += eaten
    
    for indx, s in enumerate(sheep):
        s = (s[0], s[1] + 1)
        if s[1] >= max_y:
            del sheep[indx]
        else:
            sheep[indx] = (s[0], s[1])
    
    eaten, sheep = check_sheep(new_dragons, sheep, safe_zone)
    sheep_eaten += eaten

    if num_moves > 0:
        sheep_eaten += calc_moves_p2(new_dragons, sheep, safe_zone, max_x_y, num_moves)

    return sheep_eaten

def check_sheep(dragons, sheep, safe_zone):
    eaten = 0
    for d in dragons:
        if d in safe_zone:
            continue
        if d in sheep:
            eaten += 1
            sheep.remove(d)
    return [eaten, sheep]



if __name__ == '__main__':
    main()
 