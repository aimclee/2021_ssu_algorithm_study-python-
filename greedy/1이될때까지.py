import time
start_time = time.time()

n,k = map(int, input().split())

cnt=0
while True:
    if n%k != 0:
        n=n-1
        cnt+=1
        if n==1:
            print(cnt)
            break
    elif n%k == 0:
        n=n/k
        cnt+=1
        if n==1:
            print(cnt)
            break



end_time = time.time()

print("time: ", end_time - start_time)