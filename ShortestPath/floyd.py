# Floyd 알고리즘
# 모든 쌍 최단 경로 알고리즘 : 모든 지점에서 다른 지점까지의 최단 경로를 모두 구해야 하는 경우
# D[i][j] = min{D[i][j], D[i][k]+D[k][j]}
# 즉, min(i에서 j로 바로 가는 것, i에서 k를 거쳐 j로 가는 것)
# 시간복잡도 : O(n^3)

INF = int(1e9)

# 노드, 간선의 개수 입력받기
v = int(input())
e = int(input())

# 인접 행렬 선언 및 모두 무한대로 초기화
graph = [[INF] * (v+1) for _ in range(v+1)]

# 주대각성분 = 0 초기화 : 자기자신으로 가는 경로의 길이 = 0
for i in range(1, v+1):
    graph[i][i] = 0
    
# 간선의 정보 입력받아 인접행렬 초기화
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
# Floyd 알고리즘 수행
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
                
# 수행 결과 출력
for i in range(1, v+1):
    for j in range(1, v+1):
        # 경로가 없는 경우 INF 출력
        if graph[i][j] == INF:
            print("INF", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
