import copy

v = int(input())
indegree = [0] * (v + 1)

graph = [[] for _ in range(v + 1)]
time = [0] * (v + 1)

for idx in range(1, v + 1):
    data = list(map(int, input().split()))
    time[idx] = data[0]
    for x in data[1:-1]:
        indegree[x] += 1
        graph[x].append(idx)

def topology_sort():
    res = copy.deepcopy(time)
    queue = []

    for idx in range(1, v + 1):
        if indegree[idx] == 0:
            queue.append(idx)

    while queue:
        cur = queue.pop(0)

        for idx in graph[cur]:
            res[idx] = max(res[idx], res[cur] + time[idx])
            indegree[idx] -= 1

            if indegree[idx] == 0:
                queue.append(idx)

    for idx in range(1, v + 1):
        print(res[idx])


topology_sort()
