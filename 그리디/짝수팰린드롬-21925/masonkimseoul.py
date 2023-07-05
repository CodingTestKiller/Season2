import sys
from itertools import combinations

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
is_pelindrome = [0] * N

def check(plist):
    for i in range(len(plist)//2):
        if plist[i] != plist[len(plist) - i - 1]:
            return False
    return True

s = 0
e = 1
answer = 0
while e < N:
    if e == N - 1 and check(numbers[s:e+1]) == False:
        answer = -1
        break
    if check(numbers[s:e + 1]):
        answer += 1
        s = e + 1
        e = s + 1
    else:
        e += 2

print(answer)