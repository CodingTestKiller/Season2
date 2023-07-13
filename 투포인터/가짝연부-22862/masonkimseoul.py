import sys

N, K = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

p1, p2 = 0, 0
cnt = 0
answer = 0
distance = 0

while p1 < N and p2 < N:
    if numbers[p1] % 2 == 1:
        p1 += 1
        if cnt > 0:
            cnt -=1
        else:
            p2 = max(p1, p2)
    else:
        if numbers[p2] % 2 == 1:
            if cnt >= K:
                if numbers[p1] % 2 ==0:
                    distance -=1
                p1 += 1
            else:
                cnt += 1
                p2 += 1
        else:
            p2 += 1
            distance += 1
    answer = max(answer, distance)
print(answer)