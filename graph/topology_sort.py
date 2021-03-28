v, e = map(int, input().split())

indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

# 두 개의 노드 간선 연결
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1        # 진입차수 1 증가


def topology_sort():
    res = []        # 결과를 담을 리스트 (BFS 탐색 순서와 유사)
    queue = []

    # 1. 진입차수가 0인 노드를 큐에 append
    for idx in range(1, v + 1):
        if indegree[idx] == 0:
            queue.append(idx)

    # 2. while 큐 is not empty
    while queue:
        cur = queue.pop(0)
        res.append(cur)

        for idx in graph[cur]:
            indegree[idx] -= 1      # 2.1 : cur 노드가 가리키는 next 노드의 진입차수를 1씩 차감
            if indegree[idx] == 0:  # 2.2 : 새롭게 진입차수가 0이 되는 노드를 큐에 append
                queue.append(idx)

        for idx in res:
            print(idx, end = ' ')

topology_sort()
