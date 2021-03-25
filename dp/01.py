
dp = [0] * 30001
destination = int(input())
next_jump = [5, 3, 2]

for cur in range(2, destination + 1):
    dp[cur] = dp[cur - 1] + 1

    for next_loc in next_jump:
        if cur % next_loc == 0:
            dp[cur] = min(dp[cur], dp[cur // next_loc] + 1)

print(dp[destination])
