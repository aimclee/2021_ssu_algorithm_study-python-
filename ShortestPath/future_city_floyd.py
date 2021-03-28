INF = int(1e9)

# 노드, 간선의 개수 입력받기
v, e = map(int, input().split())

# 인접 행렬 선언 및 모두 무한대로 초기화
graph = [[INF] * (v+1) for _ in range(v+1)]

# 주대각성분 = 0 초기화 : 자기자신으로 가는 경로의 길이 = 0
for i in range(1, v+1):
    graph[i][i] = 0
    
# 간선의 정보 입력받아 인접행렬 초기화
for _ in range(e):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
x, k = map(int, input().split()) # x : 도착지, k : 경유지

# Floyd 알고리즘 수행
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# # 1번 ~ k번 ~ x번 최단 경로의 길이 계산
distance = graph[1][k] + graph[k][x] 

# 수행 결과 출력
# 경로가 없는 경우
if distance >= INF:
    print("-1")
else:
    print(distance)
