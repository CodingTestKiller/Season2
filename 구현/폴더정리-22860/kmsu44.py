from collections import deque, defaultdict

n, m = map(int, input().split())
Folder = defaultdict(list)
File = defaultdict(list)
INPUT = []
for _ in range(n+m):
    p, f, c = input().split()
    INPUT.append((p, f, c))

for p, f, c in INPUT:
    if c == '1':
        Folder[p].append(f)
    else:
        File[p].append(f)


q = int(input())
answer = []
for _ in range(q):
    query = deque(input().split('/'))
    checkfolder = deque()
    checkfolder.append(query[-1])
    file = set()
    file_cnt = 0
    while checkfolder:
        check = checkfolder.popleft()
        if File[check]:
            for filename in File[check]:
                file.add(filename)
            file_cnt += len(File[check])
        for folder in Folder[check]:
            checkfolder.append(folder)
    answer.append((len(file), file_cnt))
for i in answer:
    print(*i)
