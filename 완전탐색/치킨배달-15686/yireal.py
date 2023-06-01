from itertools import combinations
import sys
inp = sys.stdin.readline
n,m = map(int,inp().split())
city = [list(map(int,inp().split())) for _ in range(n)]
kfc = []
home = []
ans = n**2 * 13
def set_index():
    for i in range(n):
        for j in range(n):
            if city[i][j] == 0:
                continue
            elif city[i][j] == 1 :
                home.append((j,i))
            else : 
                kfc.append((j,i))   

set_index()
for k in combinations(kfc,m):
    tmp = 0
    for h in home:
        c_range = n**2
        for j in range(m):
            c_range = min(c_range,abs(h[0] - k[j][0]) + abs(h[1] - k[j][1]))
        tmp += c_range
    ans = min(ans,tmp) 
print(ans)