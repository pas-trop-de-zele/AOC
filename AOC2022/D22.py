import sys
from math import *
from pprint import pprint as pprint
import time
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
sys.setrecursionlimit(100000)
grid, notes = sys.stdin.read().strip().split("\n\n")
grid = grid.split('\n')[1:]
for l in grid:
    print(l)
walls = set()
max_row = defaultdict(lambda : [None, -1])
max_col = defaultdict(lambda : [None, None])
for row, l in enumerate(grid):
    left, right = None, len(l) - 1
    for col, char in enumerate(l):
        max_row[col][0] = row if max_row[col][0] is None and not char.isspace() else max_row[col][0]
        max_row[col][1] = max(max_row[col][1], row) if not char.isspace() else max_row[col][1]

        if left is None and not char.isspace():
            left = col

        if char == '#':
            walls.add((row, col))
    max_col[row] = [left, right]
pprint(max_row)
pprint(max_col)
MOVES_ADJACENT = [[0, 1], [1, 0], [0, -1], [-1, 0]]
cur_direction = 0 # R
direction_repr = 'RDLU'
is_inside = False
def move(r, c, count):
    global cur_direction, is_inside
    dy, dx = MOVES_ADJACENT[cur_direction]
    for _ in range(count):
        rr = r + dy
        cc = c + dx

        if rr > max_row[c][1]:
            print("DOWN EXCEED")
            rr = max_row[c][0]
        elif rr < max_row[c][0]:
            print("UP EXCEED", rr, max_row[c])
            rr = max_row[c][1]

        # print('+', rr, cc)
        if cc > max_col[r][1]:
            print("RIGHT EXCEED")
            cc = max_col[r][0]
        elif cc < max_col[r][0]:
            print("LEFT EXCEED")
            cc = max_col[r][1]

        if (rr, cc) in walls:
            print("WALLS", rr, cc)
            return r, c
        r, c = rr, cc
        print('AT',rr, cc)
    return r, c

def solve():
    r, c, count = 0, max_col[0][0], 0
    global cur_direction
    for char in notes:
        print(char)
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            # Process count
            print(r, c, count, direction_repr[cur_direction])
            r, c = move(r, c, count)
            count = 0
            if char == 'R':
                cur_direction = (cur_direction + 1) % 4
            elif char == 'L':
                cur_direction = (cur_direction + 3) % 4

    # Need to take care of the last direction        
    if count:
        r, c = move(r, c, count)
    return r, c, cur_direction

r, c, d = solve()
print(r, c, d)
print(((r + 1) * 1000) + ((c + 1) * 4) + d)
print(((c + 1) * 4))
print(d)


# PART2
import sys
from math import *
from pprint import pprint as pprint
import time
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
sys.setrecursionlimit(100000)
grid, notes = sys.stdin.read().strip().split("\n\n")
grid = grid.split('\n')[1:]
walls = set()
SIZE = 50

class Side:
    def __init__(self, id, left, right, up, down):
        self.id = id
        self.left=left
        self.right = right
        self.up = up
        self.down = down
        self.up_side = None
        self.right_side = None
        self.down_side = None
        self.left_side = None
    
    def __str__(self):
        return f"{self.left} <-> {self.right} | {self.up} ^v {self.down}"

    def __eq__(self, other) -> bool:
        return self.id == other.id

sides = {}
def setup():
    for row, l in enumerate(grid):
        for col, char in enumerate(l):
            if char == '#':
                walls.add((row, col))

    sides[1] = Side(1, 50, 50 + SIZE - 1, 0, 0 + SIZE - 1)
    sides[2] = Side(2, 100, 100 + SIZE - 1, 0, 0 + SIZE - 1)
    sides[3] = Side(3, 50, 50 + SIZE - 1, 50, 50 + SIZE - 1)
    sides[4] = Side(4, 50, 50 + SIZE - 1, 100, 100 + SIZE - 1)
    sides[5] = Side(5, 0, SIZE - 1, 100, 100 + SIZE - 1)
    sides[6] = Side(6, 0, SIZE - 1, 150, 150 + SIZE - 1)

    # sides[1] = Side(1, 3, 3 + SIZE - 1, 0, 0 + SIZE - 1)
    # sides[2] = Side(2, 6, 6 + SIZE - 1, 0, 0 + SIZE - 1)
    # sides[3] = Side(3, 3, 3 + SIZE - 1, 3, 3 + SIZE - 1)
    # sides[4] = Side(4, 3, 3 + SIZE - 1, 6, 6 + SIZE - 1)
    # sides[5] = Side(5, 0, SIZE - 1, 6, 6 + SIZE - 1)
    # sides[6] = Side(6, 0, SIZE - 1, 9, 9 + SIZE - 1)

    #   3
    # 2   0
    #   1
    #

    # map to (next side index, direction)
    sides[1].up_side = 6, 0
    sides[1].right_side = 2, 0
    sides[1].down_side = 3, 1
    sides[1].left_side = 5, 0

    sides[2].up_side = 6, 3
    sides[2].right_side = 4, 2
    sides[2].down_side = 3, 2
    sides[2].left_side = 1, 2

    sides[3].up_side = 1, 3
    sides[3].right_side = 2, 3
    sides[3].down_side = 4, 1
    sides[3].left_side = 5, 1

    sides[4].up_side = 3, 3
    sides[4].right_side = 2, 2
    sides[4].down_side = 6, 2
    sides[4].left_side = 5, 2

    sides[5].up_side = 3, 0
    sides[5].right_side = 4, 0
    sides[5].down_side = 6, 1
    sides[5].left_side = 1, 0

    sides[6].up_side = 5, 3
    sides[6].right_side = 4, 3
    sides[6].down_side = 2, 1
    sides[6].left_side = 1, 1

setup()
for side in sides.values():
    print(side)
MOVES_ADJACENT = [[0, 1], [1, 0], [0, -1], [-1, 0]]
cur_direction = 0 # R
direction_repr = 'RDLU'
index = 1

#   3
# 2   0
#   1
RIGHT, DOWN, LEFT, UP = 0,1,2,3
# the side will always be opposite the 
def transform(r, c, cur_direction, new_direction, old_side, new_side):
    if old_side == new_side:
        return r, c

    # face direction_relative position
    left_left_facing = (cur_direction == LEFT and new_direction == RIGHT)
    left_top_facing = (cur_direction == UP and new_direction == RIGHT)
    right_right_facing = (cur_direction == RIGHT and new_direction == LEFT)
    right_bottom_facing = (cur_direction == DOWN and new_direction == LEFT)
    top_left_facing = (cur_direction == LEFT and new_direction == DOWN)
    bottom_right_facing = (cur_direction == RIGHT and new_direction == UP)
    
    # same direction case
    straight_bottom = (cur_direction == DOWN and new_direction == DOWN)
    straight_top = (cur_direction == UP and new_direction == UP)
    straight_right = (cur_direction == RIGHT and new_direction == RIGHT)
    straight_left = (cur_direction == LEFT and new_direction == LEFT)
    if straight_bottom:
        print("straight_bottom")
        new_r = new_side.up
        new_c = new_side.left + abs(c - old_side.left)
    elif straight_top:
        print("straight_top")
        new_r = new_side.down
        new_c = new_side.left + abs(c - old_side.left)
    elif straight_right:
        print("straight_right")
        new_r = new_side.up + abs(r - old_side.up)
        new_c = new_side.left
    elif straight_left:
        print("straight_left")
        new_r = new_side.up + abs(r - old_side.up)
        new_c = new_side.right
    elif left_left_facing:
        print("left_left_facing")
        print(new_side.down, abs(r - old_side.up))
        new_r = new_side.down - abs(r - old_side.up)
        print(new_r)
        new_c = new_side.left
    elif left_top_facing:
        print("left_top_facing")
        new_r = new_side.up + abs(c - old_side.left)
        new_c = new_side.left
    elif right_right_facing:
        print("right_right_facing")
        new_r = new_side.down - abs(r - old_side.up)
        new_c = new_side.right
    elif right_bottom_facing:
        print("left_top_facing")
        new_r = new_side.up + abs(c - old_side.left)
        new_c = new_side.right
    elif top_left_facing:
        print("top_left_facing")
        new_r = new_side.up
        new_c = new_side.left + abs(r - old_side.up)
    elif bottom_right_facing:
        print("bottom_right_facing")
        new_r = new_side.down
        new_c = new_side.left + abs(r - old_side.up)
    return new_r, new_c

# Cur direction will shift in here
def move(r, c, count):
    global cur_direction, index
    print(sides[index])
    for _ in range(count):
        old_index = index
        old_side = sides[old_index]
        dy, dx = MOVES_ADJACENT[cur_direction]
        rr = r + dy
        cc = c + dx

        new_direction = cur_direction
        if cc < old_side.left:
            print("EXCEED LEFT", cc, old_side.left)
            index, new_direction = old_side.left_side
        elif cc > old_side.right:
            print("EXCEED right", cc, old_side.right)
            index, new_direction = old_side.right_side
        elif rr < old_side.up:
            print("EXCEED UP", rr, old_side.up)
            index, new_direction = old_side.up_side
        elif rr > old_side.down:
            print("EXCEED DOWN", rr, old_side.down)
            index, new_direction = old_side.down_side
        
        new_side = sides[index]
        if old_side != new_side:
            print(f"Switched to side {index}")
            rr, cc = transform(r, c, cur_direction, new_direction, old_side, new_side)
            print("AT SIDE", index, "row=", rr, "col=", cc)
        if (rr, cc) in walls:
            # Revert to the previous place
            index = old_index
            print("WALLS")
            return r, c
        
        cur_direction = new_direction
        r, c = rr, cc
    return r, c

def solve():
    r, c, count = 0, SIZE, 0
    global cur_direction
    
    for char in notes:
        print(char)
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            # Process count
            # print(r, c, index, count, direction_repr[cur_direction])
            r, c = move(r, c, count)
            print("AT SIDE", index, "row=", r, "col=", c)
            count = 0
            if char == 'R':
                cur_direction = (cur_direction + 1) % 4
            elif char == 'L':
                cur_direction = (cur_direction + 3) % 4
            print("CURRENT DIR", direction_repr[cur_direction])

    # Need to take care of the last direction        
    if count:
        r, c = move(r, c, count)
        print("AT SIDE", index, "row=", r, "col=", c, direction_repr[cur_direction])
    return r, c, cur_direction


r, c, d = solve()
print((r), (c), d)
# print((r+1), (c+1), d)
print(((r + 1) * 1000) + ((c + 1) * 4) + d)
