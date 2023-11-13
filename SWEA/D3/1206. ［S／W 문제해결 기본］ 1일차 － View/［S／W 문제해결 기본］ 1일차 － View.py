dx = [-1, -2, 1, 2]

for test_case in range(1, 10 + 1):
    result = 0
    N = int(input())
    graph = [[0]*N for _ in range(255)]
    heights = list(map(int, input().split()))

    for idx, h in enumerate(heights):
        for i in range(h):
            graph[254 - i][idx] = 1

    for i in range(255):
        for j in range(2, N-2):
            ok = True
            if graph[i][j] == 0:
                continue

            for n in dx:
                nx = j + n
                if graph[i][nx] == 1:
                    ok = False
                    break

            if ok:
                result += 1

    print(f'#{test_case} {result}')
