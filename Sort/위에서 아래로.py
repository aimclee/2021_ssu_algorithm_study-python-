import time

# elapsed time : 2.9861197471618652

num = int(input())
data = []

start_time = time.time()

for _ in range(num):
    data.append(int(input()))

data = sorted(data, reverse=True)

for i in data:
    print(i, end=' ')
    
print()
end_time = time.time()
print("elapsed time : ", end_time-start_time)
