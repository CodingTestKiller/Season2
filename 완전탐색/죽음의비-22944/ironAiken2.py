from sys import stdin
input = stdin.readline
from collections import deque

n, h, d = [int(x) for x in input().split()]
_map = [[str(x) for x in input().rstrip()] for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]
moves = [[0,1],[0,-1],[1,0],[-1,0]]
flag = False

def bfs(x: int, y: int) -> int:
    global flag, h, d

    q = deque()
    q.append(([x,y], h, 0, 0))
    visit[x][y] = h

    while q:
        index, health, umb, dist = q.popleft()

        for move in moves:
            nx, ny = index[0] + move[0], index[1] + move[1]
            nhealth, numb = health, umb
            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue

            if _map[nx][ny] == 'E':
                return dist + 1
            if _map[nx][ny] == 'U':
                numb = d
            if numb == 0:
                nhealth -= 1
            else:
                numb -= 1

            if visit[nx][ny] < nhealth:
                visit[nx][ny] = nhealth
                q.append(([nx,ny], nhealth, numb, dist + 1))

    

    return -1
        


for i in range(n):
    for j in range(n):
        if _map[i][j] == 'S':
            ans = bfs(i, j)

print(ans)