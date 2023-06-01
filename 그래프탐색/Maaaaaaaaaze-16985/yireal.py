from itertools import permutations
import sys
from collections import deque
SIZE = 5
inp = sys.stdin.readline
input_cube = [[list(map(int,inp().split())) for _ in range(SIZE)] for _ in range(SIZE)]
l_set = [(1,0),(4,1),(3,4),(0,3)]
r_set = [(3,0),(4,3),(1,4),(0,1)]
v1_set = [(0,0),(4,0),(4,4),(0,4)]
c1_set = [(2,0),(4,2),(2,4),(0,2)]
v2_set = [(1,1),(3,1),(3,3),(1,3)]
c2_set = [(2,1),(3,2),(2,3),(1,2)]
center = [(2,2)]
offset = [[]]*3
offset[0] = [l_set,r_set,v1_set,c1_set]
offset[1] = [v2_set,c2_set]
offset[2] = [center]
move = [(-1,0),(0,-1),(1,0),(0,1)]
que = deque()
def portal(x,y):
    for o in offset:
        for s in o:
            if (x,y) in s:
                return s

                
def bfs():
    cube_level = 0
    cnt = 0
    que.append((0,0,0,0))
    while que:
        x,y,cube_level,cnt = que.popleft()
        print(x,y,cube_level,cnt)
        if x == 4 and y == 4 and cube_level == 4:
            print(cnt)
            exit(0)
        spin = portal(x,y)
        for pos in spin:
            nx = pos[0]
            ny = pos[1]
            if cube_level == 0:
                if cube[cube_level+1][ny][nx] == 0 and visit[cube_level+1][ny][nx] == 0:
                    visit[cube_level+1][ny][nx] = 1
                    que.append((nx,ny,cube_level+1,cnt+1))
            elif cube_level == 4:
                if cube[cube_level-1][ny][nx] == 0 and visit[cube_level-1][ny][nx] == 0:
                    visit[cube_level-1][ny][nx] = 1
                    que.append((nx,ny,cube_level-1,cnt+1))
            else:
                print(visit[cube_level+1][ny][nx])
                if cube[cube_level+1][ny][nx] == 0 and visit[cube_level+1][ny][nx] == 0:
                    visit[cube_level+1][ny][nx] = 1
                    que.append((nx,ny,cube_level+1,cnt+1))
                if cube[cube_level-1][ny][nx] == 0 and visit[cube_level-1][ny][nx] == 0:
                    visit[cube_level-1][ny][nx] = 1
                    que.append((nx,ny,cube_level-1,cnt+1))
        if cube[cube_level][y][x] == 0:
            for pos in move:
                nx = x + pos[0]
                ny = y + pos[1]
                if nx < 0 or ny < 0 or nx >= SIZE or ny >= SIZE:
                    continue
                if cube[cube_level][ny][nx] == 1 or visit[cube_level][ny][nx] == 1:
                    continue
                visit[cube_level][ny][nx] = 1
                que.append((nx,ny,cube_level,cnt+1))                   
                
        
for cube in permutations(input_cube,SIZE):
    visit = [[[0]*SIZE]*SIZE]*SIZE
    bfs()
print(-1)