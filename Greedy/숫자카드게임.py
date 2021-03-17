# elapsed time : 7.005775451660156

import time

start_time = time.time()

n, m = map(int, input().split())
result = 0

for _ in range(n):
    data = list(map(int, input().split()))
    minValue = min(data)
    result = max(result, minValue)

print(result)

end_time = time.time()

print("elapsed time : ", end_time-start_time)

