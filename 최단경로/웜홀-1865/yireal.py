import sys
inp = sys.stdin.readline
tc = int(inp())
def bellman_ford(start):
    distance = [10001] * (n+1)
    distance[start] = 0
    for i in range(n):
        for node in graph:    
            cur = node[0]
            next_node = node[1]
            cost = node[2]
            if distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                if i == n-1:
                    return True
    return False
for _ in range(tc):
    n,m,w = map(int,inp().split())
    graph = []
    for _ in range(m):
        s,e,t = map(int,inp().split())
        graph.append((s,e,t))
        graph.append((e,s,t))
    for _ in range(w):
        s,e,t = map(int,inp().split())
        graph.append((s,e,-t))
    ans = bellman_ford(1)
    if ans:
        print("YES")
    else:
        print("NO")   