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

sys.setrecursionlimit(100000000)

def debM(m):
    for r in m:
        for c in r:
            print(c, end='')
        print()
    print()

ALPHABET = 'AKQJT98765432J'[::-1]
class Hand:
    def __init__(self, label, bid):
        self.label = label
        self.bid = bid
        self.RANK = 0

    def calculate_rank(self):
        if self.five_of_kind():
            return 6
        elif self.four_of_kind():
            return 5
        elif self.full_house():
            return 4
        elif self.three_of_kind():
            return 3
        elif self.two_pair():
            return 2
        elif self.one_pair():
            return 1
        elif self.high_card():
            return 0

    def five_of_kind(self):
        for c in self.label:
            if self.label.count(c) == 5:
                return True
        for c in self.label:
            if self.label.count(c) == 4 and c != 'J' and self.label.count('J') >= 1:
                return True
            if self.label.count(c) == 3 and c != 'J' and self.label.count('J') >= 2:
                return True
            if self.label.count(c) == 2 and c != 'J' and self.label.count('J') >= 3:
                return True
            if self.label.count(c) == 1 and c != 'J' and self.label.count('J') >= 4:
                return True
        return False

    def four_of_kind(self):
        for c in self.label:
            if self.label.count(c) == 4:
                return True
        for c in self.label:
            if self.label.count(c) == 3 and c != 'J' and self.label.count('J') >= 1:
                return True
            if self.label.count(c) == 2 and c != 'J' and self.label.count('J') >= 2:
                return True
            if self.label.count(c) == 1 and c != 'J' and self.label.count('J') >= 3:
                return True
        return False

    def full_house(self):
        distinct = set([c for c in self.label])
        if len(distinct)==2:
            counter=Counter(self.label)
            elements = list(distinct)
            if counter[elements[0]] == 3 and counter[elements[1]] == 2:
                return True
            if counter[elements[0]] == 2 and counter[elements[1]] == 3:
                return True
            
        pairs = [self.label.count(c) == 2 for c in distinct if c != 'J']
        if len(pairs) == 2 and 'J' in distinct:
            return True
        return False
    
    def three_of_kind(self):
        for c in self.label:
            if self.label.count(c) == 3:
                return True
        for c in self.label:
            if self.label.count(c) == 2 and c != 'J' and self.label.count('J') >= 1:
                return True
            if self.label.count(c) == 1 and c != 'J' and self.label.count('J') >= 2:
                return True
        return False
    
    def two_pair(self):
        counter = Counter(self.label)
        twos = 0
        for c, v in counter.items():
            if v==2:
                twos +=1
        if twos == 2:
            return True
        if self.label.count('J') >= 2:
            return True
        if self.label.count('J') >= 1 and twos==1:
            return True
        return False
    
    def one_pair(self):
        counter = Counter(self.label)
        for v in counter.values():
            if v==2:
                return True
        if 'J' in self.label:
            return True
        return False
    
    def high_card(self):
        return ('J' not in self.label) and (len(self.label) == len(set(self.label)))
    
    def __lt__(self, other):
        if self.calculate_rank() == other.calculate_rank():
            for i in range(5):
                if self.label[i] != other.label[i]:
                    return ALPHABET.index(self.label[i]) < ALPHABET.index(other.label[i])
            return True
        return self.calculate_rank() < other.calculate_rank()

MOVES_ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]
fin = sys.stdin.read().strip().split("\n")
cards = []
for line in fin:
    label, bid = line.split()
    bid = int(bid)
    cards.append(Hand(label, bid))
cards.sort()
ret = 0
for i,card in enumerate(cards):
    ret += (i+1) * card.bid
print(ret)