from collections import deque
from itertools import combinations, permutations
graph = [list(map(str, input().strip()))for _ in range(5)]


star_cnt = 0
star_pos = []
for i in range(5):
    for j in range(5):
        if graph[i][j] == '*':
            star_cnt += 1
            star_pos.append((i, j))

all_pos = []
for i in range(5):
    for j in range(5):
        all_pos.append((i, j))
compare_star = list(combinations(all_pos, star_cnt))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def is_Connected(x, y, arr, size):
    global cnt
    q = deque()
    q.append((x, y))
    visit = [[True for _ in range(5)] for _ in range(5)]
    visit[x][y] = False
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            kx = dx[i] + cx
            ky = dy[i] + cy
            if 0 <= kx < 5 and 0 <= ky < 5 and visit[kx][ky] and (kx, ky) in arr:
                visit[kx][ky] = False
                cnt += 1
                q.append((kx, ky))
    if cnt == size:
        return True
    else:
        False


P = list(permutations(star_pos, star_cnt))
res = 25
for arr in compare_star:
    cnt = 1
    if is_Connected(arr[0][0], arr[0][1], arr, len(arr)):
        for arr2 in P:
            tmp = 0
            for idx, data in enumerate(arr2):
                x, y = data
                x1, y1 = arr[idx]
                tmp += abs(x1-x) + abs(y1-y)
            res = min(res, tmp)
    else:
        continue

print(res)
