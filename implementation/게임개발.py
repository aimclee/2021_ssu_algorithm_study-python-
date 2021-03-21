import time
start_time = time.time()

n,m = map(int,input().split())
a,b,d = map(int, input().split())

direction_list = [0,1,2,3]
dx = [-1,1]
dy = [-1,1]

graph=[]
for _ in range(n):
    for _ in range(m):
        graph.append(list(map(int, input().split())))




end_time = time.time()
print("time: ", end_time - start_time)
