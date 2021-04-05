#문자열 뒤집기
arr = list(map(int,input()))
ans = []
a =0
b = 0

def count(a,arr):
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            a += 1
    ans.append(a//2)

def reverse(arr):
    for i in range(len(arr)):
        if arr[i] ==1:
            arr[i] =0
        else:
            arr[i] =1

count(a,arr)
reverse(arr)
count(b,arr)
ans.sort()
#print(ans)
print(ans[0])
