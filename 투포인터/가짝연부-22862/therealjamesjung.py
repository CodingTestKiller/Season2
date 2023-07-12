from sys import stdin

input = stdin.readline

n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

l, r = 0, -1
result, odd_cnt = 0, 0

while True:
    if odd_cnt <= k:
        result = max(r-l+1-odd_cnt, result)
        r += 1
        if r >= n:
            break
        if arr[r] % 2 == 1:
            odd_cnt += 1
    else:
        if arr[l] % 2 == 1:
            odd_cnt -= 1
        l += 1
        if l > r:
            break

print(result)
