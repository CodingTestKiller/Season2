from sys import stdin, setrecursionlimit
input = stdin.readline
limit_number = 15000
setrecursionlimit(limit_number)

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n):
    n, l, r = [int(x) for x in input().split()]

    tree[n].append(l)
    tree[n].append(r)


def travesal(index: int) -> int:
    cnt = 0

    if tree[index][0] != -1:
        cnt += travesal(tree[index][0]) + 1
    if tree[index][1] != -1:
        cnt += travesal(tree[index][1]) + 1

    return cnt


def back_root_cnt(index: int) -> int:
    cnt = 0

    if tree[index][1] != -1:
        cnt += back_root_cnt(tree[index][1]) + 1

    return cnt


print(travesal(1) * 2 - back_root_cnt(1))
