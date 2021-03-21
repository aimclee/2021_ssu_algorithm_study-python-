import time
start_time = time.time()

n=int(input())

num_list=[]
for i in range(n):
    num_list.append(int(input()))
num_desc_list=sorted(num_list, reverse=True)

for j in range(n):
    print(num_desc_list[j], end=' ')

end_time = time.time()
print("time: ", end_time - start_time)