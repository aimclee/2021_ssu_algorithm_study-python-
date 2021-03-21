# 시간복잡도 : O(n^2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[min_idx], array[i] = array[i], array[min_idx]
            
print(array)
