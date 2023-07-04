from sys import stdin, maxsize
input = stdin.readline

n = int(input())
cmd, total = [], 0
for _ in range(n):
    v, p = [int(x) for x in input().split()]
    cmd.append([v,p])
    total += p
cmd.sort(key=lambda x:x[0])
flag = 0
for c in cmd:
    flag += c[1]
    if flag >= total / 2:
        print(c[0])
        break

