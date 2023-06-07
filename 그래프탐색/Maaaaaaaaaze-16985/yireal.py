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
cube_set =[-1,1]
move = [(-1,0),(0,-1),(1,0),(0,1)]
que = deque()
def portal(x,y):
    for o in offset:
        for s in o:
            if (x,y) in s:
                return s

                
def bfs():
    que.append((0,0,0,1))
    while que:
        x,y,cube_level,cnt = que.popleft()
        print(x,y,cube_level,cnt)
        visit.append((x,y,cube_level))
        if x == 4 and y == 4 and cube_level == 4:
            print(cnt)
            exit(0)
        spin = portal(x,y)
        for pos in spin:
            nx = pos[0]
            ny = pos[1]
            for c in cube_set:
                nc = cube_level + c
                if nc < 0 or nc > 4:
                    continue
                if cube[nc][ny][nx] == 1 or (nx,ny,nc) in visit:
                    continue
                que.append((nx,ny,nc,cnt+1))
        if cube[cube_level][y][x] == 0:
            for pos in move:
                nx = x + pos[0]
                ny = y + pos[1]
                if nx < 0 or ny < 0 or nx >= SIZE or ny >= SIZE:
                    continue
                if cube[cube_level][ny][nx] == 1 or (nx,ny,cube_level) in visit:
                    continue
                que.append((nx,ny,cube_level,cnt+1))                   
                
        
for cube in permutations(input_cube,SIZE):
    visit = []
    bfs()
print(-1)