output = []
op = []
priority = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

exp = input("Enter the infix expression: ")

for ch in exp:
    if ch == '(':
        op.append(ch)
    elif ch == ')':
        while op[-1] != '(':
            ele = op.pop()
            output.append(ele)
        op.pop()  # Remove '(' from stack
    elif ch in {'+', '-', '*', '/', '^'}:
        if len(op) > 0:
            while op and priority[op[-1]] >= priority[ch]:
                ele = op.pop()
                output.append(ele)
        op.append(ch)
    else:  # Operand
        output.append(ch)

while op:
    ele = op.pop()
    output.append(ele)

print("Infix expression:", exp)
print("Postfix operation:", ''.join(output))
