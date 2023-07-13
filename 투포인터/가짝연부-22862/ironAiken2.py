from sys import stdin
input = stdin.readline

n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

if n == 1:
    print(0) if arr[-1] % 2 != 0 else print(1)
    exit()
p1, p2 = 0, 1
odd_cnt = 1 if arr[p1] % 2 != 0 else 0
odd_cnt += 1 if arr[p2] % 2 != 0 else 0
MAX = 1 if arr[0] % 2 == 0 else 0

while True:
    if p1 > p2 or p1 == len(arr) or p2 == len(arr):
        break
    if MAX < p2 - p1 and odd_cnt <= k:
        MAX = p2 - p1
    if odd_cnt <= k:
        p2 += 1
        if p2 == len(arr):
            break
        if arr[p2] % 2 != 0:
            odd_cnt += 1
    else:
        if arr[p1] % 2 != 0:
            odd_cnt -= 1
        p1 += 1
        if p1 == len(arr):
            break


print(MAX - odd_cnt + 1)
        
    