n, k = map(int, input().split())
L = list(map(int, input()))

S = []
for i in range(n):
    if k < 0:
        break
    while S and S[-1] < L[i] and k > 0:
        tmp = S.pop()
        k -= 1
    S.append(L[i])

for i in S:
    print(i, end='')
