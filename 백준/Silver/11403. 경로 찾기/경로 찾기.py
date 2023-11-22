from collections import deque

N = int(input())
graph = [[] for _ in range(N)]
answer = [['0']*N for _ in range(N)]

for i in range(N):
    input_list = list(map(int, input().split()))
    for idx, num in enumerate(input_list):
        if num == 1:
            graph[i].append(idx)

for i in range(N):
    for j in range(N):
        queue = deque([i])
        visit = [False] * N

        while queue:
            next_ = queue.popleft()
            for v in graph[next_]:
                if not visit[v]:
                    if v == j:
                        answer[i][j] = '1'
                        queue.clear()
                        break
                    queue.append(v)
                    visit[v] = True


for ans in answer:
    print(' '.join(ans))