# import os
# import sys
import copy
# from pprint import pprint
# from functools import cache
from aocd import get_data
from tqdm import tqdm
# from aocd import submit
import time
import math
from pprint import pprint
import numpy as np
from scipy.spatial import ConvexHull
from shapely.geometry import Point, Polygon, MultiPoint

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'


def main():
    # # # # # # # # # # # # # # # # #
    # --- Day 9: Movie Theater ---  #
    # # # # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    aoc_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".splitlines()
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=9, year=2025).splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    ul_dist = math.inf
    ul_point = ()
    ur_dist = math.inf
    ur_point = ()
    ll_dist = math.inf
    ll_point = ()
    lr_dist = math.inf
    lr_point = ()
    points = []
    mx = 0
    my = 0

    
    for p in aoc_input:
        p = [int(x) for x in p.split(',')]
        points.append(tuple(p))
        if p[0] > mx:
            mx = p[0]
        if p[1] > my:
            my = p[1]
    
    points.append(points[0])
    path = []
    for indx, p in enumerate(points[:-1]):
        pt1 = p
        pt2  = points[indx + 1]
        step = 1
        if pt1[0] == pt2[0]:
            if pt1[1] > pt2[1]:
                step = -1
            for y in range(pt1[1], pt2[1], step):
                path.append((pt1[0], y))
        else:
            if pt1[0] > pt2[0]:
                step = -1
            for x in range(pt1[0], pt2[0], step):
                path.append((x, pt1[1]))
    
    path.append(points.pop())

    for p in points:
        ul = math.dist((0,0), p)
        ur = math.dist((mx, 0), p)
        ll = math.dist((0, my), p)
        lr = math.dist((mx, my), p)
        if ul < ul_dist:
            ul_dist = ul
            ul_point = p
        if ur < ur_dist:
            ur_dist = ur
            ur_point = p
        if ll < ll_dist:
            ll_dist = ll
            ll_point = p
        if lr < lr_dist:
            lr_dist = lr
            lr_point = p
    
    p1 = calc_area(lr_point, ul_point)
    if calc_area(ll_point, lr_point) > p1:
        p1 = calc_area(ll_point, lr_point)
    
    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def calc_area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

if __name__ == '__main__':
    main()
 