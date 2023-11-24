from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board, start, size, N):
    result = ()
    depth = 1
    visit = set()
    queue = deque([start])
    visit.add(start)

    while not result and queue:
        temp = deque()

        for x, y in queue:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue

                if (nx, ny) not in visit and board[nx][ny] <= size:
                    if board[nx][ny] != 0 and board[nx][ny] < size :
                        if not result or result[0] > nx or (result[0] == nx and result[1] > ny):
                            result = (nx, ny, depth)

                    temp.append((nx, ny))
                    visit.add((nx, ny))

        queue = temp
        depth += 1
    return result

N = int(input())
board = []
start = ()
answer = 0

c_size = 2
eat = 0

for i in range(N):
    row = list(map(int, input().split()))
    if not start:
        for j in range(N):
            if row[j] == 9:
                start = (i, j)
    board.append(row)

while True:
    result = bfs(board, start, c_size, N)

    if result:
        answer += result[2]
        board[start[0]][start[1]] = 0
        board[result[0]][result[1]] = 9
        start = (result[0], result[1])

        eat += 1
        if eat == c_size:
            eat = 0
            c_size += 1
    else:
        break

print(answer)
