import sys
import math
from pprint import pprint as pprint
import heapq
from copy import *
from collections import *
import functools

sys.setrecursionlimit(100000000)

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.components = size
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        if not self.is_connected(x, y):
            rootX = self.root[x]
            rootY = self.root[y]
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.components -= 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def distinct_components(self):
        return self.components

def debM(m):
    for r in m:
        for c in r:
            print(c, end='')
        print()
    print()


MOVES_ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]
fin = sys.stdin.read().strip()
s = fin
tobin = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}
# Parse input into binary
s = ''.join([tobin[c] for c in s])
ret = 0
while(s):
    version = int(s[:3], 2)
    ret += version

    typeID = int(s[3:6], 2)
    if typeID == 4:
        content = s[6:]
        print(version, typeID, content)
        combined = ''
        for i in range(0, len(content), 5):
            part = content[i:i + 5]
            combined += part[1:]
            if part[0] == '0':
                print("Total", int(combined, 2))
                s = content[i + 5:]
                if len(s) < 6:
                    s = 0
                break
    else:
        operator = int(s[6:7],2)
        if operator == 0:
            packetLen = int(s[7:7+15],2)
            content = s[7+15:7+15+packetLen]
            s = content
            print(packetLen, content)
        else:
            subpacketCount = int(s[7:7+11], 2)
            content = s[7+11:]
            print(subpacketCount, content)
print(ret)
# 110 100 01010 
# 010 100 10001 00100