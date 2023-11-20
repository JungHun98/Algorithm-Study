def solution(string, boom):
    answer = []
    for char in string:
        answer.append(char)

        if len(answer) >= len(boom) and ''.join(answer[-len(boom):]) == boom:
            for _ in range(len(boom)):
                answer.pop()

    result = ''.join(answer)
    return 'FRULA' if not result else result

string = input()
boom = input()

print(solution(string, boom))
