from sys import stdin, maxsize
from collections import deque
from itertools import permutations
MAX = maxsize
input = stdin.readline

maps = [[[int(x) for x in input().split()] for _ in range(5)]
        for __ in range(5)]
moves = [(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]


def spin(map):
    return list(zip(*map[::-1]))


def bfs(matrix):
    visit = [[[0] * 5 for _ in range(5)] for __ in range(5)]

    q = deque()
    q.append((0, 0, 0))
    visit[0][0][0] = 0

    while q:
        x, y, z = q.popleft()
        for move in moves:
            nx, ny, nz = x + move[0], y + move[1], z + move[2]
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5 and matrix[nx][ny][nz] == 1 and visit[nx][ny][nz] == 0:
                visit[nx][ny][nz] = visit[x][y][z] + 1
                q.append((nx, ny, nz))

    if visit[4][4][4] == 0:
        return MAX
    return visit[4][4][4]


steps = list(permutations([0, 1, 2, 3, 4]))
ans = MAX

for step in steps:
    map1, map2, map3, map4, map5 = maps[step[0]], maps[step[1]
                                                       ], maps[step[2]], maps[step[3]], maps[step[4]]

    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    for e in range(4):
                        matrix = [map1, map2, map3, map4, map5]
                        if matrix[0][0][0] == 1 and matrix[4][4][4] == 1:
                            ans = min(ans, bfs(matrix))
                            if ans == 12:
                                print(12)
                                exit()
                        map1 = spin(map1)
                    map2 = spin(map2)
                map3 = spin(map3)
            map4 = spin(map4)
        map5 = spin(map5)


if ans == MAX:
    print(-1)
else:
    print(ans)
