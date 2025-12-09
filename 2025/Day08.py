# import os
# import sys
# import copy
# from pprint import pprint
# from functools import cache
from aocd import get_data
from tqdm import tqdm
# from aocd import submit
import time
import math
from pprint import pprint


def main():
    # # # # # # # # # # # # # # #
    # --- Day 8: Playground --- #
    # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""".splitlines()
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=8, year=2025).splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 1
    p2 = 0

    points = {}
    distances = []
    # x, y, z = [int(x) for x in aoc_input[0].split(',')]
    # p1 = [x, y, z]
    # for a in aoc_input[1:]:
    #     x, y, z = [int(x) for x in a.split(',')]
    #     print(f'{a}: {calc_distance(p1, [x, y, z])}')

    for indx in range(len(aoc_input) - 1):
        x, y, z = [int(x) for x in aoc_input[indx].split(',')]
        point1 = (x, y, z)
        for a in aoc_input[indx + 1:]:
            x, y, z = [int(x) for x in a.split(',')]
            point2 = (x, y, z)
            # dist = calc_distance(point1, point2)
            dist = math.dist(point1, point2)
            points[dist] = (point1, point2)
            distances.append(dist)
    distances.sort()
    closest_points = []
    junctions = []
    wired = []
    count = 0
    for d in distances:
        closest_points.append(points[d])
    for c in closest_points:
        point1, point2 = c
        if point1 not in wired and point2 not in wired:
            # New Circuit
            junctions.append([point1, point2])
            wired.append(point1)
            wired.append(point2)
            count += 1
        elif point1 in wired and point2 not in wired:
            # Find the p1 junction and add p2
            for indx, p in enumerate(junctions):
                if point1 in p:
                    junctions[indx].append(point2)
                    wired.append(point2)
                    count += 1
                    p2 = c
                    break
        elif point1 not in wired and point2 in wired:
            # Find the p2 junction and add p1
            for indx, p in enumerate(junctions):
                if point2 in p:
                    junctions[indx].append(point1)
                    wired.append(point1)
                    count += 1
                    p2 = c
                    break
        elif point1 in wired and point2 in wired:
            p1_indx = -2
            p2_indx = -2
            for indx, p in enumerate(junctions):
                if point1 in p and point2 in p:
                    # Do Nothing
                    p1_indx = -1
                    p2_indx = -1
                    count += 1
                    break
                elif point1 in p:
                    p1_indx = indx
                elif point2 in p:
                    p2_indx = indx
                    p2_data = p
            if p1_indx  == -1 and p2_indx == -1:
                pass
            elif p1_indx == -2 or p2_indx == -2:
                print('Should not get here')
            else:
                for z in p2_data:
                    junctions[p1_indx].append(z)
                del junctions[p2_indx]
                count += 1
        else:
            # we should not get here either
            print('I dont know what happened.')
        if count == 1000:
            junction_lens = []
            for j in junctions:
                junction_lens.append(len(j))
            junction_lens.sort(reverse=True)
            for indx in range(3):
                p1 *= junction_lens[indx]
    
    p2 = p2[0][0] * p2[1][0]
    
    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')



if __name__ == '__main__':
    main()
 