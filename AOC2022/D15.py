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

def mandist(x, y, xx, yy):
    return abs(x - xx) + abs(y - yy)

fin = sys.stdin.read().strip().split("\n")
sensors = set()
beacons = set()

MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]
H = W = 4000000

for l in fin:
    l = l.split()
    sensorx, sensory = int(l[2][2:-1]), int(l[3][2:-1])
    beaconx, beacony = int(l[8][2:-1]), int(l[9][2:])
    sensor_range = mandist(sensorx, sensory, beaconx, beacony)
    sensors.add((sensorx, sensory, sensor_range))
    beacons.add((beaconx, beacony))


def get_ranges(y):
    all_taken = []
    for sensorx, sensory, sensor_range in sensors:
        x_diff = sensor_range - abs(sensory - y)
        if x_diff < 0:
            continue
        left = sensorx - x_diff
        right = sensorx + x_diff
        all_taken.append((left, right))
    for beaconx, beacony in beacons:
        if y == beacony:
            all_taken.append((beaconx, beaconx))
    all_taken.sort()
    return all_taken

def merge_ranges(all_taken):
    merged = []
    prev = all_taken[0]
    for taken in all_taken[1:]:
        l, r = taken
        if prev[1] + 1 < l:
            merged.append(prev)
            prev = taken
        else:
            prev = [min(prev[0], l),  max(prev[1],r)]
    merged.append(prev)
    return merged

def find():
    for y in range(H + 1):
        # print(y)
        takens = get_ranges(y)
        taken_ranges = merge_ranges(takens)
        if len(taken_ranges) > 1:
            print(y, taken_ranges)
            return
find()

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

def mandist(x, y, xx, yy):
    return abs(x - xx) + abs(y - yy)

fin = sys.stdin.read().strip().split("\n")
sensors = set()
beacons = set()

MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]
H = W = 4000000

for l in fin:
    l = l.split()
    sensorx, sensory = int(l[2][2:-1]), int(l[3][2:-1])
    beaconx, beacony = int(l[8][2:-1]), int(l[9][2:])
    sensor_range = mandist(sensorx, sensory, beaconx, beacony)
    sensors.add((sensorx, sensory, sensor_range))
    beacons.add((beaconx, beacony))


def get_ranges(y):
    all_taken = []
    for sensorx, sensory, sensor_range in sensors:
        x_diff = sensor_range - abs(sensory - y)
        if x_diff < 0:
            continue
        left = sensorx - x_diff
        right = sensorx + x_diff
        all_taken.append((left, right))
    for beaconx, beacony in beacons:
        if y == beacony:
            all_taken.append((beaconx, beaconx))
    all_taken.sort()
    return all_taken

def merge_ranges(all_taken):
    merged = []
    prev = all_taken[0]
    for taken in all_taken[1:]:
        l, r = taken
        if prev[1] + 1 < l:
            merged.append(prev)
            prev = taken
        else:
            prev = [min(prev[0], l),  max(prev[1],r)]
    merged.append(prev)
    return merged

def find():
    for y in range(H + 1):
        # print(y)
        takens = get_ranges(y)
        taken_ranges = merge_ranges(takens)
        if len(taken_ranges) > 1:
            print(y, taken_ranges)
            return
find()

