# 시간복잡도 : O(n+k) - 정렬할 원소의 개수 n, 데이터 중 최대값의 크기 k
# 공간복잡도 : O(n+k) - 정렬할 원소의 개수 n, 데이터 중 최대값의 크기 k


# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 원소의 범위를 포함하는 리스트, 0으로 초기화
count = [0] * (max(array)+1)

for i in array:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
