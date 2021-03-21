import time

# elapsed time : 0.000997781753540039

n, k = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

start_time = time.time()

arr_a = sorted(arr_a) # 오름차순 정렬
arr_b = sorted(arr_b, reverse=True) # 내림차순 정렬

# 같은 인덱스에 있는 것끼리 swap
for i in range(k): # 최대 k번 바꿔치기 연산 가능
    if arr_a[i] < arr_b[i]: # b에 있는 원소 값이 크면 swap
        arr_a[i], arr_b[i] = arr_b[i], arr_a[i]
    else: # 더 이상 바꿀 것이 없으면(a에 큰 것들로만 있는 경우) 반복문 탈출
        break
        
print(sum(arr_a))

end_time = time.time()
print("elapsed time : ", end_time-start_time)
