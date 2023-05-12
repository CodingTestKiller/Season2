from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n = int(input())
graph = [[0 for _ in range(3)] for _ in range(n+1)]
for _ in range(n):
    node, left, right = map(int, input().split())
    graph[node][0] = left
    graph[node][1] = right
    if left != -1:
        graph[left][2] = node
    if right != -1:
        graph[right][2] = node

q = []
visit = [True for _ in range(n+1)]


def order(node):
    if graph[node][0] != -1 and visit[graph[node][0]]:
        order(graph[node][0])
    q.append(node)
    visit[node] = False
    if graph[node][1] != -1 and visit[graph[node][1]]:
        order(graph[node][1])


order(1)
last = q[-1]
visit = [True for _ in range(n+1)]
cnt = 0
visit_cnt = 0
node = 1

while True:
    left, right = graph[node][0], graph[node][1]
    visit[node] = False
    if left != -1 and visit[left]:
        node = left
        cnt += 1
    elif right != -1 and visit[right]:
        node = right
        cnt += 1
    elif node == last:
        break
    else:
        if graph[node][2] != 0:
            node = graph[node][2]
            cnt += 1
print(cnt)

# 2
# 1 2 -1
# 2 -1 -1
