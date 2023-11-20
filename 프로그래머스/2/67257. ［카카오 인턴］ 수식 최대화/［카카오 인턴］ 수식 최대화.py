from itertools import permutations

def calc(string, expr):
    stack = []
    number_list = []

    for idx, c in enumerate(string):
        if c.isdigit():
            number_list.append(c)
        else:
            if c == '-':
                if idx == 0 or (string[idx+1].isdigit() and not string[idx-1].isdigit()):
                    number_list.append(c)
                    continue

            num = ''.join(number_list)
            number_list = []

            if stack and stack[-1] == expr:
                stack.pop()
                p_num = stack.pop()
                num = str(eval(''.join([p_num, expr, num])))
            stack.append(num)
            stack.append(c)

    num = ''.join(number_list)

    if stack and stack[-1] == expr:
        stack.pop()
        p_num = stack.pop()
        num = str(eval(''.join([p_num, expr, num])))
    stack.append(num)
    return ''.join(stack)


def solution(expression):
    answer = 0
    expr_set = set()
    for char in expression:
        if char in '-+*':
            expr_set.add(char)

    expr_list = list(permutations(expr_set, len(expr_set)))
    ans_list = []

    for expr in expr_list:
        string = expression

        for e in expr:
            temp = calc(string, e)
            string = temp
        ans_list.append(abs(int(string)))

    answer = max(ans_list)
    return answer