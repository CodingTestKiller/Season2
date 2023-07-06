import sys
inp = sys.stdin.readline
n,k = map(int,inp().split())
learn = ['a','n','t','i','c']
word = [list(inp().rstrip()) for _ in range(n)]
if k < 5:
    print(0)
    exit()
elif k >= 26:
    print(n)
    exit()
ans = 0
learn = [0] * 26
for c in ('a','c','i','n','t'):
    learn[ord(c) - ord ('a')] = 1
def dfs(index,cnt):
    global ans
    if cnt == k - 5 :
        readcnt = 0
        for wo in word:
            check = True
            for w in wo:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt += 1
        ans = max(ans,readcnt)
        return
    for i in range(index,26):
        if not learn[i]:
            learn[i] = True
            dfs(i,cnt + 1)
            learn[i] = False
dfs(0,0)
print(ans)
