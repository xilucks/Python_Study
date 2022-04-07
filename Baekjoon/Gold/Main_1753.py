import heapq
import sys

N, M = map(int, input().split())

K = int(input())
INF = int(1e9)

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    start, target, value = map(int, input().split())
    graph[start].append([target, value])

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(K)

for i in range(1, N + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])



