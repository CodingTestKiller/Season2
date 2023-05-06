from collections import deque
n, m = map(int, input().split())
L = list(map(int, input().split()))
M = [0 for _ in range(n)]
R = [0 for _ in range(m)]

M[0] = L[0] % m
R[M[0]] += 1

for i in range(1, n):
    M[i] += (M[i-1] + L[i]) % m
    R[M[i]] += 1

res = 0
for i in range(m):
    if i == 0:
        res += R[i]
    res += (R[i] * (R[i]-1)) // 2
print(res)
