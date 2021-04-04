n,m = map(int, input().split())
k = list(map(int, input().split()))

cnt=0
for i in k:
    for j in k:
        if i != j:
            cnt+=1
print(cnt//2)