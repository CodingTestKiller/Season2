import sys, math

N = int(sys.stdin.readline())
circles = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
circles.sort(key = lambda x:x[2], reverse = True)
circles.insert(0,(0,0,float('inf')))
graph = [[] * (N + 1) for _ in range(N + 1)]
ch = [-1] * (N + 1)

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def DFS(x):
    x1, y1, r1 = circles[x]
    for i in range(x + 1, N + 1):
        if ch[i] == -1:
            x2, y2, r2 = circles[i]
            d = distance(x1, y1, x2, y2)
            if abs(r1 - r2) > d:
                graph[x].append(i)
                graph[i].append(x)
                ch[i] = 1
                DFS(i)

def LFS(L, x):
    global res, st
    if L > res:
        res = L
        st = x

    for y in graph[x]:
        if ch[y] == -1:
            ch[y] = 1
            LFS(L + 1, y)
            ch[y] = -1

DFS(0)

res = -3
st = -1
et = -1

ch = [-1] * (N + 1)
ch[0] = 1
LFS(0, 0)
ch = [-1] * (N + 1)
ch[st] = 1
LFS(0, st)
print(res)