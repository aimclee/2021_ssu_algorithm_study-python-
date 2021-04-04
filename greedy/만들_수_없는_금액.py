import itertools
n=int(input()) # 5
units = list(map(int, input().split()))

units.sort(reverse=True) # 9 3 2 1 1

values_list=[]
for i in range(1, len(units)):
    # 조합
    for x in itertools.combinations(units,i):
        values_list.append(sum(list(x)))

# 리스트 중복제거
values_list = list(set(values_list))

# 최솟값 골라내기
temp = 1
for j in values_list:
    if j == temp:
        temp+=1
    else:
        print(temp)
        break