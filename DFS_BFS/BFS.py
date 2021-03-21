from collections import deque

def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 dequeue 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 떄까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        # 해당 노드의 인접노드 중 아직 방문하지 않은 노드들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
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

bfs(graph, 1, visited)
