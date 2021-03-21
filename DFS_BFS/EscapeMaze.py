from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)] # 괴물있는부분 0, 괴물 없는 부분 1

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1] # 상하좌우

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4): # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m: # 범위 벗어난 경우
                continue
            if data[nx][ny]==0: # 괴물 있는 부분
                continue
            if data[nx][ny]==1: # 이동 가능한 경로
                queue.append((nx, ny))
                data[nx][ny] = data[x][y]+1
    return data[n-1][m-1]

print(bfs(0,0))
