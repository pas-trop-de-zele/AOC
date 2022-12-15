import sys
from math import *
from pprint import pprint as pprint
from sympy.ntheory.modular import crt
import heapq
from copy import *
from collections import *
import functools
from itertools import *

# sys.setrecursionlimit(100000000)

from math import sqrt, ceil


MOVES_ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]
fin = sys.stdin.read().strip().split("\n")

"""
After the first point of each path
each point indicates the end of a straight horizontal or vertical line to be drawn from the PREVIOUS POINT.

The sand is pouring into the cave from point 500,0.
Drawing rock as #, air as ., and the source of the sand as +, 

move down => down left -> down right -> rest
down as in all the way down on top of the first # or sand

get the max Y depth, so if falls over that, terminate
"""


startx, starty = inf, 0
endx, endy = -inf, -inf
rocks = set()
sands = set()
def display():
    for y in range(starty, endy + 1):
        for x in range(startx - 20, endx + 1 + 20):
            if (x, y) in rocks:
                print('#', end='')
            elif (x, y) in sands:
                print('o', end='')
            else:
                print('.', end='')
        print()
for l in fin:
    l = l.split(" -> ")
    prev = None
    for coor in l:
        x, y = map(int, coor.split(","))
        startx = min(startx, x)
        starty = min(starty, y)
        endx = max(endx, x)
        endy = max(endy, y)

        new_prev = (x, y)
        if prev is None:
            prev = (x, y)
        else:
            prevx, prevy = prev
            if prevx != x:
                if prevx > x:
                    x, prevx = prevx, x
                for c in range(prevx, x + 1):
                    rocks.add((c, y))
            elif prevy != y:
                if prevy > y:
                    y, prevy = prevy, y
                for r in range(prevy, y + 1):
                    rocks.add((x, r))
        prev = new_prev

display()
endy += 2
for x in range(startx - 1000, endx + 1000):
    rocks.add((x, endy))
while True:
    x, y = 500, -10
    reach_bottom = False
    while True:
        # print(x, y)
        # Check that next fall not touching rock or sand
        while (x, y + 1) not in rocks and (x, y + 1) not in sands:
            y += 1
            # print(x, y)
        
        
        if ((x - 1, y + 1) in rocks or (x - 1, y + 1) in sands) and \
           ((x + 1, y + 1) in rocks or (x + 1, y + 1) in sands):
           break

        if (x - 1, y + 1) not in rocks and (x - 1, y + 1) not in sands:
            x -= 1
            # print("LEFT ", x, y)
        elif (x + 1, y + 1) not in rocks and (x + 1, y + 1) not in sands:
            x += 1
            # print("RIGHT ", x, y)
    
    sands.add((x, y))
    if (x, y) == (500, 0):
        break
    # display()
    
# display()

print(len(sands))
        

