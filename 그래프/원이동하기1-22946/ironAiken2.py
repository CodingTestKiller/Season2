from sys import stdin
input = stdin.readline

n = int(input())
circles = [[int(x) for x in input().split()] for _ in range(n)]
_map = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j: continue

        d = ((circles[i][0] - circles[j][0]) ** 2 + (circles[i][1] - circles[j][1]) ** 2) ** 0.5
        if circles[i][2] + circles[j][2] < d:
            continue
        if abs(circles[i][2] - circles[j][2]) > d or d == 0:
            _map[i].append(j) if circles[i][2] > circles[j][2] else _map[j].append(i)

for i, data in enumerate(_map):
    _map[i] = list(set(data))

visit = [False for _ in range(n)]

def find_depth(i: int, cnt: int) -> list:
    ans = []
    ans.append(i)

    for child in _map[i]:
        if visit[child] == True:
            continue
        flag = find_depth(child, cnt + 1)
        if len(ans) <= len(flag):
            ans += flag

    return ans

result = 0
ans = []
for i in range(n):
    if visit[i] == True:
        continue
    _ret = find_depth(i, 0)
    if len(ans) <= len(_ret):
        ans = _ret[:]

result += len(ans)
for data in ans:
    visit[data] = True
    
rem = ans[0]

ans2 = []
for i in range(n):
    if visit[i] == True:
        continue
    _ret = find_depth(i, 0)
    if len(ans2) <= len(_ret):
        ans2 = _ret[:]
result += len(ans2)
cnt = 0
for data in ans:
    if ans2[0] in _map[data]:
        cnt += 1

print(result - cnt)