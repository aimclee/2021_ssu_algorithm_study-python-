#곱하기 혹은 더하기 -> 가장 큰 수
arr = list(map(int, input()))
#print(arr)

res = arr[0]
for i in range(1,len(arr)):
    if arr[i] < 2 or res ==0 :
        res += arr[i]
    else:
        res *= arr[i]


print(res)