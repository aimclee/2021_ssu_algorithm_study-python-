import time
import datetime
start_time = time.time()

# time: 7.939856052398682
# 수열

n,m,k = map(int,input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)) * k
count += m%(k+1)

result=0
result += (count) * first #가장 큰 수 더하기
result += (m-count) * second #두번째로 큰 수 더하기

print(result)

end_time = time.time()
sec = end_time - start_time
times = str(datetime.timedelta(seconds=sec)).split(".")
times = times[0]
print(times)


# print("time: ", end_time - start_time)