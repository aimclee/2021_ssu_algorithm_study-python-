import time
start_time = time.time()

n,k=map(int,input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

A.sort()
B=sorted(B,reverse=True)

for i in range(k):
    A[i]=B[i]
print(sum(A))
    

end_time = time.time()
print("time: ", end_time - start_time)