from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())

l = [int(x) for x in input().split()]

if n % 2 != 0:
    print(-1)
    exit()

queue = deque([l[0], ])
palindrome = deque([l[0], ])

def is_palindrome(s):
    if len(s) % 2 != 0:
        return False
    l = 0
    r = len(s) - 1
    while True:
        if l >= r:
            return True
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

cnt = 0

for i in range(1, len(l)):
    if len(queue) == 0:
        queue.append(l[i])
        palindrome.append(l[i])
        continue

    if l[i] == queue[-1]:
        queue.pop()
        palindrome.append(l[i])
        if len(queue) == 0:
            if is_palindrome(palindrome):
                cnt += 1
                palindrome = deque()
            else:
                print(-1)
                exit()
    else:
        queue.append(l[i])
        palindrome.append(l[i])

if len(queue) != 0:
    print(-1)
else:
    print(cnt)