from collections import deque
import copy

v = int(input())
# 연결정보를 담은 인접리스트
graph = [[] for _ in range(v+1)]
# 각 노드들의 진입차수 저장할 리스트
indegree = [0] * (v+1)
# 각 강의 시간 저장할 리스트
time = [0] * (v+1)

# 방향 그래프의 간선 정보 입력 받기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]: # 입력받은 데이터에 선행과목이 있는 경우
        indegree[i] += 1 # end 노드의 진입차수 1 증가
        graph[x].append(i) # x : 선수 과목, i : 다음에 수강할 과목

def topology_sort():
    result = copy.deepcopy(time) # time 리스트를 result 리스트에 복사
    queue = deque()
    
    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            queue.append(i)
            
    while queue:
        # 큐에서 노드 하나 꺼내기
        now = queue.popleft()
        # 해당 노드에서 시작하는 간선 제거
        # 즉, 해당 간선의 end 노드의 진입차수값 -1 해주기
        for node in graph[now]:
            result[node] = max(result[node], result[now]+time[node]) # 소요시간을 더 큰 값으로 업데이트
            indegree[node] -= 1
            # 새롭게 진입차수가 0이된 노드가 있다면 큐에 삽입해주기
            if indegree[node] == 0:
                queue.append(node)
                
        # 위상 정렬 결과 출력
    for i in range(1, v+1):
        print(result[i])
        
topology_sort()
