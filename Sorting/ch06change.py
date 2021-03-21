n, k = map(int, input().split())
ans = 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
print(sum(a[-2:])+sum(b[-3:]))

