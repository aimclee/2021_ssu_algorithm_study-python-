# elapsed time :  6.357971906661987

import time

start_time = time.time()

N, M, K = map(int, input().split())
data = list(map(int, input().split()))
tmp = K
sum = 0 

data.sort()
first = data[-1]
second = data[-2]

for i in range(0, M):
    if tmp!=0:
        sum+=first
    else: 
        sum+=second
        tmp=K
    tmp-=1
    
print(sum)

end_time = time.time()

print("elapsed time : ", end_time-start_time)
