# 다익스트라 알고리즘
# 하나의 정점에서 다른 모든 정점까지의 최단 경로 구해주는 알고리즘
# distance[w] = min( distance[w], distance[u] + graph[u, w] )
# 죽,  min(w로 직접가는 경로, 다른 노드를 경유해서 w로 가는 경로)

import sys
input = sys.stdin.realine

INF = int(1e9)

# 노드, 간선의 개수 입력받기
v, e = map(int, input().split())
# 시작 노드 입력받기
start = int(input())
# 그래프의 인접 리스트
graph = [[] for _ in range(v + 1)]
# 방문 여부 저장
visited = [False] * (v + 1)
# 최단 경로 길이 저장
distance = [INF] * (v + 1)

# 간선 정보(가중치) 입력 받기
# 정점 번호와 인덱스 일치 시키기 위해 따로 입력받음
for _ in range(e):
    # a에서 b까지 간선의 가중치 : c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
# 방문하지 않은 노드 중 가장 경로의 길이가 짧은 정점의 인덱스 리턴
def get_shortest_node():
    min_value = INF
    index = 0 # 경로 길이가 가장 짧은 노드의 인덱스
    
    for i in range(1, v+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    
    return index

# 다익스트라 알고리즘
def dijkstra(start):
    print("Path > ", end=' ')
    print(start, end=' ') # 경로 출력을 위한 코드
    # 시작 노드에 대한 초기화
    distance[start] = 0
    visited[start] = True
    for node in graph[start]:
        # 시작 노드의 인접 노드 정보를 이용하여 distance 초기화
        distance[node[0]] = node[1]
        
    # 시작 노드를 제외한 나머지 노드들의 경로 결정
    for i in range(v-1):
        # 현재 가장 가까운 정점의 번호를 now에 저장
        now = get_shortest_node()
        # now 방문 처리
        visited[now] = True
        print(now, end=' ') # 경로 출력을 위한 코드
        
        # now를 기준으로 distance 정보 업데이트
        for node in graph[now]:
            distance[node[0]] = min(distance[now]+node[1], distance[node[0]])
        
# 다익스트라 알고리즘 수행
dijkstra(start)
print()

# 최단 거리 출력
for i in range(1, v+1):
    # 도달할 수 없는 경우 INF 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
