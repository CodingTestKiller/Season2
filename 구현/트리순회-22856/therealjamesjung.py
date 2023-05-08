from sys import stdin

n = int(input())

tree = {}

for _ in range(n):
    p, l, r = [int(x) for x in input().split()]
    tree[p] = [l, r]

# print(tree)

current = tree[1][1]
cnt = 0

if current == -1:
    print((n-cnt-1)*2+cnt)
    exit()

while True:
    cnt += 1
    current = tree[current][1]
    if current == -1:
        break

# print(cnt)
print((n-cnt-1)*2+cnt)
