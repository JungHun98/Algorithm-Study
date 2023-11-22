S = input()

answer = [0, 0]

prev = S[0]

for i in range(1, len(S)):
    if prev != S[i]:
        answer[int(prev)] += 1

    prev = S[i]

answer[int(prev)] += 1

print(min(answer))