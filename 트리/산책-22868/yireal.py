import sys
from collections import deque
inp = sys.stdin.readline
n,m = map(int,inp().split())
vertex = [[] for _ in range (n+1)]
distance = [10001 for _ in range (n+1)]
for _ in range(m):
    a,b = map(int,inp().split())
    vertex[a].append(b)
    vertex[b].append(a)
for i in range(1,n+1):
    vertex[i].sort()
s,e = map(int,inp().split())
que = deque()
visit_done = []
def bfs(start,end):
    visit = []
    if start not in visit:
        visit.append(start)
    que.append((start,1))
    while que:
        p,d = que.popleft()
        if distance[p] > d:
            distance[p] = d
        for i in vertex[p]:
            if i == end:
                distance[i] = d+1
                visit.append(i)
                return d+1
            if i not in visit and i not in visit_done:
                visit.append(i)
                que.append((i,d+1))
def dfs(pos,cnt):
    visit = []
    visit.append(pos)
    visit_done.append(pos)
    print(pos)
    if pos == e:
        return
    for i in vertex[pos]:
        if distance[pos] + 1 == distance[i]:
            visit.append(i)
            dfs(i,cnt + 1)
        else:
            for _ in range(cnt - 1):
                visit_done.pop(-1)
            return
print(vertex)
cnt = 0
cnt += bfs(s,e)
dfs(s,0)
print(visit_done)
cnt += bfs(e,s) -1
print(cnt)