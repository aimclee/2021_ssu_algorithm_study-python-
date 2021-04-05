#공포도 X->X명 이상으로 그룹 만들기
# 최대그룹수

n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=True)

cnt = 1
i= arr[0]
res = n-i
while i < n :
    if arr[i] == 1:
        cnt += res
        break
    res -= arr[i]
    if res < 0:
        break
    i += arr[i]
    cnt += 1

print(cnt)
print(arr)