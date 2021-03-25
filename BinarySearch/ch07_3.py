#떡자르기
n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

front = 0
back = max(array)
#answer
ans = 0

#binary search
while(front <= back):
    total = 0
    mid = (front + back) // 2
    for x in array:
        #절단 후 남은 떡볶이를 total에 저장
        if x > mid:
            total += x - mid
    #떡볶이양이 부족할 경우 절단기크기 줄이
    if total < m:
        back = mid - 1
    else:
        ans = mid
        front = mid + 1


print(ans)