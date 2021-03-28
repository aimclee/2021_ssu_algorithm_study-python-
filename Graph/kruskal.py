# Kruskal's algorithm

# find 연산 : 임의의 원소가 속한 집합을 찾기
# 재귀적으로 부모를 거슬러 올라가면서 루트를 찾아주기
def find_set(parent, x):
    # 루트 노드를 찾을 때까지 재귀적으로 호출
    # 루트 노드 조건 : parent[x] == x
    if parent[x] != x:
        parent[x] = find_set(parent, parent[x])
    return parent[x]

def union_set(parent, x, y):
    # 두 집합의 루트가 다른 경우 합쳐준다
    x = find_set(parent, x)
    y = find_set(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
        
# 노드의 개수와 간선의 개수(union 연산 횟수) 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블

# 부모 테이블 초기화 : 자기자신을 가리키도록
for i in range(1, v+1):
    parent[i] = i
    
# 모든 간선 정보 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 정점들 간의 연결 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # edges 리스트에 append : 추후에 cost 기준으로 오름차순 정렬
    edges.append((cost, a, b))
    
# cost(가중치) 기준으로 오름차순 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 서로 다른 집합에 속하는 경우 연결 : 사이클 생성 (X) 조건에 해당
    if find_set(parent, a) != find_set(parent, b):
        union_set(parent, a, b)
        result += cost # 최종 비용 업데이트
    
print(result)
