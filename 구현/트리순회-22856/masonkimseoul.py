import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())
tree = [0] * (N + 1)
visited = [0] * (N+1)

for i in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a] = [b,c]

def inorder(node):
    global cnt1
    visited[node] = 1
    if tree[node][0] != -1 and visited[tree[node][0]] == 0:
        inorder(tree[node][0])
        cnt1 += 1
    if tree[node][1] != -1 and visited[tree[node][1]] == 0:
        inorder(tree[node][1])
        cnt1 += 1

def modified_inorder(node):
    global cnt2
    if tree[node][1] != -1:
        modified_inorder(tree[node][1])
        cnt2 += 1

cnt1 = 0
cnt2 = 0
inorder(1)
modified_inorder(1)
print(cnt1 * 2 - cnt2)