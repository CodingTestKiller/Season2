import sys


def calc(a, b, o):
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b


def solve(idx, result):
    global max_result

    if idx == len(operators):
        max_result = max(max_result, result)
        return

    solve(idx+1, calc(result, operands[idx+1], operators[idx]))

    if idx+1 != len(operators):
        temp = calc(operands[idx+1], operands[idx+2], operators[idx+1])
        solve(idx+2, calc(result, temp, operators[idx]))


input = sys.stdin.readline

n = int(input())
equation = input().strip()

operands = []
operators = []

max_result = -sys.maxsize

for i in equation:
    try:
        operands.append(int(i))
    except ValueError:
        operators.append(i)

solve(0, operands[0])
print(max_result)
