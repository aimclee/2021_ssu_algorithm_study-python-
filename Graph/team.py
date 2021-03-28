def find_set(parent, x):
    if parent[x] != x:
        parent[x] = find_set(parent, parent[x])
    return parent[x]

def union_set(parent, x, y):
    x = find_set(parent, x)
    y = find_set(parent, y)
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(0, v+1):
    parent[i] = i
    
for _ in range(e):
    op, a, b = map(int, input().split())
    # 팀 합치기 연산 : union
    if op == 0:
        union_set(parent, a, b)
        
    # 같은 팀 여부 확인 : find
    elif op == 1:
        if find_set(parent, a) == find_set(parent, b):
            print("YES")
        else:
            print("NO")
