import heapq

INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, cur = heapq.heappop(queue)
        if distance[cur] < dist:
            continue

        for next_node in graph[cur]:
            cost = dist + next_node[1]

            if cost < distance[next_node[0]]:
                distance[next_node[0]] = cost
                heapq.heappush(queue, (cost, next_node[0]))


dijkstra(start)

res = 0
max_distance = 0
for dis in distance:
    if dis != INF:
        res += 1
        max_distance = max(max_distance, dis)

print(res - 1, max_distance)
