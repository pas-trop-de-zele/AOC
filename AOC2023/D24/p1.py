import sys
import math
from pprint import pprint as pprint
import heapq
from copy import *
from collections import *
import functools
from math import *
from dataclasses import dataclass
from hashlib import md5
from itertools import permutations
from sympy.ntheory.modular import crt 
from sympy import Point, Line 
import hashlib
from time import sleep
from enum import Enum
import json
import copy

sys.setrecursionlimit(10000000)

def debM(m):
    for r in m:
        for c in r:
            print(c, end='')
        print()
    print()


MOVES_ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]

fin = sys.stdin.read().strip().split('\n')
def get_intersection(A,B):
    pos1,vel1 = A
    x1,y1,_ = pos1
    xv1,yv1,_ = vel1

    pos2,vel2 = B
    x2,y2,_ = pos2
    xv2,yv2,_ = vel2

    l1 = Line(Point(x1,y1), Point(x1+xv1,y1+yv1))
    l2 = Line(Point(x2,y2), Point(x2+xv2,y2+yv2))
    return l1.intersection(l2)
    

stones = []
for line in fin:
    pos, vel = [x.strip() for x  in line.split('@')]
    pos = [int(c.strip()) for c in pos.split(',')]
    vel = [int(c.strip()) for c in vel.split(',')]

    stones.append((pos, vel))

N = len(stones)
# LEFT = 7
# RIGHT = 27
LEFT = 200000000000000
RIGHT = 400000000000000
ret = 0
for i in range(N):
    print(i)
    for j in range(i+1,N):
        if i != j:
            P = get_intersection(stones[i], stones[j])
            if not list(P):
                continue

            X,Y = P[0].evalf() # convert to float for debugging
            
            if not(LEFT <= X <= RIGHT and LEFT <= Y <= RIGHT):
                continue


            pos1,vel1 = stones[i]
            x1,y1,_ = pos1
            xv1,yv1,_ = vel1

            pos2,vel2 = stones[j]
            x2,y2,_ = pos2
            xv2,yv2,_ = vel2

            # make sure intersection is in the future of first stone
            if (xv1 < 0 and X > x1) or (xv1 > 0 and X < x1) or \
                (yv1 < 0 and Y > y1) or (yv1 > 0 and Y < y1):
                continue

            # make sure intersection is in the future of second stone
            if (xv2 < 0 and X > x2) or (xv2 > 0 and X < x2) or \
                (yv2 < 0 and Y > y2) or (yv2 > 0 and Y < y2):
                continue
            ret += 1
        # print("====")
print(ret)
            