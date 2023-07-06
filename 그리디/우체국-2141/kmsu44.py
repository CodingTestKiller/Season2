n = int(input())

L = []
S = 0
for _ in range(n):
    a, b = map(int, input().split())
    S += b
    L.append([a, b])
L.sort(key=lambda x: x[0])


i = 0
cnt = 0
while i < n:
    cnt += L[i][1]
    if cnt >= S / 2:
        res = L[i][0]
        break
    i += 1


print(res)
