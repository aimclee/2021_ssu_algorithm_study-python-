import sys
import time

# 순차탐색으로 하면 답은 잘 나오지만, 시간초과를 받을 가능성이 있어, 
# 탐색범위가 1000만 이상이라면 이진탐색을 고려하는 것이 좋다.

start_time = time.time()

n, m = map(int, sys.stdin.readline().split())
height_list = list(map(int, input().split()))

h = max(height_list) - 1

ddeok_list = []
for _ in range(max(height_list) - 1):
    for i in height_list:
        var = i-h
        if var>=0:
            ddeok_list.append(var)
        var=0
    
        
    if m <= sum(ddeok_list):
        print(h)
        break
    h-=1
    ddeok_list.clear()

end_time = time.time()
print("time: ", end_time - start_time)