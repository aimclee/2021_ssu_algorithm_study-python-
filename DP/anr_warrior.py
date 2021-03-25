# f(n) = f(n), n = 1
# f(n) = max(f(n), f(n-1)), n = 2
# f(n) = max(arr[n] + f(n-2), f(n-1)), n>=3

dp = [0] * 100

def ant_warrior(array, n):
    dp[0] = array[0]
    dp[1] = max(array[0], array[1])

    for i in range(2, n):
        dp[i] = max(array[i]+dp[i-2], dp[i-1])
        
    return dp[i]
    
# 데이터 입력
n = int(input())
array = list(map(int, input().split()))

print(ant_warrior(array, n))
