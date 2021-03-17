# elapsed time : 15.06650161743164

import time

start_time = time.time()

# 데이터 입력 받기
n, m = map(int, input().split())
a, b, d = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(n)] # 0 : 육지, 1 : 바다

map_data[a][b] = 1 # 현재 위치 방문 처리

# (북, 동, 남, 서) 방향으로 이동 : 0~3 인덱스 순서 이용하기 위해
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
result = 1 # 방문 노드 개수
turn_time = 0 # 회전 횟수 : 4인 경우 사방에 갈 곳이 없다는 의미

while True:
    d = (d + 3) % 4 # 90도 반시계 회전 (왼쪽으로 회전)
    nx = a + dx[d] # next_x
    ny = b + dy[d] # next_y
    
    if map_data[nx][ny]==0: # 왼쪽에 안 가본 곳이 있는 경우, 방문하기
        map_data[nx][ny] = 1
        # 현재 위치 업데이트
        a = nx 
        b = ny
        turn_time = 0
        result += 1
        continue
    else: # 왼쪽이 이미 방문했거나 바다인 경우
        turn_time += 1
        
    if turn_time == 4: # 사방이 막힌 경우(이미 방문했거나 바다인 경우)
        # 왼쪽으로 전진하기 전 위치
        nx = a - dx[d]
        ny = b - dy[d]
        
        if map_data[nx][ny]==0: # 후진할 수 있는 경우
            # 현재 위치 업데이트
            a = nx
            b = ny
        else :
            break
            
        turn_time = 0

print(result)
end_time = time.time()

print("elapsed time : ", end_time-start_time)
