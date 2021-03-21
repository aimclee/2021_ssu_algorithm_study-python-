n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)] # 구멍 뚫린 부분 0, 아닌 부분 1
result = 0 # 아이스크림의 개수

def dfs(x, y):
    # 재귀함수 종료 조건
    if x<0 or x>=n or y<0 or y>=m: # 얼음틀 범위를 벗어나는 경우
        return False
    
    if data[x][y] == 0 : # 아직 방문하지 않은 상태
        data[x][y] = 1 # 방문처리
        # 해당 노드의 상하좌우 노드 방문하기
        # 리턴값 사용 X, 상하좌우 노드 방문 목적
        dfs(x-1, y) # 상
        dfs(x+1, y) # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True: # dfs : 이미 방문했거나 범위 벗어난 경우 False 리턴
            result += 1       # 노드(i, j)를 처음 방문하는 경우 true 리턴
            
print(result)
