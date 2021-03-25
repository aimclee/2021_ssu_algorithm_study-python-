# binary search

def binary_search(front, back, target, arr):
    mid = (front + back) // 2
    if front > back:
        print("target is not found")
        return 0
    if arr[mid] == target:
        print(mid + 1 + "번째 숫자가 target입니다.")
        return 0
    elif arr[mid] > target:
        binary_search(front, mid - 1, target, arr)
    else:
        binary_search(mid + 1, back, target, arr)


# 원소의 개수 n , target 입력받기
n, target = list(map(int, input().split()))

#전체 원소를 입력받는다
arr = list(map(int, input().split()))
# 오름차순으로 정리한다
arr.sort()
binary_search(0,n-1,target,arr)
