
n, m = map(int, input().split())
# n개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

dp = [10001] * (m + 1)

# Bottom-up
dp[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if dp[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            dp[j] = min(dp[j], dp[j - array[i]] + 1)

if dp[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(dp[m])