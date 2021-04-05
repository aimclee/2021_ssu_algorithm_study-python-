n, m = map(int, input().split())
arr = list(map(int, input().split()))

res=0
dp = [0] * 11

for i in arr:
    dp[i] += 1



for i in range(1, m + 1):
    n -= dp[i]
    res += dp[i] * n

print(res)