string = input()
answer = 0
stick = 0

for i in range(1, len(string)):
    if string[i] == '(':
        if string[i-1] == '(':
            stick += 1
    else:
        if string[i-1] == '(':
            answer += stick
        else:
            answer += 1
            stick -= 1

print(answer)