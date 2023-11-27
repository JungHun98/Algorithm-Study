import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]
answer = float('inf')

for start in ['W', 'B']:
    result =[[0]*(M+1) for _ in range(N+1)]

    # 보드의 차이 누적합
    for i in range(N):
        for j in range(M):
            if (i + j) % 2 == 0:
                if board[i][j] != start:
                    result[i + 1][j + 1] = 1
            else:
                if board[i][j] == start:
                    result[i + 1][j + 1] = 1
            result[i+1][j+1] = result[i+1][j+1] + result[i][j+1] + result[i+1][j] - result[i][j]

    # KxK 메트릭스에서 가장 작은 차이 구하기
    for i in range(1, N - K + 2):
        for j in range(1, M - K + 2):
            p_sum = result[i+K-1][j+K-1] - result[i+K-1][j-1] - result[i-1][j+K-1] + result[i-1][j-1]
            answer = min(answer, p_sum)

print(answer)
