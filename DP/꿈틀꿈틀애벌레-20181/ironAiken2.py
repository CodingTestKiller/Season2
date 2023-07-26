from sys import stdin
input = stdin.readline

n, k =[int(x) for x in input().split()]
feeds = [int(x) for x in input().split()]
satisfactions = [0 for _ in range(n)]

p1, p2 = 0, 0
current = 0
while p2 < n:
    current += feeds[p2]
    satisfactions[p2] = satisfactions[p2 - 1]

    while current >= k:
        satisfactions[p2] = max(satisfactions[p2], satisfactions[p1-1] + current - k)
        current -= feeds[p1]
        p1 += 1
    
    p2 += 1

print(satisfactions[-1])