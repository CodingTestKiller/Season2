import heapq
N, M, L = map(int, input().split())
pos = []
if N != 0:
    pos = list(map(int, input().split()))

pos.append(0)
pos.append(L)
pos.sort()

l, r = 1, L-1

ans = 0
while l < r:
    cnt = 0
    mid = (l+r) // 2
    for i in range(1, len(pos)):
        if (pos[i] - pos[i-1]-1) >= mid:
            cnt += (pos[i] - pos[i-1]-1) // mid
    if cnt > M:
        l = mid+1
    else:
        r = mid


print(r)
