from collections import deque
import time

start_time = time.time()


# n X m
n,m = map(int, input().split())
start = 0
queue = deque([start])

# 미로의 정보 입력받기
maze_list=[]
for i in range(n):
    maze_list.append(list(map(int, input())))
print(maze_list)


cnt=0
def bfs(start,x,y):
    if x<=-1 or y <= -1 or x>=n or y >=m:
        return 1

bfs()


end_time = time.time()
print("time: ", end_time - start_time)