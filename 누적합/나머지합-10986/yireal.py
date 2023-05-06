import sys
inp = sys.stdin.readline
n,m = map(int,inp().split())
table = list(map(int,inp().split()))
sum_table = [0]*(n+1)
sum_table[0] = 0
for i in range(1,n+1):
    sum_table[i] = (table[i-1] + sum_table[i-1]) % m
remainders = [0] * m
cnt = 0
for i in range(n + 1):
    cnt += remainders[sum_table[i]]
    remainders[sum_table[i]] += 1

print(cnt)
