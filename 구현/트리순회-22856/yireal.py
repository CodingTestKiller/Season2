import sys
inp = sys.stdin.readline
sys.setrecursionlimit(10**5)
n = int(inp())
cnt = 0
flag = 0
tree = [[0,0] for _ in range(n+1)]
visit = []
for i in range(n):
    a,b,c = map(int,inp().split())
    tree[a][0] = b
    tree[a][1] = c
def dfs(pos):
    global cnt
    if tree[pos][0] != -1 :
        cnt += 1
        dfs(tree[pos][0])
    if pos not in visit:
        visit.append(pos)
    if len(visit) == n:
        print(cnt)
        exit()
    if tree[pos][1] != -1:
        cnt += 1
        dfs(tree[pos][1])
    cnt += 1
dfs(1)