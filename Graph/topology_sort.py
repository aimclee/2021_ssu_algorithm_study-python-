# 위상정렬
# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
# ex) 선수과목을 고려한 학습 순서 설정
# 시간복잡도 : O(V+E)

from collections import deque

# 노드와 간선의 개수 입력받기
v, e = map(int, input().split())
# 모든 노드에 대해 진입차수 0으로 초기화
indegree = [0] * (v+1)
# 연결정보를 담은 인접리스트
graph = [[] for _ in range(v+1)]

# 방향 그래프의 간선 정보 입력 받기
for _ in range(e):
    start, end = map(int, input().split())
    graph[start].append(end)
    indegree[end] += 1 # end 노드의 진입차수 1 증가
    
# 위상 정렬 함수
def topology_sort():
    result = [] # 결과 담을 리스트
    queue = deque()
    
    # 진입차수가 0인 노드 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            queue.append(i)
            
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나 꺼내기
        now = queue.popleft()
        result.append(now)
        # 꺼낸 노드에서 출발하는 간선 제거하기
        # 즉, 해당 간선이 end 노드로 갖는 노드들의 진입차수 - 1 해주기
        for node in graph[now]:
            indegree[node] -= 1
            # 새롭게 진입차수가 0이 된 노드를 큐에 삽입해주기
            if indegree[node] == 0:
                queue.append(node)
                
    # 위상 정렬 결과 출력
    for i in result:
        print(i, end=' ')
        
topology_sort()
