# 여러번 입력하며 자연스레 익히기!

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        # 중간점의 값과 찾고자 하는 값이 같은 경우 중간점 인덱스 반환
        if array[mid] == target : 
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid-1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None


# n(원소의 개수)과 target(찾고자하는 문자열)을 입력받기 
n, target = list(map(int, input().split()))

# 전체 원소 입력받기
array = list(map(int,input().split()))

# 이진탐색 수행결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않음")
else:
    print(result+1)