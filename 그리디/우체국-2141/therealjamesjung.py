from sys import stdin

n = int(stdin.readline())

town = []
population = 0

for _ in range(n):
    current = [int(x) for x in input().split()]
    population += current[1]
    town.append(current)

town.sort(key=lambda x: x[0])
s = 0

for i in range(n):
    s += town[i][1]
    if s >= population / 2:
        print(town[i][0])
        break