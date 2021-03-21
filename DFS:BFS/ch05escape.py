from collections import deque


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상,하,좌,
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # 미로영역 벗어나면 종료
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                continue
            if graph[new_x][new_y] == 0:
                continue

            if graph[new_x][new_y] == 1:
                graph[new_x][new_y] = graph[x][y] + 1
                q.append((new_x, new_y))
    return graph[n - 1][m - 1]

print(bfs(0, 0))