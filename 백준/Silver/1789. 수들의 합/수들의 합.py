N = int(input())
answer = 0

val = 1

while N >= val:
    N -= val
    val += 1
    answer += 1

print(answer)