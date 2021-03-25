num = int(input())
ans = [0] * (num + 3)

#Top-down
def fibo(n):
    # global ans
    if n == 1 or n == 2:
        return 1

    if ans[n] != 0:
        return ans[n]

    ans[n] = fibo(n - 1) + fibo(n - 2)
    return ans[n]


print(fibo(num))