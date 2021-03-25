
n, m = map(int, input().split())
payment_list = list()
INF = 99999999
dp = [INF] * 10001
dp[0] = 0

for _ in range(n):
    payment_list.append(int(input()))

for num in range(n):
    for cur in range(payment_list[num], m + 1):
        if dp[cur - payment_list[num]] != INF:
            dp[cur] = min(dp[cur], dp[cur - payment_list[num]] + 1)

if dp[m] == INF:
    print(-1)
else:
    print(dp[m])
