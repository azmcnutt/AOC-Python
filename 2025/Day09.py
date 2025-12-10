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
7,3
9,3
7,1""".splitlines()
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    # aoc_input = get_data(day=9, year=2025).splitlines()
    # too high 4598136816
    #          4672413798
    
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
    
    # for p in points:
    #     ul = math.dist((0,0), p)
    #     ur = math.dist((mx, 0), p)
    #     ll = math.dist((0, my), p)
    #     lr = math.dist((mx, my), p)
    #     if ul < ul_dist:
    #         ul_dist = ul
    #         ul_point = p
    #     if ur < ur_dist:
    #         ur_dist = ur
    #         ur_point = p
    #     if ll < ll_dist:
    #         ll_dist = ll
    #         ll_point = p
    #     if lr < lr_dist:
    #         lr_dist = lr
    #         lr_point = p
    
    # p1 = calc_area(lr_point, ul_point)
    # if calc_area(ll_point, lr_point) > p1:
    #     p1 = calc_area(ll_point, lr_point)

    # hull = ConvexHull(points)
    # hull = [(int(x[0]), int(x[1])) for x in hull.points]
    # hull = Polygon(hull)

    #9,5
    # print(points)
    mp = MultiPoint(points)
    test = mp.convex_hull
    hull = Polygon(points)
    print(hull.exterior.coords[:])

    for indx, point1 in enumerate(points):
        for point2 in points:
            x = calc_area(point1, point2)
            if x > p1:
                p1 = x
            if x > p2:
                if (hull.intersects(Point(point1)) 
                    and hull.intersects(Point(point2))
                    and hull.intersects(Point((point1[0], point2[1])))
                    and hull.intersects(Point((point2[0], point1[1])))):
                    p2 = x

    test_points = [
        [False, (0, 0)],
        [False, (7, 0)],
        [True, (7, 1)],
        [True, (7, 2)],
        [True, (7, 3)],
        [True, (7, 4)],
        [False, (1, 3)],
        [True, Point(2, 3)],
        [True, Point(3, 3)],
        [False, Point(1, 4)],
        [True, Point(2, 4)],
        [True, Point(3, 4)],
        [True, Point(3, 5)],
        [True, Point(2, 5)],
        [False, Point(3, 6)],
        [True, Point(8, 5)],
        [True, Point(9, 5)],
        [True, Point(10, 5)],
        [True, Point(8, 4)],
        [True, Point(8, 5)],
        [False, Point(4, 6)],
        [False, Point(5, 6)],
        [False, Point(6, 6)],
        [False, Point(7, 6)],
        [False, Point(8, 6)],
        [False, Point(8, 7)],
        [False, Point(11, 0)],
        [True, Point(11, 1)],
        [True, Point(11, 2)],
        [True, Point(10, 2)],
        [False, Point(12, 0)],
        [False, Point(12, 1)],
        [False, Point(12, 2)],
        [False, Point(12, 7)],
        [False, Point(12, 8)],
    ]
    for x in test_points:
        ret = hull.intersects(x[1])
        if (bool(ret) != bool(x[0])):
            print(RED, end='')
        print(f'{x[0]} : {ret} - {x[1]}')
        print(RESET, end='')
    
    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

def calc_area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def is_point_in_polygon(point, polygon):
    """
    Determines if a point is inside an irregular polygon using the ray casting algorithm.

    Args:
        point (tuple): A tuple (x, y) representing the coordinates of the point.
        polygon (list): A list of tuples, where each tuple (x, y) represents a vertex
                        of the polygon in sequential order.

    Returns:
        bool: True if the point is inside the polygon, False otherwise.
    """
    x, y = point
    num_vertices = len(polygon)
    inside = False

    # Start with the last vertex as the first point of the current edge
    p1x, p1y = polygon[num_vertices - 1]

    for i in range(num_vertices):
        p2x, p2y = polygon[i]

        # Check if the ray from the point intersects the current edge
        if point in polygon:
            return True
        if ((p1y <= y and p2y > y) or (p1y > y and p2y <= y)) and \
           (x < (p2x - p1x) * (y - p1y) / (p2y - p1y) + p1x):
            inside = not inside

        p1x, p1y = p2x, p2y

    return inside

def is_point_in_hull(point, hull, tolerance=1e-12):
    """
    Checks if a point is within or on the boundary of a convex hull.

    Args:
        point (np.ndarray): The point to check, as a 1D NumPy array.
        hull (scipy.spatial.ConvexHull): The ConvexHull object.
        tolerance (float): A small tolerance for numerical comparisons.

    Returns:
        bool: True if the point is inside or on the hull, False otherwise.
    """
    # For each equation (facet), check if the point lies on the "inside" side.
    # The equation is of the form: normal_vector . point + offset <= 0
    # where normal_vector is hull.equations[:, :-1] and offset is hull.equations[:, -1]
    return np.all(np.dot(hull.equations[:, :-1], point) + hull.equations[:, -1] <= tolerance)

if __name__ == '__main__':
    main()
 