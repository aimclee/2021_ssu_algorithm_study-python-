n,m = map(int,input().split())
parent = [0] * (n+1)

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b 

for i in range(0,n+1):
    parent[i] = i


for i in range(m):
    c,a,b=map(int,input().split())
    if c == 0:
        union(parent, a, b)
    elif c == 1:
        if find(parent,a) == find(parent,b):
            print('YES')
        else:
            print('NO')

