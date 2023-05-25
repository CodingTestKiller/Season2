# 2시 50분 시작

n = int(input())
L = input()
S = int(L[0])

res = -2**31
if len(L) == 1:
    print(S)
    exit()


def calculator(cal_index, a_index, b_index):
    if L[cal_index] == '+':
        return int(L[a_index]) + int(L[b_index])
    elif L[cal_index] == '-':
        return int(L[a_index]) - int(L[b_index])
    else:
        return int(L[a_index]) * int(L[b_index])


def DFS(S, index):
    global res
    if index >= n:
        res = max(res, S)
        return S
    cal = L[index]
    if cal == '+':
        # 괄호 닫는 경우
        DFS(S + int(L[index+1]), index+2)
        # 다음거에 괄호
        if index+3 < n:
            s = calculator(index+2, index+1, index+3)
            DFS(S+s, index+4)
    if cal == '-':
        # 괄호 닫는 경우
        DFS(S - int(L[index+1]), index+2)
        # 다음거에 괄호
        if index+3 < n:
            s = calculator(index+2, index+1, index+3)
            DFS(S-s, index+4)
    if cal == '*':
        # 괄호 닫는 경우
        DFS(S * int(L[index+1]), index+2)
        # 다음거에 괄호
        if index+3 < n:
            s = calculator(index+2, index+1, index+3)
            DFS(S*s, index+4)


DFS(S, 1)
print(res)
