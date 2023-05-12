import sys
from collections import defaultdict, deque

N, M = map(int, sys.stdin.readline().split())
files = defaultdict(list)
folders = defaultdict(list)

for i in range(N + M):
    parent, son, _type = sys.stdin.readline().rstrip().split()
    if _type == '1':
        folders[parent].append(son)
    else:
        files[parent].append(son)

Q = int(sys.stdin.readline())
for i in range(Q):
    query = list(sys.stdin.readline().rstrip().split('/'))
    files_cnt = 0
    files_names = set()

    check = deque([query[-1]])
    while check:
        current = check.popleft()
        if len(files[current]) > 0:
            for j in files[current]:
                files_names.add(j)
            files_cnt+=len(files[current])

        for j in folders[current]:
            check.append(j)

    print(len(files_names), files_cnt)
