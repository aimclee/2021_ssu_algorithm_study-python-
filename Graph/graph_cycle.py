# 그래프에서 서로 루트 노드가 동일하다면 사이클이 발생한 것이다

# find 연산 : 임의의 원소가 속한 집합을 찾기
# 재귀적으로 부모를 거슬러 올라가면서 루트를 찾아주기
def find_set(parent, x):
    # 루트 노드를 찾을 때까지 재귀적으로 호출
    # 루트 노드 조건 : parent[x] == x
    if parent[x] != x:
        parent[x] = find_set(parent, parent[x]) # 바뀐 부분!!
    return parent[x]
  
# union 연산 : 서로 다른 집합을 합치는 연산
# 일반적으로 더 작은 번호를 가진 원소가 부모가 된다
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
parent = [0] * (v+1)  # 부모 테이블

# 부모 테이블 초기화 : 자기자신을 가리키도록
for i in range(1, v+1):
    parent[i] = i
    
# 사이클 발생 여부
cycle = False

for _ in range(e):
    a, b = map(int, input().split())
    
    # 사이클 발생한 경우 : 종료
    if find_set(parent, a) == find_set(parent, b):
        cycle = True
        break
    else:
        union_set(parent, a, b)
        
if cycle == True:
    print("사이클이 발생하였습니다")
else:
    print("사이클이 발생하지 않았습니다")
