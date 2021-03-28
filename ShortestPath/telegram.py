import sys
import heapq

input = sys.stdin.realine
INF = int(1e9)

# 노드, 간선의 개수, 시작 노드 입력받기
v, e, start = map(int, input().split())
# 그래프의 인접 리스트
graph = [[] for _ in range(v + 1)]
# 최단 경로 길이 저장
distance = [INF] * (v + 1)

# 간선 정보(가중치) 입력 받기
# 정점 번호와 인덱스 일치 시키기 위해 따로 입력받음
for _ in range(e):
    # a에서 b까지 간선의 가중치 : c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라 알고리즘
def dijkstra(start):
#    print("Path > ", end=' ')
    queue = []
    
    # 시작 노드에 대한 초기화
    heapq.heappush(queue, (0, start)) # (가중치, 노드번호)
    distance[start] = 0
    
    while queue: # queue가 비어있지 않은 동안
        # 우선순위 큐에서 하나 pop : 지금 가중치가 제일 작은 노드
        dist, now = heapq.heappop(queue)
        # 현재 노드가 방문한 적이 있는 노드라면 무시
        if dist > distance[now]:
            continue

        print(now, end=' ') # 경로 출력을 위한 코드

        # 방문학 적이 없는 노드라면 그 노드의 인접 노드에 대해 distance 업데이트
        for node in graph[now]:
            cost = dist + node[1] # 현재 노드까지의 최단 경로 + 인접노드로 가는 경로의 가중치
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(queue, (cost, node[0])) # now 노드를 경유하는게 더 가까운 경우로 업데이트

# 다익스트라 알고리즘 수행
dijkstra(start)
count = 0 
max_dist = 0

# 결과 출력
for data in distance:
    if data != INF:
        count+=1
        max_dist = max(data, max_dist)
        
print(count-1, max_dist) # 시작노드 제외(-1)
