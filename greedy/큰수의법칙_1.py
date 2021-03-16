import time
import datetime
start_time = time.time()

n,m,k = map(int,input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m==0:
            break
        result+=first
        m-=1
    if m==0:
        break
    result+=second
    m-=1

print(result)

end_time = time.time()
sec = end_time - start_time
times = str(datetime.timedelta(seconds=sec)).split(".")
times = times[0]
print(times)