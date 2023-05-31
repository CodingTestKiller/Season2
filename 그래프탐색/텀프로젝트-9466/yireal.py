import sys
inp = sys.stdin.readline
sys.setrecursionlimit(10**5)
t = int(inp())
def run_cycle(pos,level):
    global cnt
    if cycle[pos] == level:
        tmp = 0
        st = pos
        while True:
            pos = graph[pos]
            tmp += 1
            if pos == st: break
        cnt = tmp
        return
    elif visit[pos] == 1:
        cnt = 0
        return
    elif graph[pos] == pos:
        cnt = 1
        visit[pos] = 1
        return
    else:
        cnt += 1
        cycle[pos] = level
        visit[pos] = 1
        run_cycle(graph[pos],level)
for _ in range(t):
    level = 1
    total = 0    
    n = int(inp())
    visit = [0] * (n+1)
    cycle = [0] * (n+1)
    graph = [0] + list(map(int,inp().split()))
    for i in range(1,n+1):
        if visit[i] == 1: continue
        cnt = 0
        run_cycle(i,level)
        level += 1
        total += cnt
    print(n-total)  
        

    
