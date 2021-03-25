n = int(input())
#식량 정보 입력
arr = list(map(int, input().split()))

dp = [0] * 100

#Bottom-up
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])
for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

# 계산된 결과 출력
print(dp[n - 1])