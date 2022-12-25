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

lookup = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

revlookup = {
    -5: "-0",
    -4: "-1",
    -3: "-2",
    -2: '0=',
    -1: '0-',
    0: '00',
    1: "01",
    2: "02",
    3: "1=",
    4: "1-",
    5: "10",
    6: "11",
    7: "12",
    8: "2=",
    9: "2-"
}

def add_symbol(a, b):
    # Make 2 side same
    if len(a) < len(b):
        a = a.zfill(len(b))
    elif len(b) < len(a):
        b = b.zfill(len(a))
    
    print(a, b)
    a = a[::-1]
    b = b[::-1]
    # print(a, b)
    ret = ''
    remainder = 0
    for x, y in zip(a, b):
        combine = lookup[x] + lookup[y] + remainder
        assert -5 <= combine <= 9
        print(combine)
        ret += revlookup[combine][-1]
        remainder = lookup[revlookup[combine][-2]]
        # print(ret, remainder)
        print(ret)
    if remainder:
        ret += revlookup[remainder][-1]
    return ret[::-1]
"""
1-111=
  2=0=
10=-01
"""

all_sum = 0
symbol = ''

# 429698259232087
# 32969743607087
for l in fin:
    ret = 0
    num = reversed(l)
    power = 0
    for char in num:
        ret += lookup[char] * (5 ** power)
        power += 1
    all_sum += ret
    symbol = add_symbol(symbol, l)
    print("SYMBOL", symbol)

print("SUM", all_sum)



    

