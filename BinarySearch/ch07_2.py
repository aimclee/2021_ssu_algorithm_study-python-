n = int(input())
arr = list(map(int,input().split()))

m = int(input())
target = list(map(int, input().split()))

#이진탐색을위한 정렬
arr.sort()

def binary_search(front, back, target, arr):
    mid = (front + back) // 2
    if front > back:
        #print("no ")
        print("no", end=' ')
        return 0
    if arr[mid] == target:
        print("yes ")
        return 0
    elif arr[mid] > target:
        binary_search(front, mid - 1, target, arr)
    else:
        binary_search(mid + 1, back, target, arr)

for i in target:
    binary_search(0,n-1,i,arr)