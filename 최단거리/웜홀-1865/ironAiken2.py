from sys import stdin, maxsize
input = stdin.readline
from collections import defaultdict

def bellmanford(s):
    dist = [maxsize] * (n + 1)
    dist[s] = 0
    for i in range(n):
        for s, e, w in edges:
            if dist[s] != maxsize and dist[e] > dist[s] + w:
                if i == n - 1:
                    return True
                dist[e] = dist[s] + w
                check[s] += 1
    return False

tc = int(input())
for _ in range(tc):
    n, m, w = [int(x) for x in input().split()]
    edges = []
    for i in range(m+w):
        s, e, t = [int(x) for x in input().split()]
        if i >= m:
            t *= -1
        edges.append((s, e, t))
        if i < m:
            edges.append((e, s, t)) 

    flag = False
    check = defaultdict(int)
    for i in range(0, n+1):
        if check[i] != 0:
            continue
        if bellmanford(i):
            flag = True
            break
    
    print('YES') if flag == True else print('NO')

# 2
# 3 3 1
# 1 2 2
# 1 3 4
# 2 3 1
# 3 1 3
# 3 2 1
# 1 2 3
# 2 3 4
# 3 1 8