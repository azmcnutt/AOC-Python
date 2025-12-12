# import os
# import sys
import copy
# from pprint import pprint
from functools import lru_cache
from collections import deque
from aocd import get_data
from tqdm import tqdm
# from aocd import submit
import time
from pprint import pprint
from functools import cache



def main():
    # # # # # # # # # # # # # #
    # --- Day 11: Reactor --- #
    # # # # # # # # # # # # # #

    # load sample data, copied and pasted from the site into list.
    # Each list item is one line of input
    # p1 Sample data
    aoc_input = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out""".splitlines()
    
    # p2 Sample data
    aoc_input= """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""
    
    # once the test data provides the right answer:
    # replace test data with data from the puzzle input
    aoc_input = get_data(day=11, year=2025).splitlines()
    
    # Get the time to see how fast the solution runs.
    # I get the time after the input has been downloaded to test
    # the speed of my program, not the speed of my Internet connection.
    start_time = time.time()

    p1 = 0
    p2 = 0

    path = {}
    for l in aoc_input:
        k, p = l.split(': ')
        p = p.split()
        path[k] = p
    
    p1 = walk_path('you', 'out', path, set(), {})
    p2p1s1 = walk_path('svr', 'fft', path, set(), {})
    p2p1s2 = walk_path('fft', 'dac', path, set(), {})
    p2p1s3 = walk_path('dac', 'out', path, set(), {})
    p2p2s1 = walk_path('svr', 'dac', path, set(), {})
    p2p2s2 = walk_path('dac', 'fft', path, set(), {})
    p2p2s3 = walk_path('fft', 'out', path, set(), {})
    p2 = (p2p1s1 * p2p1s2 * p2p1s3) + (p2p2s1 * p2p2s2 * p2p2s3)

    
    print(f'P1: {p1}, P2: {p2} in {time.time() - start_time} seconds.')

# Some help
# https://topaz.github.io/paste/#XQAAAQBqAwAAAAAAAAAkk4ZG/3FmkOEiq1dFAAFDFSTdMr6/b8mE3YPdTt/5lzxZMpUhTYTHPIx1KQTzz0gFw4jNvbk0+5bXHczfghuyhpIZUvzY4pz3Yac9kVWiyUBRbskxIPTVsRHjiB97Das8YLJ1qA1D+mVVuae2UQUsIDO5g6pNKObWCYPA9B8OHfzx6Uj6blqUSB/EG8QLP5zwd7gNE7qjRmkpQvCDGc18T4Fw1x4jQYAub3LYbnaVIP6oCdtaPmow9pjyUOW35pSoVDrgQNT3ht5T6wTO9C+2fWtklIXxjw2ubk2Tw6U9gj5SQXHiQ1MSRMVUkrBRERhGxM9/diQ/CB+/WYu/Yqa6spoO8Nn/u0zgyX52j5GWpvEtewntMUx4Frh4tEuSWJufSqWMgdl23Dx7H1BGz5JICvSMQ0pVgo2ki0TfjLvbG0bHn+XZ2au8ZsGXD/GYl+EzKj2w+D7l0zMpetOuZQypaMX09KKEF78MoBboGYuIlQOJgoWkfItuvKr//YHWcg==
def walk_path(loc, end, path, visited, totals):
    if loc == end:
        return 1
    if loc == 'out' or loc in visited:
        return 0
    if loc in totals:
        return totals[loc]
    count = 0
    visited.add(loc)
    for l in path[loc]:
        count += walk_path(l, end, path, visited, totals)
    totals[loc] = count
    visited.remove(loc)
    return count

if __name__ == '__main__':
    main()
 