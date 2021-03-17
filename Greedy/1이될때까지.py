# 어떤 수 N이 1이 될 때까지 다음의 과정 반복
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
# 나누는게 1씩 빼주는 것보다 숫자 N의 값을 빠르게 줄일 수 있는 방법임을 이용하기
# n%k=나머지 : 나머지만큼 n에서 빼주고(result+=나머지) 그 다음 n을 k로 나눠서 n의 값 줄이기

# elapsed time : 1.6725304126739502

import time

start_time = time.time()

n, k = map(int, input().split())
result = 0

while n>=k:
    if n%k!=0:
        remainder = n%k
        n -= remainder
        result += remainder
    else:
        n//=k
        result += 1

while n!=1:
    n -=1
    result += 1
        
print(result)
end_time = time.time()

print("elapsed time : ", end_time-start_time)

