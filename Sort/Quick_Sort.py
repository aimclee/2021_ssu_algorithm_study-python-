# 시간 복잡도
# 최선의 경우 : 피복에 의해 원소들이 왼쪽과 오른쪽 부분집합으로 정확히 n/2씩 이등분 되는 경우,
# 최악의 경우 : 피봇에 의해 원소들을 분할 하였을 때 1개와 n-1개로 한쪽으로 치우쳐 분할되는 경우 O(n^2),
# 평균시간 복잡도 : O(nlogn)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end): # start : 리스트의 첫번째(위치 고정), end : 리스트의 마지막(위치 고정), left/right : 위치 이동
    if start>=end: # 원소가 1개인 경우 종료 : 재귀함수 종료 조건
        return
    
    pivot = start # pivot : 배열의 첫번째 원소 인덱스
    left = start+1
    right = end
    
    while left<=right: # 크로스가 안 된 동안
        # pivot 값보다 큰 값 찾을 동안 left를 오른쪽으로 이동
        while left <= end and array[left] <= array[pivot]: # left가 pivot 보다 작으면 left 값을 증가시켜 이동(크면 반복문 종료)
            left += 1
        # pivot 값보다 작은 값을 찾을 동안 right를 왼쪽으로 이동
        while right > start and array[right] >= array[pivot]: # right가 pivot 보다 크면 right 값을 감소시켜 이동(작으면 반복문 종료)
            right -= 1
            
        # right와 left가 크로스되었으면(엇갈렸으면) right자리에 있던 것과 pivot자리 원소랑 swap
        if right < left:
            array[right], array[pivot] = array[pivot], array[right]
        # right와 left가 크로스되지 않았다면 left 자리에 있던 것과 right 자리에 있던것 swap
        else :
            array[left], array[right] = array[right], array[left]
            
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행    
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
        
quick_sort(array, 0, len(array)-1)
print(array)
