import sys
inp = sys.stdin.readline
n = int(inp())
table = []
for i in range(n):
    t1,t2 = map(int,inp().split())
    table.append((t1,t2))
if n == 1:
    print(table[0][0])
    exit()
table.sort(key = lambda x:x[0])
start = table.index(max(table,key = lambda x:x[1]))
def calc_dis(base):
    val = 0
    for pos in table:
        val += abs(base - pos[0]) * pos[1]
    return val
pos = table[start][0]
while True:
    min_val = calc_dis(pos)
    if pos - 1 > table[0][0]:
        if calc_dis(pos-1) < min_val:
            pos -= 1
            continue
    elif pos + 1 < table[-1][0]: 
        if calc_dis(pos+1) < min_val:
            pos += 1
            continue
    break 
print(pos)