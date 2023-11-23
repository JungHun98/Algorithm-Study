from collections import deque

answer = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = float('inf')

while True:
    N = int(input())
    if N == 0:
        break

    board = [list(map(int, input().split())) for _ in range(N)]
    memo = [[INF] * N for _ in range(N)]
    memo[0][0] = board[0][0]

    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            cost = memo[x][y] + board[nx][ny]
            if cost < memo[nx][ny]:
                queue.append((nx, ny))
                memo[nx][ny] = cost

    answer.append(memo[-1][-1])

for idx, ans in enumerate(answer):
    print(f'Problem {idx+1}: {ans}')