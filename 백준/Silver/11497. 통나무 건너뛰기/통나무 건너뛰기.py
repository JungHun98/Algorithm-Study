T = int(input())
answer = []

for _ in range(T):
    N = int(input())
    number_list = list(map(int, input().split()))
    number_list.sort()
    temp = [0] * N
    start, end = 0, N - 1

    for i, num in enumerate(number_list):
        if i % 2 == 0:
            temp[start] = num
            start += 1
        else:
            temp[end] = num
            end -= 1

    level = 0
    for i in range(N):
        next_level = abs(temp[(i+1) % N] - temp[i])
        if next_level > level:
            level = next_level

    answer.append(level)

for ans in answer:
    print(ans)