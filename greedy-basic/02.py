n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort(reverse=True)     # 내림차순 정렬

res = 0

for cnt in  range(1, m + 1):
    if int(cnt % k) == 0:
        res += num_list[1]
    else:
        res += num_list[0]

print(res)
