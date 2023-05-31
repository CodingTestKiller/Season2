from sys import stdin
from itertools import permutations
from collections import deque

input = stdin.readline

maps = [[[int(x) for x in input().split()] for _ in range(5)]
        for __ in range(5)]


def rotate_map(map):
    return list(zip(*map[::-1]))


moves = [(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]


def bfs(matrix):
    q = deque()
    q.append((0, 0, 0))
    visited = [[[0] * 5 for _ in range(5)] for __ in range(5)]
    visited[0][0][0] = 0
    while q:
        x, y, z = q.popleft()
        for dx, dy, dz in moves:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5 and matrix[nx][ny][nz] == 1 and visited[nx][ny][nz] == 0:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                q.append((nx, ny, nz))
    if visited[4][4][4] == 0:
        return 1000000000
    return visited[4][4][4]


sequences = list(permutations([0, 1, 2, 3, 4]))

result = 1000000000

for sequence in sequences:
    map1 = maps[sequence[0]]
    map2 = maps[sequence[1]]
    map3 = maps[sequence[2]]
    map4 = maps[sequence[3]]
    map5 = maps[sequence[4]]

    for a in range(4):
        map1 = rotate_map(map1)
        for b in range(4):
            map2 = rotate_map(map2)
            for c in range(4):
                map3 = rotate_map(map3)
                for d in range(4):
                    map4 = rotate_map(map4)
                    for e in range(4):
                        map5 = rotate_map(map5)

                        matrix = [map1, map2, map3, map4, map5]
                        if matrix[0][0][0] == 1 and matrix[4][4][4] == 1:
                            result = min(result, bfs(matrix))

if result == 1000000000:
    print(-1)
else:
    print(result)
