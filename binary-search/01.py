# N: 100만, M: 10만
# 전략: 집합 set (시간 복잡도: O(N)) 이용

# 입력값 받기
n = int(input())
n_set = set(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

for num in m_list:
    if num in n_set:
        print("yes", end=' ')
    else:
        print("no", end=' ')
print()
