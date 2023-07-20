from sys import stdin
input = stdin.readline

d, n, m = [int(x) for x in input().split()]
stones = []
for _ in range(n):
    inp = int(input())
    stones.append(inp)
stones.sort()
stones.append(d)

s, e = 0, d
ans = 0

while s <= e:
    mid = (s+e) // 2
    flag, cnt = 0, 0

    for stone in stones:
        if stone - flag < mid:
            cnt += 1
        else:
            flag = stone
    
    if cnt <= m:
        s = mid + 1
        ans = mid
    else:
        e = mid - 1

print(ans)
