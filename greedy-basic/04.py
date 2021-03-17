n, k = map(int, input().split())

res = 0
while n != 1:
    if int(n % k) == 0:
        n = n // k
    else:
        n -= 1
    res += 1

print(res)
