import json

def solution(functions, n, array):
    answer = []
    front = 0
    back = n
    state = 'F'

    for func in functions:
        if func == 'R':
            if state == 'F':
                state = 'B'
            else:
                state = 'F'
        else:
            if state == 'F':
                front += 1
            else:
                back -= 1

            if back < front:
                return 'error'

    answer = array[front:back]

    if state == 'B':
        answer.reverse()
    answer = str(answer).replace(' ', '')

    return answer

T = int(input())
result = []
for _ in range(T):
    functions = input()
    N = int(input())
    array = json.loads(input())
    
    result.append(solution(functions, N, array))

for re in result:
    print(re)