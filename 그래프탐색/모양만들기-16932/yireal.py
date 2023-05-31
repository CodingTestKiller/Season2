import sys
from collections import deque
inp = sys.stdin.readline
n,m = map(int,inp().split())
field = [list(map(int,inp().split())) for _ in range(n)]
offset = [(-1,0),(0,-1),(1,0),(0,1)]
que = deque()
visit = [[0]*m for _ in range(n)]
def bfs(sx,sy,level):
    que.append((sx,sy))
    cnt = 1
    while que:
        x,y = que.popleft()
        for o in offset:
            nx = x + o[0]
            ny = y + o[1]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if visit[ny][nx] == level or field[ny][nx] == 0:
                continue
            cnt += 1
            visit[ny][nx] = level
            que.append((nx,ny))
    return cnt
max_cnt = 0
level = 0
for i in range(n):
    for j in range(m):
        level += 1
        if field[i][j] == 0:
            cnt = bfs(j,i,level)
            if max_cnt < cnt:
                max_cnt = cnt
print(max_cnt)