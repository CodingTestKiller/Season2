from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split()]

arr = [[int(x) for x in input().split()] for _ in range(n)]
result = [[0 for _ in range(n)] for _ in range(n)]

middle = m // 2

s, e = middle, n - middle


def is_possible(x, y):

    result[x][y] -= arr[x - middle][y - middle]
    if x - middle - 1 >= 0:
        result[x][y] += arr[x - middle - 1][y - middle]
    if y - middle - 1 >= 0:
        result[x][y] += arr[x - middle][y - middle - 1]
    if x - middle - 1 >= 0 and y - middle - 1 >= 0:
        result[x][y] -= arr[x - middle - 1][y - middle - 1]
    if x - m >= 0:
        result[x][y] += result[x - m][y]
    if y - m >= 0:
        result[x][y] += result[x][y - m]
    if x - m >= 0 and y - m >= 0:
        result[x][y] -= result[x - m][y - m]


for i in range(s, e):
    for j in range(s, e):
        is_possible(i, j)

for a in result:
    print(*a)
