import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

queue = deque([X])
visit[X] = True
depth = 0

while queue and depth != K:
    temp = deque()
    for ver in queue:
        for v in graph[ver]:
            if not visit[v]:
                temp.append(v)
                visit[v] = True

    queue = temp
    depth += 1

answer = list(queue)
answer.sort()

if answer:
    for ans in answer:
        print(ans)
else:
    print(-1)
