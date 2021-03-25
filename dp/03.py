n = int(input())
dp = [0] * 1001

dp[0] = 1
dp[1] = 3

for cur in range(2, n):
    dp[cur] = (dp[cur - 1] + dp[cur - 2] * 2) % 796796

print(dp[n - 1])
