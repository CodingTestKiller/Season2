import sys

N, K = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split()))
energy = [0] * N

energy_max = 0
answer = 0

cur, l, r = 0, 0, 0

while True:
    if cur >= K:
        if l == 0:
            energy_max = 0
        else:
            energy_max = max(energy_max, energy[l - 1])
        energy[r - 1] = max(energy[r - 1], energy_max + cur - K)
        cur -= score[l]
        l += 1
    elif r == N: break
    else:
        cur += score[r]
        r += 1

for i in range(N):
    answer = max(answer, energy[i])
print(answer)