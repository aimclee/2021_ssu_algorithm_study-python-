# 전략: 전체 경우의 수 - 무게가 같은 경우의 수"
from collections import Counter


def get_redpulication_number(weight_list):
    counter = Counter(weight_list)
    res = 0
    for val in counter.values():
        if val > 1:
            res += 1
    return res


def is_even(n):
    if int(n % 2) == 0:
        return True
    else:
        return False


n, m = map(int, input().split())
weight_list = list(map(int, input().split()))
if is_even(n):
    res = (n // 2 - 1) * n + n // 2     # n이 짝수일 경우, 모든 경우의 수 구하기
else:
    res = (n // 2) * n                  # n이 홀수일 경우, 모든 경우의 수 구하기

res -= get_redpulication_number(weight_list)
print(res)
