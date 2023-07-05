import sys
from collections import deque
inp = sys.stdin.readline
n = int(inp())
base = list(map(int,inp().split()))
pos = 0
stack = deque()
ans = 0
s_check = 0
flag = False
def get_reverse(ori_list):
    ori_list.reverse()
    return ori_list
def compare_list(target,control):
    if target == get_reverse(control):
        return True
    else:
        return False
while True:
    if pos == n: break
    if stack and stack[-1] == base[pos]:
        if pos - s_check > n - pos:
            break
        else:
            if compare_list(base[pos:pos + pos - s_check],base[s_check:pos]):
                while stack:
                    stack.pop()
                    pos += 1
            else:
                stack.append(base[pos])
                pos += 1
    else:
        if not stack:
            s_check = pos
        stack.append(base[pos])
        pos += 1
    if not stack:
        ans += 1

if stack:
    print(-1)
else:
    print(ans)

    
