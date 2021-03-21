#음료수 얼려 먹
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 얼음틀 영역을 벗어나면 종
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1
        # 상,하,좌,우 들리
        dfs(x, y+1)
        dfs(x, y - 1)
        dfs(x-1 , y)
        dfs(x+1, y )
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
