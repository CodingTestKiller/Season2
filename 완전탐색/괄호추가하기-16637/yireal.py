import sys
inp = sys.stdin.readline
n = int(inp())
ans = 0
exp = list(inp().rstrip())
def calc(p_exp):
    if p_exp:
        num = int(p_exp[0])
        for i in range(2,len(p_exp),2):
            if p_exp[i-1] == '+':
                num += int(p_exp[i])
            elif p_exp[i-1] == '-':
                num -= int(p_exp[i])
            elif p_exp[i-1] == '*':
                num *= int(p_exp[i])
        return num
    else:
        return 0
def combine(n_exp):
    l_index = 0
    max_val = calc(n_exp)
    flag = 0
    for i in range(1,len(n_exp)-1,2):
        if i+2 == len(n_exp):
            
        