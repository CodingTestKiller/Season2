import sys
import heapq

input = sys.stdin.readline
n, m, a, b, c = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

res = sys.maxsize


def dijkstra(mid):
    q = []
    heapq.heappush(q, (0, a))
    distance = [sys.maxsize] * (n+1)
    distance[a] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for vertex, weight in graph[now]:
            if weight > mid:
                continue
            if dist + weight < distance[vertex]:
                distance[vertex] = dist + weight
                heapq.heappush(q, (dist+weight, vertex))
    if distance[b] > c:
        return False
    else:
        return True


l = 1
r = 10 ** 14

res = 0
if not dijkstra(c):
    print(-1)
    exit()
while l <= r:
    mid = (l+r)//2
    if dijkstra(mid):
        res = mid
        r = mid - 1
    else:
        l = mid + 1
print(res)
