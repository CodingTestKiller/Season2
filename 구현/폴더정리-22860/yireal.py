import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)
inp = sys.stdin.readline
n,m = map(int,inp().split())
dir = defaultdict(list)
file = defaultdict(list)
type_cnt = []
def search_dir(pos):
    global cnt
    cnt += len(file[pos])
    for i in file[pos]:
        if i not in type_cnt:
            type_cnt.append(i)
    for i in dir[pos]:
        search_dir(i)
for i in range(n + m):
    upper,now,c = inp().split()
    c = int(c)
    if c == 1:
        dir[upper].append(now)
    else:
        file[upper].append(now)
q = int(inp())
for i in range(q):
    input_str = list(inp().rstrip().split('/'))
    key = input_str[-1]
    cnt = 0
    type_cnt.clear()
    search_dir(key)
    print(len(type_cnt),cnt)
