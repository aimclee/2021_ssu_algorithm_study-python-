
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2 # mid = int((start + end) / 2) 와 같은 효과
        
        if array[mid] == target : # 찾는 원소를 찾은 경우
            return mid+1 # 그 원소의 인덱스 리턴
        elif array[mid] > target : # 찾는 원소가 start~mid 사이에 있는 경우
            end = mid - 1
        elif array[mid] < target : # 찾는 원소가 mid~end 사이에 있는 경우
            start = mid + 1
            
    return None # 찾는 값이 배열에 없는 경우

# 데이터 입력받기
n = int(input()) # array 크기
array = list(map(int, input().split()))
m = int(input()) # target 크기
target = list(map(int, input().split()))

array.sort() # array 정렬

for i in target:
    result = binary_search(array, i, 0, n-1)
    if result == None: # 해당 부품이 없는 경우
        print('no', end=' ')
    else:
        print('yes', end=' ')
