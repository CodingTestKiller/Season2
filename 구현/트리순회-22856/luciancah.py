import sys
sys.setrecursionlimit(10**9)
n, a, r = -1, -1, -1
relation = {}


def input_data():
    global n
    n = int(input())
    for _ in range(n):
        a, b, c = map(int, input().split())
        relation[a] = (b, c)


def travel(cur, flag):
    global a, r
    if cur == -1:
        return

    a += 1
    travel(relation[cur][0], False)

    if flag:
        r += 1
        travel(relation[cur][1], True)
    else:
        travel(relation[cur][1], False)


def solution():
    input_data()
    travel(1, True)
    print(2 * a - r)


if __name__ == "__main__":
    solution()
