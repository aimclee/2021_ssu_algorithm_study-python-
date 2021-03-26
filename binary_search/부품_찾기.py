import sys

n=int(sys.stdin.readline().rstrip())
market=list(map(int, input().split()))

m=int(sys.stdin.readline().rstrip())
guest = list(map(int, input().split()))

def binary_search(m,request,start,end):
    mid = (start + end) // 2
    if start > end:
        return 0
    if request == market[mid]:
        return request
    elif request < market[mid]:
        return binary_search(m, request, start, mid-1)
    else:
        return binary_search(m, request, mid+1, end)

result_list=[]
for i in guest:
    result = binary_search(m,i,0,n-1)
    result_list.append(result)

for j in result_list:
    if j == 0:
        print('no', end=' ')
    else:
        print('yes', end=' ')
