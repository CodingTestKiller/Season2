from itertools import combinations
n, k = map(int, input().split())
words = []
for i in range(n):
    tmp = input()
    tmp = tmp[4:len(tmp)-4]
    words.append(tmp)

T = set(['a', 'n', 't', 'c', 'i'])
alphabet = set()
k -= 5
for word in words:
    for j in word:
        if j in T:
            continue
        alphabet.add(j)
if k < 0:
    print(0)
else:
    res = 0
    L = list(combinations(alphabet, k))
    for case in L:
        cnt = 0
        for word in words:
            flag = True
            for i in word:
                if i in case or i in T:
                    continue
                else:
                    flag = False
                    break
            if flag:
                cnt += 1
        res = max(res, cnt)
    print(res)
