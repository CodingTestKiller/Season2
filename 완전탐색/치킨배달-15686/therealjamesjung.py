from itertools import combinations
import sys

input = sys.stdin.readline

n, m = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(n)]

chickens = []
houses = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            houses.append((i, j))
        elif matrix[i][j] == 2:
            chickens.append((i, j))

cases = list(combinations(chickens, m))


def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


result = 100000000

for case in cases:
    current_dist = 0
    for house in houses:
        current_dist += min([get_distance(house, chicken) for chicken in case])
    result = min(result, current_dist)

print(result)
