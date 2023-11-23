T = int(input())
answer = []

for _ in range(T):
    N = int(input())
    money = list(map(int, input().split()))
    M = int(input())
    dp = [[0] * (M+1) for _ in range(N+1)]

    for i in range(1, N+1):
        temp = money[i-1]
        for j in range(1, M+1):
            if j % temp == 0:
                dp[i][j] += 1
            temp_sum = 0
            idx = j

            while idx > 0:
                temp_sum += dp[i-1][idx]
                idx -= temp
            dp[i][j] += temp_sum

    answer.append(dp[-1][-1])

for ans in answer:
    print(ans)
