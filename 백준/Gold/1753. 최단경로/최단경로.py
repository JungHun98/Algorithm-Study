import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = float('inf')

graph =[[] for _ in range(V+1)]
visit = set()
dist = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

queue = [(0, K)]
heapq.heapify(queue)
dist[K] = 0

while queue:
    cur_w, cur_v = heapq.heappop(queue)
    cur_dist = dist[cur_v]

    if cur_dist < cur_w:
        continue

    for v, w in graph[cur_v]:
        next_dist = w + cur_w
        if next_dist < dist[v]:
            dist[v] = next_dist
            heapq.heappush(queue, (next_dist, v))

for i in range(1, V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
