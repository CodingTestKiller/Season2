from itertools import combinations
from collections import defaultdict
import sys


class Bitset:
    def __init__(self, size):
        self.size = size
        self.bits = 0

    def set(self, index):
        mask = 1 << index
        self.bits |= mask

    def reset(self, index):
        mask = 1 << index
        self.bits &= ~mask

    def test(self, index):
        mask = 1 << index
        return bool(self.bits & mask)

    def copy(self):
        new_bitset = Bitset(self.size)
        new_bitset.bits = self.bits
        return new_bitset

    def count(self):
        count = 0
        temp = self.bits
        while temp:
            count += 1
            temp &= temp - 1
        return count

    def xor(self, other):
        if isinstance(other, Bitset) and self.size == other.size:
            self.bits ^= other.bits
        else:
            raise ValueError("Bitset size mismatch or unsupported type")

    def __str__(self):
        return bin(self.bits)[2:].zfill(self.size)


n, m = map(int, input().split())

T = Bitset(n)
array_j = input()
for idx, data in enumerate(array_j):
    if data == '1':
        T.set(idx)

switch = []
for _ in range(m):
    tmp = input()
    bitset = Bitset(n)
    for idx, data in enumerate(tmp):
        if data == '1':
            bitset.set(idx)
    switch.append(bitset)


index = [i for i in range(1, m+1)]


def years(k):
    one_count = k.count()
    return one_count - (n-one_count)


D = {}
for i in range(-n, n+1):
    D[i] = -1

result = []


cnt = 0

L = []

index = [i for i in range(1, m+1)]

for i in range(n):
    L += list(combinations(index, i))

D = defaultdict(list)
for case in L:
    tmp = T.copy()
    for k in case:
        tmp.xor(switch[k-1])
    if not case:
        D[years(T)] = [0]
    if D[years(tmp)]:
        continue
    else:
        D[years(tmp)] = case

for i in range(-n, n+1):
    if D[i]:
        if D[i] == [0]:
            print(0)
        else:
            print(len(D[i]), *D[i])
    else:
        print(-1)
