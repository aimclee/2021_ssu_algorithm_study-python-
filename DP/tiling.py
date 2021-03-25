# f(1) = 1, f(2) = 3
# f(n) = f(n-1) + f(n-2) * 2, n>=3

n = int(input())
dp = [0] * n

dp[0] = 1
dp[1] = 3

for i in range(2, n):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 796796 # dp[i]를 796796로 나눈 나머지
    
print(dp[n])
