def reverse(s):
    str = "" 
    for i in s:
        str = i + str 
    return str 

output = []
op = []
priority = {
    ')': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

exp1 = input("Enter the infix expression: ")
exp = reverse(exp1)

for ch in exp:
    if ch == ')':
        op.append(ch)
    elif ch == '(':
        while op[-1] != ')':
            ele = op.pop() 
            output.append(ele) 
        op.pop()  # Remove ')' from stack
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

prefix = reverse(output) 

print("Infix expression:", exp1)
print("Prefix operation:", prefix)
