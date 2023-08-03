import heapq
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
index = 1
index_list = []
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t, index))
    graph[b].append((a, t, index))
    index += 1

res = []


def dijkstra(prohibit):
    global res
    distance = [sys.maxsize for _ in range(n+1)]
    distance[1] = 0
    q = []
    heapq.heappush(q, (0, 1, []))
    while q:
        dist, now, route = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next, time, index in graph[now]:
            if index == prohibit:
                continue
            if dist + time < distance[next]:
                distance[next] = dist+time
                if next == n:
                    res = route + [index]
                heapq.heappush(q, (dist + time, next, route + [index]))
    return distance[n]


shortest_path = dijkstra(0)
longest_path = 0
for prohibit_index in res:
    longest_path = max(longest_path, dijkstra(prohibit_index))
    if longest_path == sys.maxsize:
        print(-1)
        exit()

print(longest_path-shortest_path)
