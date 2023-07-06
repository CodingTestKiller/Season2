import sys
inp = sys.stdin.readline
n,k = map(int,inp().split())
int_list = list(inp().rstrip())
ans = []
for num in int_list:
    while ans and ans[-1] < num and k > 0:
        ans.pop()
        k -= 1
    ans.append(num)
if k == 0: print(*ans,sep='')
else:
    print(*ans[:-k],sep='')