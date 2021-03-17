import time
start_time = time.time()

n = int(input())

cnt=0
for i in range(0,n+1):
	for j in range(0,60):
			for k in range(0,60):
				if '3' in str(i)+str(j)+str(k):
					cnt+=1
                
					
print(cnt)


end_time = time.time()
print("time: ", end_time - start_time)