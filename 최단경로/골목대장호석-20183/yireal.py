import sys
import heapq
inp = sys.stdin.readline
n,m,start,end,bank = map(int,inp().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
cost_list = []
ans = INF
def dijkstra(mid):
    q = []
    heapq.heappush(q,(0,start))
    cost = [INF] * (n+1)
    cost[start] = 0 
    while q:
        cur_cost,now = heapq.heappop(q) 
        if cost[now] != cur_cost:
            continue
        for next_node in graph[now]:
            if next_node[1] > mid:
                continue
            if cost[next_node[0]] > cost[now]+next_node[1]:
                cost[next_node[0]] = cost[now] + next_node[1]
                if next_node[0] == end and cost[next_node[0]] <= bank:
                    return True
                heapq.heappush(q,(cost[next_node[0]],next_node[0]))
    return cost[end] <= bank
for _ in range(m):
    s,e,c = map(int,inp().split())
    graph[s].append((e,c))
    graph[e].append((s,c))
    heapq.heappush(cost_list,-c)
cost_list.sort()    
fr = 0
re = -heapq.heappop(cost_list)
while fr <= re:
    mid = (fr+re)//2
    if dijkstra(mid):
        ans = min(ans,mid)
        re = mid - 1
    else:
        fr = mid + 1
if ans == INF:
    print(-1)
else:
    print(ans)