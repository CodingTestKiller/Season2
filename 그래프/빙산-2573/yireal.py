import sys
from collections import deque
inp = sys.stdin.readline
n,m = map(int,inp().split())
que = deque()
field = [list(map(int,inp().split())) for _ in range(n)]
index = []
melted = [[0]*m for _ in range(n)]
cnt = 0
cycle = 0
offset = [(0,-1),(0,1),(-1,0),(1,0)]
def set_index(tx,ty):
    visit = [[0]*m for _ in range(n)]
    que.append((tx,ty))
    index.append((tx,ty))
    visit[ty][tx] = 1
    while que:
        x,y = que.popleft()
        for of in offset:
            nx = x + of[0]
            ny = y + of[1]
            if nx >= m or ny >= n or nx < 0 or ny <0:
                continue
            if field[ny][nx] != 0 and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                index.append((nx,ny))
                que.append((nx,ny))
def bfs():
    visit = [[0]*m for _ in range(n)]
    cnt = 1
    tx = index[0][0]
    ty = index[0][1]
    que.append((tx,ty))
    visit[ty][tx] = 1
    while que:
        x,y = que.popleft()
        for of in offset:
            nx = x + of[0]
            ny = y + of[1]
            if nx >= m or ny >= n or nx < 0 or ny <0:
                continue
            if field[ny][nx] != 0 and visit[ny][nx] == 0:
                que.append((nx,ny))
                visit[ny][nx] = 1
                cnt += 1
    if cnt < len(index):
        print(cycle)
        exit()



def melt():
    d_list = []
    for pos in index:
        x = pos[0]
        y = pos[1]
        for of in offset:
            nx = x + of[0]
            ny = y + of[1]
            if nx >= m or ny >= n or nx < 0 or ny <0:
                continue
            if field[ny][nx] == 0:
                melted[y][x] += 1
    for i in index:
        x = i[0]
        y = i[1]
        field[y][x] -= melted[y][x]
        if field[y][x] <= 0:
            field[y][x] = 0
            d_list.append(i)
        melted[y][x] = 0
    for d in d_list:
        index.remove(d)

def find_start():
    for i in range(n):
        for j in range(m):
            if field[i][j] > 0:
                return i,j
    return 0,0
while True:
    pos = find_start()
    if pos == (0,0): break
    if cycle == 0:
        set_index(pos[0],pos[1])
    bfs()
    melt()
    if len(index) == 0:
        break
    cycle += 1
print(0)