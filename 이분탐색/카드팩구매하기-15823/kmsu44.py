# 2시 25분 시작
N, M = map(int, input().split())
L = list(map(int, input().split()))

l = 1
r = N//M
ans = 0
while l <= r:
    mid = (l+r)//2
    i = 0
    cnt = 0
    move = 0
    while mid + move <= N:
        visited = dict()
        for i in range(move, move + mid):
            if L[i] not in visited:
                visited[L[i]] = i
            else:
                move = visited[L[i]] + 1
                break
        else:
            cnt = cnt + 1
            move = move + mid
    if cnt >= M:
        l = mid + 1
        ans = max(ans, mid)
    else:
        r = mid - 1
print(ans)
