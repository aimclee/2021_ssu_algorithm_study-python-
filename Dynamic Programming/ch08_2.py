# 1로 만들기

# 정수를 입력받는다.
x = int(input())
# dynamic programming memoization
d = [0] * (x+1)

def dp(x):
    if x == 1:
        return 0
    if d[x] > 0:
        return d[x]

    d[x] = dp(x-1)+1
    if x % 2 == 0:
        tmp = dp(x//2)+1;
        if d[x] > tmp:
            d[x] = tmp
    if x % 3 == 0:
        tmp = dp(x//3)+1;
        if d[x] > tmp:
            d[x] = tmp

    if x % 5 == 0:
        tmp = dp(x//5)+1;
        if d[x] > tmp:
            d[x] = tmp

    return d[x]

print(dp(x))