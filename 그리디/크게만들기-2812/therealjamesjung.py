from sys import stdin
from collections import deque

input = stdin.readline

n, k = [int(x) for x in input().split()]
num = deque([int(x) for x in input().strip()])
result = deque()

for i in range(n):
    while result and result[-1] < num[i] and k > 0:
        result.pop()
        k -= 1
    result.append(num[i])

print(''.join([str(x) for x in result][:len(result) - k]))

