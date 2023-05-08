from sys import stdin
from collections import deque

input = stdin.readline

n, m = [int(x) for x in input().split()]

directory = {}

for _ in range(n+m):
    p, c, flag = [x.strip() for x in input().split()]
    try:
        directory[p].append(c)
    except KeyError:
        directory[p] = [c, ]
    if flag == '1' and c not in directory.keys():
        directory[c] = []

# print(directory)

n = int(input())

for _ in range(n):
    current = input().strip().split('/')[-1]
    files = set()
    file_cnt = 0
    q = deque(directory[current])

    while q:
        current = q.popleft()

        if current in directory.keys():
            q += directory[current]
        else:
            files.add(current)
            file_cnt += 1

    print(len(files), file_cnt)
    # 4
    # main
    # main/FolderA
    # main/FolderB
    # main/FolderB/FolderC
