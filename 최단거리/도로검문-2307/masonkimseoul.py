import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, T = map(int, sys.stdin.readline().split())
    graph[A].append([B, T])
    graph[B].append([A, T])
prev = [0 for _ in range(N + 1)]

def dijkstra(s, e):
    cost = [1e9 for _ in range(N + 1)]
    cost[1] = 0
    queue = [[0,1]]
    while queue:
        time, cur = heapq.heappop(queue)
        if cur == N:
            break
        for p1, p2 in graph[cur]:
            if s == cur and e == p1 or s == p1 and e == cur:
                continue

            if time + p2 < cost[p1]:
                cost[p1] = time + p2
                if not s:
                    prev[p1] = cur
                heapq.heappush(queue, [cost[p1],p1])
    return cost[N]

answer = dijkstra(0,0)
res = -1
e = N
while prev[e] != 0:
    s = prev[e]
    tmp = dijkstra(s, e)
    if tmp != 1e9:
        diff= tmp - answer
        res = max(res, diff)
    else:
        res = -1
        break
    e = s

print(res)