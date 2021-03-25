# f(n) = min( f(n/5), f(n/3), f(n/2), f(n-1) ), n>=2 단 f(n/5), f(n/3), f(n/2)는 가능한 경우에만

dp = [0] * 30001 # 입력 가능 숫자 범위 : 0 ~ 30000

def make_it_one(num):
    for i in range(2, num+1):
        dp[i] =  dp[i-1] + 1 # 이것 먼저 해주지 않으면 min = 0(초기화 값)이 된다.
        
        if i % 5 == 0: # 5로 나눠 떨어지는 경우
            dp[i] = min(dp[i], dp[i // 5] + 1) # min(현재 값, 5로 나눈 숫자가 연산한 횟수 + 1)
        elif i % 3 == 0 : # 3으로 나눠 떨어지는 경우
            dp[i] = min(dp[i], dp[i // 3] + 1) # min(현재 값, 3으로 나눈 숫자가 연산한 횟수 + 1)
        elif i % 2 == 0 : # 3으로 나눠 떨어지는 경우
            dp[i] = min(dp[i], dp[i // 2] + 1) # min(현재 값, 2로 나눈 숫자가 연산한 횟수 + 1)
        
    return dp[i]

num = int(input())
print(make_it_one(num))
