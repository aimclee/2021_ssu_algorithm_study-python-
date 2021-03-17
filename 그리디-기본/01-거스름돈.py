n = input(input())
coin = [500, 100, 50, 10]
res = 0

for val in coin:
    res += n // val
    n = int(n % val)

print(res)
