import sys
sys.setrecursionlimit(100000)
# 2시 50분 시작

T = int(input())

res = 0


# 미방문 1 방문 0 싸이클 1
def Find_Team(i):
    global res
    visit[i] = False
    circle.append(i)
    # 미방문시 다음 노드 방문
    if visit[L[i]]:
        Find_Team(L[i])
    # 방문 시 사이클 반환
    else:
        if L[i] in circle:
            res += len(circle[circle.index(L[i]):])
    return 0


answer = []
for _ in range(T):
    n = int(input())
    L = [0] + list(map(int, input().split()))
    visit = [True] * (n+1)
    for i in range(1, n+1):
        circle = []
        if visit[i]:
            Find_Team(i)
    answer.append(n-res)
    res = 0

for i in answer:
    print(i)
