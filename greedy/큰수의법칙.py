import time

start_time = time.time()

#sol1 -> time: 6.945800542831421

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

print("time: ", end_time - start_time)  