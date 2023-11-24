from collections import deque

move = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

def bfs(start_x, start_y, end_x, end_y):
    if start_x == end_x and start_y == end_y:
        return 0

    result = 0
    visit = set()
    queue = deque([(start_x, start_y)])
    visit.add((start_x, start_y))

    while queue:
        result += 1
        temp = deque()

        for x, y in queue:
            for i in range(8):
                nx, ny = x + move[i][0], y + move[i][1]

                if nx < 0 or ny < 0 or nx >= L or ny >= L:
                    continue

                if (nx, ny) not in visit:
                    if nx == end_x and ny == end_y:
                        return result
                    temp.append((nx, ny))
                    visit.add((nx, ny))

        queue = temp

    return result

T = int(input())
answer = []

for _ in range(T):
    L = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    answer.append(bfs(start_x, start_y, end_x, end_y))

for ans in answer:
    print(ans)
