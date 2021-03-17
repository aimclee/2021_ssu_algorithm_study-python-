# elapsed time : 1.6338634490966797

import time

start_time = time.time()

n, k = map(int, input().split())
result = 0

while True:
    # n이 k의 배수가 될 때까지 한번에 빼주기
    target = (n // k) * k
    result += n-target
    n = target

    if n<k: # 나눌 수 없는 경우
        break
        
    # n이 k배수이므로 k로 나누어주기
    n//=k
    result+=1
    
# n<k인 경우, (n-1)은 n이 1이 되기 위해 수행해야할 -1 계산 횟수
result += (n-1)

print(result)
end_time = time.time()

print("elapsed time : ", end_time-start_time)
