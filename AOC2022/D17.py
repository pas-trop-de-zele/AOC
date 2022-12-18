import sys
from math import *
from pprint import pprint as pprint
from sympy.ntheory.modular import crt
import heapq
from copy import *
from collections import *
import functools
from itertools import *
from math import sqrt, ceil
import threading
import cmath  
import itertools
# sys.setrecursionlimit(100000000)

fin = sys.stdin.read().strip()
sign = itertools.cycle(fin)
cur = 0

ROCKS = set()
# Establish bottom bed rock
for x in range(7):
    ROCKS.add((x, -1))

def spawn(i):
    y = MAX_HEIGHT + 4
    if i == 0:
        return [(2, y), (3, y), (4, y), (5, y)]
    elif i == 1:
        return [(3, y+2), (2, y+1), (3, y+1), (4, y+1), (3, y)]
    elif i == 2:
        return [(4, y+2), (4, y+1), (2, y), (3, y), (4, y)]
    elif i == 3:
        return [(2, y+3), (2, y+2), (2, y+1), (2, y)]
    elif i == 4:
        return [(2, y+1), (3, y+1), (2, y), (3, y)]

def test_shapes():
    for i in range(5):
        shape = spawn(i)
        for y in range(6, -1, -1):
            for x in range(0, 7):
                if (x, y) in shape:
                    print('#', end='')
                else:
                    print('.', end='')
            print()
        print('-' * 20)

def display(shape):
    for y in range(MAX_HEIGHT + 5, -2, -1):
        print(str(y if y >= 0 else ' ').ljust(2), end=' ')
        for x in range(WIDTH):
            if (y == -1):
                print('-', end='')
            elif (x, y) in ROCKS:
                print('#', end='')
            elif (x, y) in shape:
                print('@', end='')
            else:
                print('.', end='')
        print()
    print('0' * 10)

def fall(shape):
    new_shape = set()
    is_interfered = False
    for x, y in shape:
        y -= 1
        new_shape.add((x, y))
        if (x, y) in ROCKS:
            is_interfered = True
            break
    return (False, new_shape) if not is_interfered else (True, shape)

def move(shape, direction):
    new_shape = set()
    is_interfered = False
    for x, y in shape:
        if direction == '>':
            x += 1
        elif direction == '<':
            x -= 1
        new_shape.add((x, y))
        if (x, y) in ROCKS or not 0 <= x < WIDTH:
            is_interfered = True
            break
    return new_shape if not is_interfered else shape

def issamedistance(height_map):
    distances = set()
    score_gap = set()
    for i in range(1, len(height_map)):
        distances.add(height_map[i][0] - height_map[i - 1][0])
        score_gap.add(height_map[i][1] - height_map[i-1][1])
        if len(distances) > 1 or len(score_gap) > 1:
            return False
    return True

def get_height_map():
    heights = [0] * WIDTH
    for x, y in ROCKS:
        heights[x] = max(heights[x], y)
    for i in range(WIDTH - 1):
        trajectory = EQUAL
        if heights[i] < heights[i+1]:
            trajectory = UP
        elif heights[i] > heights[i+1]:
            trajectory = DOWN
        heights[i] = (trajectory, abs(heights[i] - heights[i+1]))
    return tuple(heights[:-1])

MAX_HEIGHT = -1
WIDTH = 7
UP = 1
EQUAL = 0
DOWN = -1
cache = defaultdict(list)
cycle_height = {}
ret = 0
for i in range(2022):
    shape = spawn(cur)
    # cycle_height[i] = MAX_HEIGHT + 1

    # height_map = get_height_map()
    # cache[(height_map)].append((i, MAX_HEIGHT + 1))
    # if len(cache[height_map]) > 5 and issamedistance(cache[height_map]):
    #     print("CYCLE DETECTED")
    #     print(cache[height_map])
    #     common_difference = cache[height_map][1][0] - cache[height_map][0][0]
    #     common_gain = cache[height_map][1][1] - cache[height_map][0][1]
        
    #     start = cache[height_map][0][0]
    #     cycle_count = (1000000000000 - start) // common_difference  
    #     ret = cycle_count  * common_gain
        
    #     before_start_gain = cache[height_map][0][1]
    #     ret += before_start_gain

    #     leftover_cycle = (1000000000000 - start) % common_difference
    #     ret += cycle_height[start + leftover_cycle] - before_start_gain
    #     break

    cur = (cur + 1) % 5
    # print("SPAWN", sorted(shape))
    while True:
        shape = move(shape, next(sign))
        is_stopped, shape = fall(shape)
        if is_stopped:
            break
    ROCKS.update(shape)
    MAX_HEIGHT = max(MAX_HEIGHT, max(p[1] for p in shape))
# print(ret)
print(MAX_HEIGHT + 1)