import bitarray
import time
import random
import sys
from bitarray.util import int2ba
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
        self.split()


    def split(self):
        input_bit = self.str_to_bit()
        self.r = random.randint(0, len(input_bit)/2 - 1)
        self.rules_int = random.sample(range(0, pow(2, 2*self.r + 1) - 1), self.k - 2)
        rules_bit = self.rules_to_bit()
        self.automata.append((0, input_bit))

        for i in range(1, self.k):
            cells = [random.randint(0, 1) for x in range(len(input_bit))]
            self.automata.append((i, cells))

        m = random.randint(self.k, self.k * 2)
        for i in range(self.k, m + self.n):



        time.sleep(1)

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
