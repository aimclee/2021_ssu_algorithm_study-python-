n,m=map(int,input().split())

coin=[]
for i in range(n):
    a = int(input())
    coin.append(a)

counts=[]

for j in coin:
    cnt = m/j
    # 나머지==0
    if m%j == 0:
        counts.append(cnt)
if counts==[]:
    counts.append(-1)

count_int=[]
for k in counts:
    count_int.append(int(k))

count_int.sort()

print(count_int[-1])


