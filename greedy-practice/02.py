# 전략: 0과 1을 제외한 수는 무조건 곱하기 (단, res 가 0인 경우 더해주기)
num_list = list(map(int, input()))

res = 0
while num_list:
    num = num_list.pop(0)
    if num > 1 and res != 0:
        res *= num
    else:
        res += num

print(res)
