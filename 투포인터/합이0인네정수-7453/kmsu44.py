import sys
input = sys.stdin.readline
n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]


A = []
B = []
C = []
D = []


for i in range(len(L)):
    for j in range(len(L[i])):
        if j == 0:
            A.append(L[i][j])
        elif j == 1:
            B.append(L[i][j])
        elif j == 2:
            C.append(L[i][j])
        else:
            D.append(L[i][j])


def upperbound(num, Arr: list):
    left_index = 0
    right_index = len(Arr)-1
    while left_index < right_index:
        mid = (left_index + right_index) // 2
        if Arr[mid] < num:
            left_index = mid + 1
        else:
            right_index = mid
    return left_index


def lowerbound(num, Arr: list):
    left_index = 0
    right_index = len(Arr)-1
    while left_index < right_index:
        mid = (left_index + right_index) // 2
        if Arr[mid] < num:
            left_index = mid + 1
        else:
            right_index = mid
    return left_index


# TEST = [1, 1, 5, 5, 5, 6]
# print(lowerbound(7, TEST))
# print(upperbound(7, TEST))


AB = []
for i in A:
    for j in B:
        AB.append(i+j)

AB.sort()
CD = []
for i in C:
    for j in D:
        CD.append(i+j)
CD.sort()

left = 0
right = len(CD)-1
result = 0
while left < len(CD) and 0 <= right:
    if AB[left] + CD[right] == 0:
        next_left = left + 1
        next_right = right - 1
        while next_left < len(AB) and AB[left] == AB[next_left]:
            next_left += 1
        while 0 <= next_right and CD[right] == CD[next_right]:
            next_right -= 1
        result += (right-next_right) * (next_left - left)
        left = next_left
        right = next_right
    elif AB[left] + CD[right] < 0:
        left += 1
    else:
        right -= 1
print(result)
