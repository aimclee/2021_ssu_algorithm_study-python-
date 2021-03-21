# 전략: 배열 A의 최솟값과 배열 B의 최댓값을 바꾸기 (K번 반복)
def change_value(a_list, b_list, idx):
    tmp = a_list[idx]
    a_list[idx] = b_list[idx]
    b_list[idx] = tmp


n, k = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort(reverse=True)

for idx in range(k):
    change_value(a_list, b_list, idx)

res = 0
for val in a_list:
    res += val
print(res)
