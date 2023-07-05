import sys

N = int(sys.stdin.readline())
X = list()
heads = 0
for i in range(N):
    X.append(list(map(int, sys.stdin.readline().split())))
    heads += X[i][1]
X.sort(key = lambda x : x[0])

cnt = 0
for i in range(N):
    cnt += X[i][1]
    if cnt >= heads / 2:
        print(X[i][0])
        break