def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드의 인접노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
graph = [ # 각 노드끼리 연결 정보가 담긴 인접리스트
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7] 
]
visited = [False]*9 # 각 노드의 방문여부가 저장된 리스트

dfs(graph, 1, visited) # 1번 노드부터 시작
