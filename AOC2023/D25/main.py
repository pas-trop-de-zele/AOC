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
from itertools import permutations, combinations
from sympy.ntheory.modular import crt 
from sympy import Point3D, Line3D
import hashlib
from time import sleep
from enum import Enum
import json
import copy
import networkx as nx

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
nodes = set()
G = nx.DiGraph()
for line in fin:
    line = line.split()
    u = line[0][:-1]
    nodes.add(u)
    neis = line[1:]
    for v in neis:
        G.add_edge(u, v, capacity=1.0)
        G.add_edge(v, u, capacity=1.0)
        nodes.add(v)

def f():
    """
    For each pair of nodes, if min cut to cut them into 2 parts is 3
    """
    for u in nodes:
        for v in nodes:
            if u != v:
                cut_value, partition = nx.minimum_cut(G, u, v)
                if cut_value == 3:
                    print(len(partition[0]) * len(partition[1]))
                    return

f()