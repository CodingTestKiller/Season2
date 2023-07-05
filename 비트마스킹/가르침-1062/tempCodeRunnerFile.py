import sys
inp = sys.stdin.readline
n,k = map(int,inp().split())
learn = ['a','n','t','i','c']
k -= 5
word = [list(inp().rstrip()) for _ in range(n)]
if k < 0:
    print(0)
    exit()
def update_word():
    for i in range(n):
        for w in word[i]:
            if w not in learn:
                unknown[i] += 1
ans = 0
def learn_new(index):
    global k
    for w in word[index]:
        if k <= 0 : return
        if w not in learn:
            k -= 1
            learn.append(w)
    
while True:
    if len(word) == 0 :
        break
    unknown = [0] * n
    update_word()
    mindex = unknown.index(min(unknown))
    if unknown[mindex] > k:
        break
    if unknown[mindex] == 0:
        ans += 1
        unknown.pop(mindex)
        word.pop(mindex)
        n -= 1
        continue
    if k <= 0:
        break
    learn_new(mindex)

print(ans)
    
    



