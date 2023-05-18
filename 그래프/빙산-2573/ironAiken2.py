from sys import stdin
input = stdin.readline
from copy import deepcopy
from collections import deque

n, m = [int(x) for x in input().split()]
_map = [[int(x) for x in input().split()] for _ in range(n)]
_map_copy = [[0 for _ in range(m)] for _ in range(n)]
moves = [[-1,0], [1, 0], [0, -1], [0, 1]]

def bfs(x:int, y:int) -> None:
    q = deque()
    q.append((x, y))
    visit[x][y] = True

    while q:
        i, j = q.popleft()

        for move in moves:
            nx, ny = i + move[0], j + move[1]

            if _map[nx][ny] != 0 and visit[nx][ny] == False:
                q.append((nx, ny))
                visit[nx][ny] = True

flag = True
cnt = 0
while flag:
    flag = False
    flag2 = 0
    visit = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            zero_cnt = 0
            if _map[i][j] == 0:
                _map_copy[i][j] = 0
                continue
            
            for move in moves:
                nx, ny = i + move[0], j + move[1]

                try:
                    if _map[nx][ny] == 0:
                        zero_cnt += 1
                except IndexError:
                    continue
            
            _map_copy[i][j] = 0 if _map[i][j] - zero_cnt <= 0 else _map[i][j] - zero_cnt

            if visit[i][j] == False:
                flag = True
                bfs(i, j)
                flag2 += 1

            if flag2 >= 2:
                print(cnt)
                exit()

    _map = deepcopy(_map_copy)
    cnt += 1

print(0)
    