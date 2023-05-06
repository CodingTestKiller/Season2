#풀이 실패... 솔루션 참고

import sys
inp = sys.stdin.readline

def convert(origin_list):
    new_list = [[0 for _ in range(n-m+1)] for _ in range(n-m+1)]
    for i in range(n-m+1):
        for j in range(n-m+1):
            new_list[i][j] = -origin_list[i][j]
    return new_list

n,m = map(int,inp().split())
table = [list(map(int,input().split())) for _ in range(n)]
table = convert(table)
sum_table = [[0 for _ in range(n+1)] for _ in range(n+1)]
ans = [[0 for _ in range(n-m+1)] for _ in range(n-m+1)]

for i in range(n-m+1):
    for j in range(n-m+1):
        ans[i][j] = table[i][j] - sum_table[i][j] + sum_table[i+m][j] + sum_table[i][j+m] - sum_table[i+m-1][j+m] - sum_table[i+m][j+m-1] + sum_table[i+m-1][j+m-1]
        sum_table[i+m][j+m] = sum_table[i+m-1][j+m] + sum_table[i+m][j+m-1] - sum_table[i+m-1][j+m-1] + ans[i][j]

for i in range(m//2):
    print("0 "*n)
for i in range(n-m+1):
    print("0 "*(m//2) + " ".join(map(str,ans[i]))+ " 0"*(m//2)) 
for i in range(m//2):
    print("0 "*n)