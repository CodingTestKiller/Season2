import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
prefix = [0] * M
tmp = 0

for i in numbers:
    tmp += i
    prefix[tmp%M] += 1

result = prefix[0]
for i in prefix:
    result += i * (i-1) // 2
print(result)