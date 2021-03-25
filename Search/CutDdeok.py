def cut_ddeok(array, start, end, m):
    result = 0 # 최적화 문제로 임시로 값을 저장해야함
    while start <= end:
        total = 0 # 잘랐을 때 남는 떡의 양
        mid = (start + end) // 2
        
        for i in array:
            if i > mid: # 떡 잘랐을 때 남는 양 계산
                total += i - mid
                
        if total >= m: # 자른 양이 필요한 양보다 많은 경우
            result = mid # 현재가 최적이므로 이 때의 값 저장
            start = mid + 1 # 조금만 자를 수 있도록 start를 뒤로 이동
        else: # 자른 양이 필요한 양보다 적은 경우
            end = mid - 1 # 더 많이 자를 수 있도록 end를 앞으로 이동
            
    return result


# 데이터 입력받기
n, m = map(int, input().split())
array = list(map(int, input().split()))
print(cut_ddeok(array, 0, max(array), m))
