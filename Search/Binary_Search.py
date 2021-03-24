# 시간복잡도 : O(logN)
# 전제조건 : 데이터가 정렬되어 있어야 한다
# 탐색 범위가 2000만 넘어가는 경우 이진탐색으로 문제 접근해보기

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
print("입력할 데이터 개수와 찾을 값을 띄어쓰기로 구분하여 입력해주세요")
num, target = map(int, input().split())
print("위에서 입력한 개수만큼 데이터를 입력해주세요")
array = list(map(int, input().split()))

# 이진탐색의 전제 조건 : 정렬된 데이터
# array.sort()

result = binary_search(array, target, 0, num-1)
if result == None:
    print("입력한 데이터가 존재하지 않습니다.")
else:
    print(result, "번째에 위치")
