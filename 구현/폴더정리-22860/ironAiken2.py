from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split()]

dic = {}

for _ in range(n+m):
    p, f, c = [str(x) for x in input().rstrip().split()]

    try:
        dic[p].append((f, c))
    except KeyError:
        dic[p] = []
        dic[p].append((f, c))


def find(name: str) -> None:
    try:
        for n in dic[name]:
            if n[1] == '0':
                ans.append(n[0])
            else:
                find(n[0])
    except KeyError:
        return


q = int(input())
for _ in range(q):
    arr = [str(x) for x in input().rstrip().split('/')]

    ans = []

    find(arr[-1])
    print(len(list(set(ans))), len(ans))
