from collections import deque
from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + [int(x) for x in input().split()]
    visit = [True] + [False for _ in range(n)]
    no_team = []

    for i in range(1, len(arr)):
        if visit[i] == True:
            continue
        if i == arr[i]:
            visit[i] = True
            continue

        cycle = []

        q = deque()
        q.append(i)
        visit[i] = True
        cycle.append(i)

        while q:
            val = q.popleft()
            if visit[arr[val]] == False:
                q.append(arr[val])
                visit[arr[val]] = True
                cycle.append(arr[val])
        cycle.append(arr[val])

        for val in cycle:
            if val == cycle[-1]:
                break
            no_team.append(val)

    print(len(set(no_team)))
