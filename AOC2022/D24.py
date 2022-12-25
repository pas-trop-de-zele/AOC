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
import time

fin = sys.stdin.read().strip().split("\n")
m = [l for l in fin]
H = len(m)
W = len(m[0])
CUR = [0,1]
END = (H-1, W-2)
flakes = []
for r in range(1, H - 1):
    for c in range(1, W - 1):
        if m[r][c] in ('<>^v'):
            flakes.append((m[r][c], r,c))

ORIGINAL_FLAKES_COUNT = len(flakes)
def get_next_location(sign, r, c):
    if sign == '<':
        c -= 1
    elif sign == '>':
        c += 1
    elif sign == '^':
        r -= 1
    elif sign == 'v':
        r += 1

    if r == H - 1:
        r = 1
    elif r == 0:
        r = H - 2
    
    if c == W - 1:
        c = 1
    elif c == 0:
        c = W - 2
    return r, c


MOVES_ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
queue = deque([(0, CUR[0], CUR[1])])
seen = set()
seen.add((0, CUR[0], CUR[1]))
def solve():
    global flakes, m, CUR, END
    for round in range(1, 100000000000000):
        # print(round)
        new_flakes = []

        for flake, r, c in flakes:
            rr, cc = get_next_location(flake, r, c)
            new_flakes.append((flake, rr, cc))
        
        assert(len(new_flakes) == ORIGINAL_FLAKES_COUNT)
        flakes = new_flakes

        flakes_set = set([(r,c) for _, r, c in flakes])
        
        q_len = len(queue)
        assert(q_len > 0)
        for _ in range(q_len):
            dist, r, c = queue.popleft()

            for dy, dx in MOVES_ADJACENT:
                rr = r + dy
                cc = c + dx
                if (rr, cc) == END:
                    print(dist + 1, rr, cc)
                    return

                if not 0 < rr < H - 1 or not 0 < cc < W - 1 or (rr, cc) in flakes_set or (dist + 1, rr, cc) in seen:
                    continue
                
                queue.append((dist + 1, rr, cc))
                seen.add((dist + 1, rr, cc))

            if (r, c) not in flakes_set and (dist + 1, r, c) not in seen:
                queue.append((dist + 1, r, c))
                seen.add((dist + 1, r, c))
solve()

CUR = (0,1)
END = (H-1, W-2)
queue = deque([(0, END[0], END[1])])
seen = set()
seen.add((0, END[0], END[1]))

def solve1():
    global flakes, m, CUR, END
    for round in range(1, 100000000000000):
        # print(round)
        new_flakes = []

        for flake, r, c in flakes:
            rr, cc = get_next_location(flake, r, c)
            new_flakes.append((flake, rr, cc))
        
        assert(len(new_flakes) == ORIGINAL_FLAKES_COUNT)
        flakes = new_flakes

        flakes_set = set([(r,c) for _, r, c in flakes])
        
        q_len = len(queue)
        assert(q_len > 0)
        for _ in range(q_len):
            dist, r, c = queue.popleft()

            for dy, dx in MOVES_ADJACENT:
                rr = r + dy
                cc = c + dx
                if (rr, cc) == CUR:
                    print(dist + 1, rr, cc)
                    return

                if not 0 < rr < H - 1 or not 0 < cc < W - 1 or (rr, cc) in flakes_set or (dist + 1, rr, cc) in seen:
                    continue
                
                queue.append((dist + 1, rr, cc))
                seen.add((dist + 1, rr, cc))

            if (r, c) not in flakes_set and (dist + 1, r, c) not in seen:
                queue.append((dist + 1, r, c))
                seen.add((dist + 1, r, c))
solve1()

queue = deque([(0, CUR[0], CUR[1])])
seen = set()
seen.add((0, CUR[0], CUR[1]))
def solve2():
    global flakes, m, CUR, END
    for round in range(1, 100000000000000):
        # print(round)
        new_flakes = []

        for flake, r, c in flakes:
            rr, cc = get_next_location(flake, r, c)
            new_flakes.append((flake, rr, cc))
        
        assert(len(new_flakes) == ORIGINAL_FLAKES_COUNT)
        flakes = new_flakes

        flakes_set = set([(r,c) for _, r, c in flakes])
        
        q_len = len(queue)
        assert(q_len > 0)
        for _ in range(q_len):
            dist, r, c = queue.popleft()

            for dy, dx in MOVES_ADJACENT:
                rr = r + dy
                cc = c + dx
                if (rr, cc) == END:
                    print(dist + 1, rr, cc)
                    return

                if not 0 < rr < H - 1 or not 0 < cc < W - 1 or (rr, cc) in flakes_set or (dist + 1, rr, cc) in seen:
                    continue
                
                queue.append((dist + 1, rr, cc))
                seen.add((dist + 1, rr, cc))

            if (r, c) not in flakes_set and (dist + 1, r, c) not in seen:
                queue.append((dist + 1, r, c))
                seen.add((dist + 1, r, c))
solve2()