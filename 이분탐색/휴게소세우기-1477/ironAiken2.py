from sys import stdin
input = stdin.readline

n, m, l = [int(x) for x in input().split()]
inp = [0] + [int(x) for x in input().split()] + [l]
inp.sort()

s, e = 1, l-1
ans = 0
while s <= e:
    mid = (s+e) // 2
    cnt = 0
    for i in range(1, len(inp)):
        if inp[i] - inp[i-1] > mid:
            cnt += (inp[i] - inp[i-1] - 1) // mid
    
    if cnt > m:
        s = mid + 1
    else:
        e = mid - 1
        ans = mid

print(ans)
