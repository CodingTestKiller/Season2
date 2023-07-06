import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
numbers = list(map(int, str(sys.stdin.readline().rstrip())))
numbers2 = deque()

for i in range(N):
    while len(numbers2) > 0 and numbers[i] > numbers2[-1] and K > 0:
        numbers2.pop()
        K -= 1
    numbers2.append(numbers[i])

answer = list(map(str, numbers2))
print(''.join(answer[0:len(answer) - K]))
