from collections import deque

# best practice : http://pythontutor.com/visualize.html#code=from%20collections%20import%20deque%0A%0A%23%20N,%20M%EC%9D%84%20%EA%B3%B5%EB%B0%B1%EC%9D%84%20%EA%B8%B0%EC%A4%80%EC%9C%BC%EB%A1%9C%20%EA%B5%AC%EB%B6%84%ED%95%98%EC%97%AC%20%EC%9E%85%EB%A0%A5%20%EB%B0%9B%EA%B8%B0%0An,%20m%20%3D%20map%28int,%20input%28%29.split%28%29%29%0A%23%202%EC%B0%A8%EC%9B%90%20%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98%20%EB%A7%B5%20%EC%A0%95%EB%B3%B4%20%EC%9E%85%EB%A0%A5%20%EB%B0%9B%EA%B8%B0%0Agraph%20%3D%20%5B%5D%0Afor%20i%20in%20range%28n%29%3A%0A%20%20%20%20graph.append%28list%28map%28int,%20input%28%29%29%29%29%0A%0A%23%20%EC%9D%B4%EB%8F%99%ED%95%A0%20%EB%84%A4%20%EA%B0%80%EC%A7%80%20%EB%B0%A9%ED%96%A5%20%EC%A0%95%EC%9D%98%20%28%EC%83%81,%20%ED%95%98,%20%EC%A2%8C,%20%EC%9A%B0%29%0Adx%20%3D%20%5B-1,%201,%200,%200%5D%0Ady%20%3D%20%5B0,%200,%20-1,%201%5D%0A%0A%23%20BFS%20%EC%86%8C%EC%8A%A4%EC%BD%94%EB%93%9C%20%EA%B5%AC%ED%98%84%0Adef%20bfs%28x,%20y%29%3A%0A%20%20%20%20%23%20%ED%81%90%28Queue%29%20%EA%B5%AC%ED%98%84%EC%9D%84%20%EC%9C%84%ED%95%B4%20deque%20%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%20%EC%82%AC%EC%9A%A9%0A%20%20%20%20queue%20%3D%20deque%28%29%0A%20%20%20%20queue.append%28%28x,%20y%29%29%0A%20%20%20%20%23%20%ED%81%90%EA%B0%80%20%EB%B9%8C%20%EB%95%8C%EA%B9%8C%EC%A7%80%20%EB%B0%98%EB%B3%B5%ED%95%98%EA%B8%B0%0A%20%20%20%20while%20queue%3A%0A%20%20%20%20%20%20%20%20x,%20y%20%3D%20queue.popleft%28%29%0A%20%20%20%20%20%20%20%20%23%20%ED%98%84%EC%9E%AC%20%EC%9C%84%EC%B9%98%EC%97%90%EC%84%9C%204%EA%B0%80%EC%A7%80%20%EB%B0%A9%ED%96%A5%EC%9C%BC%EB%A1%9C%EC%9D%98%20%EC%9C%84%EC%B9%98%20%ED%99%95%EC%9D%B8%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%284%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nx%20%3D%20x%20%2B%20dx%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20ny%20%3D%20y%20%2B%20dy%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%EB%AF%B8%EB%A1%9C%20%EC%B0%BE%EA%B8%B0%20%EA%B3%B5%EA%B0%84%EC%9D%84%20%EB%B2%97%EC%96%B4%EB%82%9C%20%EA%B2%BD%EC%9A%B0%20%EB%AC%B4%EC%8B%9C%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20nx%20%3C%200%20or%20nx%20%3E%3D%20n%20or%20ny%20%3C%200%20or%20ny%20%3E%3D%20m%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20continue%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%EB%B2%BD%EC%9D%B8%20%EA%B2%BD%EC%9A%B0%20%EB%AC%B4%EC%8B%9C%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20graph%5Bnx%5D%5Bny%5D%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20continue%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%ED%95%B4%EB%8B%B9%20%EB%85%B8%EB%93%9C%EB%A5%BC%20%EC%B2%98%EC%9D%8C%20%EB%B0%A9%EB%AC%B8%ED%95%98%EB%8A%94%20%EA%B2%BD%EC%9A%B0%EC%97%90%EB%A7%8C%20%EC%B5%9C%EB%8B%A8%20%EA%B1%B0%EB%A6%AC%20%EA%B8%B0%EB%A1%9D%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20graph%5Bnx%5D%5Bny%5D%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20graph%5Bnx%5D%5Bny%5D%20%3D%20graph%5Bx%5D%5By%5D%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20queue.append%28%28nx,%20ny%29%29%0A%20%20%20%20%23%20%EA%B0%80%EC%9E%A5%20%EC%98%A4%EB%A5%B8%EC%AA%BD%20%EC%95%84%EB%9E%98%EA%B9%8C%EC%A7%80%EC%9D%98%20%EC%B5%9C%EB%8B%A8%20%EA%B1%B0%EB%A6%AC%20%EB%B0%98%ED%99%98%0A%20%20%20%20return%20graph%5Bn%20-%201%5D%5Bm%20-%201%5D%0A%0A%23%20BFS%EB%A5%BC%20%EC%88%98%ED%96%89%ED%95%9C%20%EA%B2%B0%EA%B3%BC%20%EC%B6%9C%EB%A0%A5%0Aprint%28bfs%280,%200%29%29&cumulative=false&curInstr=12&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%223%204%22,%221111%22,%221101%22,%220111%22%5D&textReferences=false

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))