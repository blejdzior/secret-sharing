import bitarray
import time
import random
import sys
from bitarray.util import int2ba
import numpy as np
import re

class Automata:
    def __init__(self, is_split, input, n, k, seed):
        self.input = input
        self.is_split = is_split
        self.n = n
        self.k = k
        if seed is None:
            random.seed()
            self.seed = random.randint(1, sys.maxsize)
            random.seed(self.seed)
        else:
            random.seed(seed)
            self.seed = seed

        self.r = None
        self.rules_int = None
        self.automata = []
        if self.is_split:
            self.split()
        else:
            self.combine()

    def combine(self):
        self.parse_input()

    def parse_input(self):
        k_match = re.search(r"k = (.+)", self.input)
        n_match = re.search(r"n = (.+)", self.input)
        r_match = re.search(r"r = (.+)", self.input)
        rules_match = re.search(r"rules = (.+)", self.input)
        automata_match = re.findall(r"(.+): (.+)", self.input)
        self.k = int(k_match.group(1))
        self.n = int(n_match.group(1))
        self.r = int(r_match.group(1))
        self.rules_int = [(int(i) for i in rules_match.group(1).split(','))]
        self.automata = [(int(i), [int(k) for k in j.strip('][').split(',')]) for i, j in automata_match]
        time.sleep(1)

    def split(self):
        input_bit = self.str_to_bit()
        self.r = random.randint(0, len(input_bit)/2 - 1)
        self.rules_int = random.sample(range(0, pow(2, 2*self.r + 1)), self.k - 1)
        rules_bit = self.rules_to_bit()

        # initial state containing secret bits
        self.automata.append((0, input_bit))

        # k - 1 random initial states
        for i in range(1, self.k):
            cells = [random.randint(0, 1) for x in range(len(input_bit))]
            self.automata.append((i, cells))

        m = random.randint(self.k, self.k * 2)
        for i in range(self.k, m + self.n):
            cells = [self.calc_state(rules_bit, x, i) for x in range(len(input_bit))]
            self.automata.append((i, cells))
    def get_neighbours(self, iter, i):
        neighbours = []
        for j in range(iter - 1, iter - self.k, -1):
            _, cells = self.automata[j]
            for r in range(i - self.r, i + self.r + 1):
                if r >= len(cells):
                    neighbours.append(cells[r - len(cells)])
                else:
                    neighbours.append(cells[r])
        _, cells = self.automata[iter - self.k]
        last_neighbour = cells[i]
        return neighbours, last_neighbour

    def calc_state(self, rules_bit, i, iter):
        neighbours, last_neighbour = self.get_neighbours(iter, i)
        neighbours_rules_applied = list(np.multiply(neighbours, rules_bit))
        neighbours_rules_applied.append(last_neighbour)
        return sum(neighbours_rules_applied) % 2

    def rules_to_bit(self):
        rules_bit = []
        for rule in self.rules_int:
            ba = int2ba(rule, length=2*self.r + 1).tolist()
            rules_bit.append(ba)
        flattened = [val for sublist in rules_bit for val in sublist]
        return flattened
    def str_to_bit(self):
        ba = bitarray.bitarray()
        ba.frombytes(self.input.encode('utf-8'))
        return ba.tolist()
