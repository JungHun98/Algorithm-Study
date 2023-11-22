N = int(input())
number_list = list(map(int, input().split()))

dp = [0] * 1001
num_set = set()

for number in number_list:
    max_ = []
    for num in num_set:
        if num < number:
            max_.append(dp[num])

    if max_:
        dp[number] = max(max_) + 1
    else:
        dp[number] = 1

    num_set.add(number)

print(max(dp))