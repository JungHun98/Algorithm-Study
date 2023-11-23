expr = input()
mul_div = set(['*', '/'])
add_sub = set(['+', '-'])
answer = []
stack = []

def is_pop(a, b):
    if a in mul_div and b in mul_div:
        return True
    elif a in add_sub and b != '(':
        return True
    else:
        return False

for char in expr:
    if char.isalpha():
        answer.append(char)
    else:
        if char == ')':
            while stack[-1] != '(':
                answer.append(stack.pop())
            stack.pop()
        else:
            if stack:
                while stack and is_pop(char, stack[-1]):
                    answer.append(stack.pop())
            stack.append(char)

while stack:
    answer.append(stack.pop())

print(''.join(answer))
