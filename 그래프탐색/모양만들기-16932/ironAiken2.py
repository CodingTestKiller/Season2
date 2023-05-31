from collections import deque
from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split()]
arr = [[int(x) for x in input().split()] for _ in range(n)]
moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visit = [[0 for _ in range(m)] for _ in range(n)]
count = [[0 for _ in range(m)] for _ in range(n)]


def bfs_same(i: int, j: int, flag: int) -> int:
    q = deque()
    q.append((i, j))
    visit[i][j] = flag

    cnt = 1

    while q:
        ii, jj = q.popleft()
        for move in moves:
            ni, nj = ii + move[0], jj + move[1]
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            if visit[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                visit[ni][nj] = flag
                cnt += 1

    return cnt


def bfs_cnt(i: int, j: int, cnt: int) -> None:
    q = deque()
    q.append((i, j))
    count[i][j] = cnt

    while q:
        ii, jj = q.popleft()
        for move in moves:
            ni, nj = ii + move[0], jj + move[1]
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            if count[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                count[ni][nj] = cnt


flag = 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visit[i][j] == 0:
            cnt = bfs_same(i, j, flag)
            flag += 1
            bfs_cnt(i, j, cnt)

ans = 0

for i in range(n):
    for j in range(m):
        check = []
        flag = 1
        if arr[i][j] != 0:
            continue

        for move in moves:
            ni, nj = i + move[0], j + move[1]
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            if arr[ni][nj] == 1 and visit[ni][nj] not in check:
                check.append(visit[ni][nj])
                flag += count[ni][nj]

        ans = max(ans, flag)
print(ans)
