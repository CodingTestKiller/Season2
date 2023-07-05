import sys
inp = sys.stdin.readline
n = int(inp())
table = []
total = 0
for i in range(n):
    t1,t2 = map(int,inp().split())
    table.append((t1,t2))
    total += t2
if n == 1:
    print(table[0][0])
    exit()
table.sort(key = lambda x:x[0])
cnt = 0
for i in range(n):
    cnt += table[i][1]
    if cnt >= total/2:
        print(table[i][0])
        break
