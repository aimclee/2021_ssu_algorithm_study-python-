# 매우매우 간단한 풀이
# m과 k의 값에 연관성에 집중해봄 (수학적인 아이디어)
# 일반적인 풀이는 아니고... 이렇게 풀면 좋지 않을까라고 생각해서 해봤는데 됨

import time
start_time = time.time()

n,m,k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

first=nums[-1]
second=nums[-2]

count=0


count+=k*first*(m//k)
count+=second*(m%k)

print(count)

end_time = time.time()
print("time: ", end_time - start_time)
