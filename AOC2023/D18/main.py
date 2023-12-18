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
import hashlib
from time import sleep
from enum import Enum

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
class D(Enum):
    LEFT,RIGHT,UP,DOWN = 0,1,2,3

def get_d(i):
    directions = ['R', 'D', 'L', 'U']
    return directions[i]

def get_delta(aim):
    if aim == 'L': return (0,-1)
    elif aim == 'R': return (0,1)
    elif aim == 'U': return (-1,0)
    elif aim == 'D': return (1,0)

fin = sys.stdin.read().strip().split('\n')
y,x = 0,0
for line_id, line in enumerate(fin):
    _, _, real = line.split()
    v = int(real[2:-2], 16)
    d = get_d(int(real[-2]))
    dy,dx = get_delta(d)
    print(dy, dx, v)