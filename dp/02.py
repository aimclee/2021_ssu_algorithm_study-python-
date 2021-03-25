n = int(input())
warehouse = list(map(int, input().split()))
dp = [0] * 1001

dp[0] = warehouse[0]
dp[1] = warehouse[1]

for cur in range(2, n):
    dp[cur] = max(dp[cur - 1], dp[cur - 2] + warehouse[cur])

print(dp[n - 1])
